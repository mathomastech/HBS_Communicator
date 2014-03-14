from configuration import *
from database import *
import os.path

#populate TextView with Welcome Message
f = open(LOG_PATH + "welcomeMessage.txt", 'r')
info_buffer = info_display.get_buffer()
chat_input = f.read()
info_buffer.set_text(chat_input) 
f.close()

#USER = ''
#USER_PERMISSIONS = []

class Communicator:
    USER = ""
    USER_PERMISSIONS = []
    
    def channel_switch(log_path,roster_path):
        if os.path.isfile(log_path):
            Communicator.write_to_channel(log_path)
        else:
            Communicator.write_to_channel_no_log(log_path)
        if os.path.isfile(roster_path):
            Communicator.write_to_roster(roster_path)
        else:
            Communicator.write_to_roster_no_roster(roster_path)

    def write_to_channel(current_log_path):
        global ACTIVE_LOG_PATH
        f = open(current_log_path, 'r')
        info_buffer = info_display.get_buffer()
        chat_input = f.read()
        info_buffer.set_text(chat_input) 
        f.close()
        ACTIVE_LOG_PATH = current_log_path

    def write_to_channel_no_log(current_log_path):
        global ACTIVE_LOG_PATH
        info_buffer = info_display.get_buffer()
        chat_input = "No logs for this channel yet.\n"
        info_buffer.set_text(chat_input) 
        ACTIVE_LOG_PATH = current_log_path
        
    def write_to_roster(current_roster_path):
        global ACTIVE_ROSTER_PATH
        f = open(current_roster_path, 'r')
        info_buffer = roster_display.get_buffer()
        roster_input = f.read()
        info_buffer.set_text(roster_input)
        f.close()
        ACTIVE_ROSTER_PATH = current_roster_path
    
    def write_to_roster_no_roster(current_roster_path):
        global ACTIVE_ROSTER_PATH
        info_buffer = roster_display.get_buffer()
        roster_input = "There is currently no roster for this channel\n"
        info_buffer.set_text(roster_input)
        ACTIVE_ROSTER_PATH = current_roster_path

    def write_chat_to_channel():
        chat_input = chat_entry.get_text()
        if (chat_input != ""):
            chat_input += '\n'
            info_buffer.insert(info_buffer.get_end_iter(),Communicator.USER + ": " + chat_input)
            f = open(ACTIVE_LOG_PATH, 'a')
            f.write(Communicator.USER + ": " + chat_input)
            f.close()
            chat_entry.set_text("")
    
    def login(username,password):
        flag, userPermissions, channelPermissions = Database.login(username,password)
        
        if flag:
           # global USER
           # global USER_PERMISSIONS
            Communicator.USER = username
            Communicator.USER_PERMISSIONS = userPermissions
    
    def check_user_permissions(channel):
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
        
        print(permissions)
        print(Communicator.USER_PERMISSIONS)
        for i in range(0,len(Communicator.USER_PERMISSIONS)):
            for j in range(0,len(permissions)):
                if Communicator.USER_PERMISSIONS[i] == permissions[j]:
                    return True
        return False
    
    def invalid_permissions():
        info_buffer = info_display.get_buffer()
        info_buffer.set_text("You do not have sufficient privaledges to view this channel. If you feel this is in error, please contact an administrator")
