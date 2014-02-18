from configuration import *
import os.path

#populate TextView with Welcome Message
f = open(LOG_PATH + "welcomeMessage.txt", 'r')
info_buffer = info_display.get_buffer()
chat_input = f.read()
info_buffer.set_text(chat_input) 
f.close()


class Communicator:
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

    def login(username,password):
        f = open(USER_PATH, 'r')
        while True:
            line = f.readline()
            if len(line) == 0:
                print("No user found")
                break
            user = line.split(",")
            if user[0] == username:
                if user[4] == password:
                    print("Success!")
                    break
                else:
                    print("Incorrect Password.")
                    break
'''
Permission Groups:

1: Central Command
2: Operations Command
3: Logistics Command
100: Regiment Command
101: Call of Duty
102: Rust
103: World of Warcraft
104: Guild Wars
105: League of Legends
106: Minecraft
107: DayZ
108: CS:GO
5: Member
6: Unregistered
'''



#gui.connect_signals(Handler())
#loginWindow.connect_signals(Handler())
#main_app.show_all()
#Gtk.main()
