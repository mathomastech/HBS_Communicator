import sys, time, os.path
from PyQt4 import QtGui, QtCore
from ui_communicator import Ui_hbsCommunicator
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

    def __init__(self):
        super(Communicator,self).__init__()
  
    def update_channel():
        # Call this function to refresh the currently selected channel
        Communicator.populate_channel(Communicator.ACTIVE_LOG_PATH,
                            Communicator.ACTIVE_ROSTER_PATH)
        
    def populate_channel(log_path,roster_path):
        # Populate the channel with both logs and rosters
        log = SSH.get_log(Communicator.SSH_CONNECTION, log_path)
        Communicator.write_to_channel(log_path,log)
        if os.path.isfile(roster_path):
            Communicator.write_to_roster(roster_path)
        else:
            Communicator.write_to_roster_no_roster(roster_path)

    def write_to_channel(current_log_path,log):
        # Write log to the currently selected channel
        GUI.CHANNEL_DISPLAY.setPlainText(log)
        Communicator.ACTIVE_LOG_PATH = current_log_path

    def write_to_roster(current_roster_path):
        f = open(current_roster_path, 'r')
        f.close()
        #GUI.ROSTER_DISPLAY.setPlainText(log)
        Communicator.ACTIVE_ROSTER_PATH = current_roster_path
    
    def write_to_roster_no_roster(current_roster_path):
        GUI.ROSTER_DISPLAY.setPlainText("There is currently no roster for this channel\n")
        Communicator.ACTIVE_ROSTER_PATH = current_roster_path

    def write_chat_to_channel():
        # Take chat box text and write it to channel and log.
        chat_input = GUI.CHAT_ENTRY.text()
        if (chat_input != ""):
            log = Communicator.USER + ": " + chat_input
            SSH.write_to_log(Communicator.SSH_CONNECTION,
                                Communicator.ACTIVE_LOG_PATH, log)
            Communicator.update_channel()
            GUI.CHAT_ENTRY.setText("")

    def login(username,password):
        # Set user login and permissions
        GUI.LOGIN_STATUS_LABEL.setText("Authenticating...")
        flag, userPermissions, channelPermissions = Database.login(username,password)
        if flag:
            # If True, set the username and user permissions. Hide the login and set 
            # the welcome message. Begin the worker loop to check channels for updates. 
            Communicator.USER = username
            Communicator.USER_PERMISSIONS = userPermissions
            Communicator.hide_login()
            Communicator.populate_channel(Config.c['Logs'] + 'welcomeMessage.txt', Config.c['Rosters'] + 'generalRoster.txt')
            Communicator.enable_widgets()

    def hide_login():
        # Hide the login box my giving it a 0,0 size. 
        GUI.LOGIN_GROUP_BOX.resize(0,0)
        return

    def enable_widgets():
        GUI.CHAT_ENTRY.setEnabled(True)
        GUI.SUBMIT_BTN.setEnabled(True)
        GUI.CHANNEL_NOTEBOOK.setEnabled(True)
        GUI.CONTENT_NOTEBOOK.setTabEnabled(1, True)
        GUI.USER_BTN.setEnabled(True)

    def check_user_permissions(channel):
        # Check if currently logged in user has permissions to view requested channel
        if channel == "Central Command":
            permissions = [9,10,54]
        if channel == "Operations Command":
            permissions = [9,10,54,57,62,63]
        if channel == "Call of Duty Command":
            permissions = [9,10,57]
        if channel == "Titan Fall Command":
            permissions = [9,10,57]
            # Need to fix permissions
        if channel == "League of Legends Command":
            permissions = [9,10,57]
            # Need to fix permissions
        if channel == "Guild Wars Command":
            permissions = [9,10]
            # Need GW command group on forums
        if channel == "World of Warcraft Command":
            permissions = [9,10,63]
        if channel == "Minecraft Command":
            permissions = [9,10]
            # Need MC command group on forums
        if channel == "DayZ Command":
            permissions = [9,10]
            # Need DayZ group of forums
        if channel == "Logistics Command": 
            permissions = [9,10,54,58,17]
        if channel == "Military Police":
            permissions = [9,10,58,17] 
        if channel == "Admissions":
            permissions = [9,10,58]

    # Need admissions group on forums
        
        for i in range(0,len(Communicator.USER_PERMISSIONS)):
            for j in range(0,len(permissions)):
                if Communicator.USER_PERMISSIONS[i] == permissions[j]:
                    return True
        return False
    
    def invalid_permissions():
        # If user does not have appropriate permissions, print out message.
        GUI.CHANNEL_DISPLAY.setPlainText("You do not have sufficient privaledges to view this channel. If you feel this is in error, please contact an administrator")




def main():
    app = QtGui.QApplication(sys.argv)
    hand = Handler()
    com = Communicator()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()

