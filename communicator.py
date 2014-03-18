from gui import *
from database import *
from ssh import *
from config import *

import os.path


class Communicator:
    #Communicator Class Level Variables 
    USER = ""
    USER_PERMISSIONS = []
    ACTIVE_LOG_PATH = ""
    ACTIVE_ROSTER_PATH = ""
    SSH_CONNECTION = SSH.connect_to_ssh()

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
        info_buffer = GUI.INFO_DISPLAY.get_buffer()
        info_buffer.set_text(log) 
        Communicator.ACTIVE_LOG_PATH = current_log_path

    def write_to_roster(current_roster_path):
        # Write roster to the currently selected channel
        f = open(current_roster_path, 'r')
        info_buffer = GUI.ROSTER_DISPLAY.get_buffer()
        roster_input = f.read()
        info_buffer.set_text(roster_input)
        f.close()
        Communicator.ACTIVE_ROSTER_PATH = current_roster_path
    
    def write_to_roster_no_roster(current_roster_path):
        info_buffer = GUI.ROSTER_DISPLAY.get_buffer()
        roster_input = "There is currently no roster for this channel\n"
        info_buffer.set_text(roster_input)
        Communicator.ACTIVE_ROSTER_PATH = current_roster_path

    def write_chat_to_channel():
        # Take chat box text and write it to channel and log.
        chat_input = GUI.CHAT_ENTRY.get_text()
        if (chat_input != ""):
            log = Communicator.USER + ": " + chat_input
            SSH.write_to_log(Communicator.SSH_CONNECTION,
                                Communicator.ACTIVE_LOG_PATH, log)
            Communicator.update_channel()
            GUI.CHAT_ENTRY.set_text("")

    
    def login(username,password):
        # Set user login and permissions
        flag, userPermissions, channelPermissions = Database.login(username,password)
        
        if flag:
            Communicator.USER = username
            Communicator.USER_PERMISSIONS = userPermissions
            #populate TextView with Welcome Message
            Communicator.populate_channel(Config.c['Logs'] + 'welcomeMessage.txt', Config.c['Rosters'] + 'generalRoster.txt')
            
    
    def check_user_permissions(channel):
        # Check if currently logged in user has permissions to view selected channel
        if channel == "Central Command":
            permissions = [9,10,54]
        if channel == "Operations Command":
            permissions = [9,10,54,57,62,63]
        if channel == "Call of Duty Command":
            permissions = [9,10,57]
        if channel == "Rust Command":
            permissions = [9,10,62]
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
            #Need admissions group of forums
        
        for i in range(0,len(Communicator.USER_PERMISSIONS)):
            for j in range(0,len(permissions)):
                if Communicator.USER_PERMISSIONS[i] == permissions[j]:
                    return True
        return False
    
    def invalid_permissions():
        # If user does not have appropriate permissions, print out message.
        info_buffer = GUI.INFO_DISPLAY.get_buffer()
        info_buffer.set_text("You do not have sufficient privaledges to view this channel. If you feel this is in error, please contact an administrator")
