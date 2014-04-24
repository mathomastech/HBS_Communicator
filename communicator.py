import sys, time, os.path
from PyQt4 import QtGui, QtCore
#from ui_communicator import Ui_hbsCommunicator
from ui_communicator_windows import Ui_hbsCommunicator
from PyQt4.Qt import QApplication
from handler import *
from gui import GUI
from database import Database
from ssh import SSH
from config import Config

class Communicator:
    #Communicator Class Level Variables 
    USER = ""
    USER_PERMISSIONS = []
    ACTIVE_LOG_PATH = ""
    ACTIVE_ROSTER_PATH = ""
    SSH_CONNECTION = SSH.connect_to_ssh()
    REMEMBER_LOGIN = False   
    TCP_HOST = Config.c['TCP Host']
    TCP_PORT = Config.c['TCP Port']
    # Channel Update Variables
    DELTA = []    
    ACTIVE_CHANNEL = ""

    def __init__(self):
        super(Communicator,self).__init__()
    
    def check_user_permissions(channel):
        for i in range(0,len(GUI.CHANNELS)):
            if channel == GUI.CHANNELS[i][GUI.CHANNEL_NAME]:
                for j in range(len(Communicator.USER_PERMISSIONS)):
                    for k in range(len(GUI.CHANNELS[i][GUI.PERMISSIONS])):
                        if Communicator.USER_PERMISSIONS[j] == GUI.CHANNELS[i][GUI.PERMISSIONS][k]:
                            return True
        return False
    
    def enable_widgets():
        GUI.CHAT_ENTRY.setEnabled(True)
        GUI.SUBMIT_BTN.setEnabled(True)
        GUI.CHANNEL_NOTEBOOK.setEnabled(True)
        GUI.CONTENT_NOTEBOOK.setTabEnabled(1, True)
        GUI.USER_BTN.setEnabled(True)
    
    def invalid_permissions():
        # If user does not have appropriate permissions, print out message.
        GUI.CHANNEL_DISPLAY.setPlainText("You do not have sufficient privileges to view this channel. If you feel this is in error, please contact an administrator")
    
    def load_local_logs():
        for i in range(0,len(GUI.CHANNELS)):
            if(os.path.isfile(GUI.CHANNELS[i][GUI.LOCAL_LOG_PATH])):
                f = open(GUI.CHANNELS[i][GUI.LOCAL_LOG_PATH],'r')
                log = f.read()
                GUI.CHANNELS[i][GUI.LOCAL_TIME_STAMP] = log
                f.close()
    
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
            GUI.LOGIN_GROUP_BOX.resize(0,0)
            Communicator.populate_channel(GUI.WELCOME_LOG, GUI.WELCOME_LOG )
            Communicator.enable_widgets()
            if Communicator.REMEMBER_LOGIN: 
                f = open('credentials.txt', 'w')
                username = username.strip()
                f.write(username + "\n" + password) 
                f.close()
            elif os.path.exists('credentials.txt'):
                os.remove('credentials.txt')

    def populate_channel(log_path,roster_path):
        # Populate the channel with both logs and rosters
        log = SSH.get_active_log(Communicator.SSH_CONNECTION, log_path)
        Communicator.write_to_channel(log_path,log)
        if os.path.isfile(roster_path):
            Communicator.write_to_roster(roster_path)
        else:
            Communicator.write_to_roster_no_roster(roster_path)
     
    def switch_command_channel(channel):
        if Communicator.check_user_permissions(channel):
            for i in range(0,len(GUI.CHANNELS)):
                if GUI.CHANNELS[i][GUI.CHANNEL_NAME] == channel: 
                    log_path = GUI.CHANNELS[i][GUI.SERVER_LOG_PATH]
                    roster_path = GUI.CHANNELS[i][GUI.SERVER_ROSTER_PATH]
                    GUI.CHANNELS[i][GUI.GUI_ELEMENT].setStyleSheet("color:black")
                    Communicator.populate_channel(log_path,roster_path)
                    Communicator.ACTIVE_CHANNEL = channel
        else: 
            Communicator.invalid_permissions()
    
    def switch_general_channel(channel):
        for i in range(0,len(GUI.CHANNELS)):
            if GUI.CHANNELS[i][GUI.CHANNEL_NAME] == channel: 
                log_path = GUI.CHANNELS[i][GUI.SERVER_LOG_PATH]
                roster_path = GUI.CHANNELS[i][GUI.SERVER_ROSTER_PATH]
                GUI.CHANNELS[i][GUI.GUI_ELEMENT].setStyleSheet("color:black")
                Communicator.populate_channel(log_path,roster_path)
                Communicator.ACTIVE_CHANNEL = channel

    def update_active_channel():
        # Call this function to refresh the currently selected channel
        Communicator.populate_channel(Communicator.ACTIVE_LOG_PATH,
                            Communicator.ACTIVE_ROSTER_PATH)
    
    def update_channel(log_path):
        Communicator.populate_channel(log_path,Communicator.ACTIVE_ROSTER_PATH)        

    def update_selected_channels():  
        for i in range(0,len(Communicator.DELTA)):
            for j in range(0,len(GUI.CHANNELS)):
                if(Communicator.DELTA[i][0] == GUI.CHANNELS[j][GUI.CHANNEL_NAME]):
                    GUI.CHANNELS[j][GUI.GUI_ELEMENT].setStyleSheet("color:red")
        Communicator.DELTA = []

    def write_chat_to_channel():
        # Take chat box text and write it to channel and log.
        chat_input = GUI.CHAT_ENTRY.text()
        if (chat_input != ""):
            log = Communicator.USER + ": " + chat_input
            SSH.write_to_log(Communicator.SSH_CONNECTION,
                                Communicator.ACTIVE_LOG_PATH, log)
            Communicator.update_active_channel()
            GUI.CHAT_ENTRY.setText("")
    
    def write_to_channel(current_log_path,log):
        # Write log to the currently selected channel
        GUI.CHANNEL_DISPLAY.setPlainText(log)
        Communicator.ACTIVE_LOG_PATH = current_log_path

        cursor = QtGui.QTextCursor(GUI.CHANNEL_DISPLAY.textCursor())
        cursor.movePosition(QtGui.QTextCursor.End)
        GUI.CHANNEL_DISPLAY.setTextCursor(cursor) 

    def write_to_roster(current_roster_path):
        f = open(current_roster_path, 'r')
        f.close()
        #GUI.ROSTER_DISPLAY.setPlainText(log)
        Communicator.ACTIVE_ROSTER_PATH = current_roster_path
    
    def write_to_roster_no_roster(current_roster_path):
        GUI.ROSTER_DISPLAY.setPlainText("There is currently no roster for this channel\n")
        Communicator.ACTIVE_ROSTER_PATH = current_roster_path


def main():
    app = QtGui.QApplication(sys.argv)
    hand = Handler()
    com = Communicator()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()

