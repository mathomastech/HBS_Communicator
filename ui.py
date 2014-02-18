from gi.repository import Gtk
import os.path
#Initialize communicator XML objects
gui = Gtk.Builder()
gui.add_from_file("communicator.glade")
main_app = gui.get_object("hbsCommunicator")

#Initialize loginWindow XML objects
loginWindow = Gtk.Builder()
loginWindow.add_from_file("loginWindow.glade")
authorize = loginWindow.get_object("loginWindow")

#Command Buttons
central_command_button = gui.get_object("centralCommandButton")
operations_command_button = gui.get_object("operationsCommandButton")
cod_command_button = gui.get_object("codCommandButton")
rust_command_button = gui.get_object("rustCommandButton")
gw_command_button = gui.get_object("gwCommandButton")
wow_command_button = gui.get_object("wowCommandButton")
mc_command_button = gui.get_object("mcCommandButton")
arma_command_button = gui.get_object("armaCommandButton")
logistics_command_button = gui.get_object("logisticsCommandButton")
mp_command_button = gui.get_object("mpCommandButton")
admissions_command_button = gui.get_object("admissionsCommandButton")
#General Buttons
general_button = gui.get_object("generalButton")
cod_general_button = gui.get_object("ccodGeneralButton")
rust_general_button = gui.get_object("rustGeneralButton")
gw_general_button = gui.get_object("gwGeneralButton")
wow_general_button = gui.get_object("wowGeneralButton")
mc_general_button = gui.get_object("mcGeneralButton")
arma_general_button = gui.get_object("armaGeneralButton")
#Channel and Roster Elements
chat_entry = gui.get_object("chatEntry")
submit_button = gui.get_object("submitButton")
info_display = gui.get_object("infoDisplay")
roster_display = gui.get_object("rosterDisplay")
#Login Window Text Entrys
username_entry = loginWindow.get_object("usernameEntry")
password_entry = loginWindow.get_object("passwordEntry")


#Global Variables
LOG_PATH = "logs/"
ACTIVE_LOG_PATH = ''
WELCOME_MESSAGE = LOG_PATH + 'welcomeMessage.txt'
ROSTER_PATH = "roster/"
ACTIVE_ROSTER_PATH = ''
USER_PATH = "users.txt"

USER = "Sniper_Zero"

#populate TextView with Welcome Message
f = open(WELCOME_MESSAGE, 'r')
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
                else:
                    print("Incorrect Password. Try again.")
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
class Handler:
    def on_hbsCommunicator_delete_event(self,*args):
        Gtk.main_quit(*args)

    def on_loginWindowButton_clicked(self, *args):
        authorize.show_all()

    def on_loginButton_clicked(self, *args):
        username = username_entry.get_text()
        password = password_entry.get_text()
        Communicator.login(username,password)

    def on_submitButton_clicked(self, *args):
        info_buffer = info_display.get_buffer()
        chat_input = chat_entry.get_text()
        if (chat_input != ""):        
            chat_input += '\n' 
            info_buffer.insert(info_buffer.get_end_iter(),USER + ": " +  chat_input)
            f = open(ACTIVE_LOG_PATH, 'a')
            f.write(USER + ": " + chat_input)
            f.close()
            chat_entry.set_text("")

    def on_chatEntry_activate(self, *args):
        Handler.on_submitButton_clicked(self, *args)

    # Command Communication Channels
    
    def on_centralCommandButton_clicked(self, *args):
        log_path = LOG_PATH + 'centcomLog.txt'
        roster_path = ROSTER_PATH + 'centcomRoster.txt'
        Communicator.channel_switch(log_path,roster_path)

    def on_operationsCommandButton_clicked(self, *args):
        log_path = LOG_PATH + 'operationsCommandLog.txt'
        roster_path = ROSTER_PATH + 'operationsCommandRoster.txt'
        Communicator.channel_switch(log_path,roster_path)
   
    def on_codCommandButton_clicked(self, *args):
        log_path = LOG_PATH + 'codCommandLog.txt'
        roster_path = ROSTER_PATH + 'codCommandRoster.txt'
        Communicator.channel_switch(log_path,roster_path)

    def on_rustCommandButton_clicked(self, *args):
        log_path = LOG_PATH + 'rustCommandLog.txt'
        roster_path = ROSTER_PATH + 'rustCommandRoster.txt'
        Communicator.channel_switch(log_path,roster_path)
    
    def on_guildWarsCommandButton_clicked(self, *args):
        log_path = LOG_PATH + 'gwCommandLog.txt'
        roster_path = ROSTER_PATH + 'gwCommandRoster.txt'
        Communicator.channel_switch(log_path,roster_path)
    
    def on_wowCommandButton_clicked(self, *args):
        log_path = LOG_PATH + 'wowCommandLog.txt'
        roster_path = ROSTER_PATH + 'wowCommandRoster.txt'
        Communicator.channel_switch(log_path,roster_path)
    
    def on_mcCommandButton_clicked(self, *args):
        log_path = LOG_PATH + 'mcCommandLog.txt'
        roster_path = ROSTER_PATH + 'mcCommandRoster.txt'
        Communicator.channel_switch(log_path,roster_path)
    
    def on_armaCommandButton_clicked(self, *args):
        log_path = LOG_PATH + 'armaCommandLog.txt'
        roster_path = ROSTER_PATH + 'armaCommandRoster.txt'
        Communicator.channel_switch(log_path,roster_path)
    
    def on_logisticsCommandButton_clicked(self, *args):
        log_path = LOG_PATH + 'logisticsCommandLog.txt'
        roster_path = ROSTER_PATH + 'logisticsCommandRoster.txt'
        Communicator.channel_switch(log_path,roster_path)
    
    def on_mpCommandButton_clicked(self, *args):
        log_path = LOG_PATH + 'mpCommandLog.txt'
        roster_path = ROSTER_PATH + 'mpCommandRoster.txt'
        Communicator.channel_switch(log_path,roster_path)
    
    def on_admissionsCommandButton_clicked(self, *args):
        log_path = LOG_PATH + 'admissionsCommandLog.txt'
        roster_path = ROSTER_PATH + 'admissionsCommandRoster.txt'
        Communicator.channel_switch(log_path,roster_path)
    
    # General Communicator Channels
    
    def on_generalButton_clicked(self, *args):
        log_path = LOG_PATH + 'generalLog.txt'
        roster_path = ROSTER_PATH + 'generalRoster.txt'
        Communicator.channel_switch(log_path,roster_path)

    def on_codGeneralButton_clicked(self, *args):
        log_path = LOG_PATH + 'codLog.txt'
        roster_path = ROSTER_PATH + 'codRoster.txt'
        Communicator.channel_switch(log_path,roster_path)
    
    def on_rustGeneralButton_clicked(self, *args):
        log_path = LOG_PATH + 'rustLog.txt'
        roster_path = ROSTER_PATH + 'rustRoster.txt'
        Communicator.channel_switch(log_path,roster_path)

    def on_guildWarsGeneralButton_clicked(self, *args):
        log_path = LOG_PATH + 'gwLog.txt'
        roster_path = ROSTER_PATH + 'gwRoster.txt'
        Communicator.channel_switch(log_path,roster_path)

    def on_wowGeneralButton_clicked(self, *args):
        log_path = LOG_PATH + 'wowLog.txt'
        roster_path = ROSTER_PATH + 'wowRoster.txt'
        Communicator.channel_switch(log_path,roster_path)

    def on_mcGeneralButton_clicked(self, *args):
        log_path = LOG_PATH + 'mcLog.txt'
        roster_path = ROSTER_PATH + 'mcRoster.txt'
        Communicator.channel_switch(log_path,roster_path)

    def on_armaGeneralButton_clicked(self, *args):
        log_path = LOG_PATH + 'armaLog.txt'
        roster_path = ROSTER_PATH + 'armaRoster.txt'
        Communicator.channel_switch(log_path,roster_path)



gui.connect_signals(Handler())
loginWindow.connect_signals(Handler())
main_app.show_all()
Gtk.main()
