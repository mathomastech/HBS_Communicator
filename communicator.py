import sys, time, os.path
from PyQt4 import QtGui, QtCore
#from ui_communicator import Ui_hbsCommunicator
from ui_communicator_windows import Ui_hbsCommunicator
from PyQt4.Qt import QApplication
from handler import *
from gui import GUI
from database import Database
from ssh import SSH
from roster import Roster
from config import Config

class Communicator:
    #Communicator Class Level Variables 
    USER = ""
    USER_PERMISSIONS = []
    ACTIVE_LOG_PATH = ""
    SSH_CONNECTION = SSH.connect_to_ssh()
    REMEMBER_LOGIN = False   
    TCP_HOST = Config.c['TCP Host']
    TCP_PORT = Config.c['TCP Port']
    # Channel Update Variables
    DELTA = []    
    ONLINE_USERS = []
    ACTIVE_CHANNEL = ""

    def __init__(self):
        super(Communicator,self).__init__()
    
    def check_user_permissions(channel):
        # Cycle through all channels and find the selected one
        for i in range(0,len(GUI.CHANNELS)):
            if channel == GUI.CHANNELS[i][GUI.CHANNEL_NAME]:
                # If channel has no restrictions, allow access
                if not GUI.CHANNELS[i][GUI.PERMISSIONS]:
                    return True
                else:
                    # Check user's permissions against channel permissions. Allow access if matching
                    for j in range(len(Communicator.USER_PERMISSIONS)):
                        for k in range(len(GUI.CHANNELS[i][GUI.PERMISSIONS])):
                            if Communicator.USER_PERMISSIONS[j] == GUI.CHANNELS[i][GUI.PERMISSIONS][k]:
                                return True
        return False
    
    def enable_widgets():
        # After a successful login, enable all widgets on application.
        GUI.CHAT_ENTRY.setEnabled(True)
        GUI.SUBMIT_BTN.setEnabled(True)
        GUI.CHANNEL_NOTEBOOK.setEnabled(True)
        GUI.CONTENT_NOTEBOOK.setTabEnabled(1, True)
        GUI.USER_BTN.setEnabled(True)
    
    def invalid_permissions():
        # If user does not have appropriate permissions, print out message.
        GUI.CHANNEL_DISPLAY.setPlainText("You do not have sufficient privileges to view this channel. If you feel this is in error, please contact an administrator")

    def load_local_logs():
        # Load users last online timestamps for each channel 
        for i in range(0,len(GUI.CHANNELS)):
            if(os.path.isfile(GUI.CHANNELS[i][GUI.LOCAL_LOG_PATH])):
                f = open(GUI.CHANNELS[i][GUI.LOCAL_LOG_PATH],'r')
                log = f.read()
                GUI.CHANNELS[i][GUI.LOCAL_TIME_STAMP] = log
                f.close()
    
    def load_local_roster():
        # Load rosters from database into application.
        roster = Roster.get_roster_raw()

        for i in range(0,len(roster)):
            for j in range(0,len(GUI.CHANNELS)):
                for k in range(0,len(GUI.CHANNELS[j][GUI.ROSTER_GROUP_NAME])):
                    if roster[i][0] == GUI.CHANNELS[j][GUI.ROSTER_GROUP_NAME][k]:
                        GUI.CHANNELS[j][GUI.ROSTER].append(roster[i])
                    if roster[i][2] == GUI.CHANNELS[j][GUI.ROSTER_GROUP_NAME][k]:
                        GUI.CHANNELS[j][GUI.ROSTER].append(roster[i])
                    
    def login(username,password):
        # Set user login and permissions
        username = username.strip()
        password = password.strip()
        GUI.LOGIN_STATUS_LABEL.setText("Authenticating...")
        flag, userPermissions, channelPermissions = Database.login(username,password)
        #Communicator.populate_logs()
        if flag:
            # If True, set the username and user permissions. Hide the login and set 
            # the welcome message and announcement. 
            Communicator.USER = username
            Communicator.USER_PERMISSIONS = userPermissions
            Communicator.load_local_logs()
            Communicator.load_local_roster()
            GUI.LOGIN_GROUP_BOX.resize(0,0)
            Communicator.populate_channel(GUI.WELCOME_LOG)
            cursor = QtGui.QTextCursor(GUI.CHANNEL_DISPLAY.textCursor())
            cursor.movePosition(QtGui.QTextCursor.Start)
            GUI.CHANNEL_DISPLAY.setTextCursor(cursor) 
            Communicator.enable_widgets()
            # If user requests password remembers, write info out to file.
            if Communicator.REMEMBER_LOGIN: 
                f = open('credentials.txt', 'w')
                username = username.strip()
                f.write(username + "\n" + password) 
                f.close()
            elif os.path.exists('credentials.txt'):
                os.remove('credentials.txt')


    def online_list():
        # Get a list of all currently logged in users
        list = ""
        for i in range(0,len(Communicator.ONLINE_USERS)):
            list += Communicator.ONLINE_USERS[i] + '\n'

        GUI.ONLINE_LIST.setPlainText(list)

    def populate_channel(log_path):
        # Populate the channel with both logs and rosters
        log = SSH.get_active_log(Communicator.SSH_CONNECTION,log_path) #,Communicator.TCP_HOST, Communicator.TCP_PORT)
        Communicator.write_to_channel(log_path,log)
        Communicator.write_to_roster()
    
    def switch_command_channel(channel):
        # After user requests access to a channel, check his permissions and allow entry if 
        # permissions are acceptable.
        if Communicator.check_user_permissions(channel):
            for i in range(0,len(GUI.CHANNELS)):
                if GUI.CHANNELS[i][GUI.CHANNEL_NAME] == channel: 
                    log_path = GUI.CHANNELS[i][GUI.SERVER_LOG_PATH]
                    GUI.CHANNELS[i][GUI.GUI_ELEMENT].setStyleSheet("color:black")
                    index = GUI.CHANNEL_TAB.currentIndex()
                    GUI.CHANNEL_TAB.tabBar().setTabTextColor(index, QtGui.QColor(0,0,0)) # Black
                    Communicator.populate_channel(log_path)
                    Communicator.ACTIVE_CHANNEL = channel
        else: 
            Communicator.invalid_permissions()
    
    def switch_general_channel(channel):
        # After user requests access to a channel, switch to channel

        #### TO-DO: Replace this and "switch_command_channel" with "switch_channel". No need for duplicate code.
        for i in range(0,len(GUI.CHANNELS)):
            if GUI.CHANNELS[i][GUI.CHANNEL_NAME] == channel: 
                log_path = GUI.CHANNELS[i][GUI.SERVER_LOG_PATH]
                GUI.CHANNELS[i][GUI.GUI_ELEMENT].setStyleSheet("color:black")
                index = GUI.CHANNEL_TAB.currentIndex()
                GUI.CHANNEL_TAB.tabBar().setTabTextColor(index, QtGui.QColor(0,0,0)) # Black
                Communicator.populate_channel(log_path)
                Communicator.ACTIVE_CHANNEL = channel

    def update_active_channel():
        # Call this function to refresh the currently selected channel
        Communicator.populate_channel(Communicator.ACTIVE_LOG_PATH)
    
    def update_channel(log_path):
        Communicator.populate_channel(log_path)        

    def update_selected_channels():  
        # Show updates to channels and tabs with visual indicators as changes occur
        # Cycle through all changed channels
        for i in range(0,len(Communicator.DELTA)):
            for j in range(0,len(GUI.CHANNELS)):
                # Compare changed channels with all channels
                if(Communicator.DELTA[i][0] == GUI.CHANNELS[j][GUI.CHANNEL_NAME]):
                    # If a channel has changes, check to see if the channel is accessible by
                    # currently logged in user. If so, visually indicate a change, otherwise
                    # do not show any indicator.
                    if Communicator.check_user_permissions(GUI.CHANNELS[j][GUI.CHANNEL_NAME]):
                        GUI.CHANNELS[j][GUI.GUI_ELEMENT].setStyleSheet("color:red")
                        # Visually indicate any tabs that also have new posts in channels
                        if GUI.CHANNELS[j][GUI.CHANNEL_GROUP] == 'command':
                            GUI.CHANNEL_TAB.tabBar().setTabTextColor(0, QtGui.QColor(255,0,0)) # Red
                        elif GUI.CHANNELS[j][GUI.CHANNEL_GROUP] == 'general':
                            GUI.CHANNEL_TAB.tabBar().setTabTextColor(1, QtGui.QColor(255,0,0)) # Red
        Communicator.DELTA = []

    def write_chat_to_channel():
        # Take chat box text and write it to channel and log.
        chat_input = GUI.CHAT_ENTRY.text()
        if (chat_input != ""):
            log = Communicator.USER + ": " + chat_input
            SSH.write_to_log(Communicator.ACTIVE_LOG_PATH, log, 
                                Communicator.TCP_HOST, Communicator.TCP_PORT)
            Communicator.update_active_channel()
            GUI.CHAT_ENTRY.setText("")
    
    def write_to_channel(current_log_path,log):
        # Write log to the currently selected channel
        GUI.CHANNEL_DISPLAY.setPlainText(log)
        Communicator.ACTIVE_LOG_PATH = current_log_path

        cursor = QtGui.QTextCursor(GUI.CHANNEL_DISPLAY.textCursor())
        cursor.movePosition(QtGui.QTextCursor.End)
        GUI.CHANNEL_DISPLAY.setTextCursor(cursor) 

    def write_to_roster():
        # Get rosters and apply them to all channels
        roster = ""
        for i in range(0,len(GUI.CHANNELS)):
            if GUI.CHANNELS[i][GUI.CHANNEL_NAME] == Communicator.ACTIVE_CHANNEL:
                for j in range(0, len(GUI.CHANNELS[i][GUI.ROSTER])):
                    roster += str(GUI.CHANNELS[i][GUI.ROSTER][j][1]) + " - " + str(GUI.CHANNELS[i][GUI.ROSTER][j][2]) + "\n"

        GUI.ROSTER_DISPLAY.setPlainText(roster)
    
def main():
    app = QtGui.QApplication(sys.argv)
    hand = Handler()
    com = Communicator()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()

