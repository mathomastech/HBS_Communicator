from configuration import *
from communicator import *

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

    def on_passwordEntry_activate(self, *args):
        Handler.on_loginButton_clicked(self, *args)

    def on_usernameEntry_activate(self, *args):
        Handler.on_loginButton_clicked(self, *args)

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
    
    def on_gwCommandButton_clicked(self, *args):
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
    
    def on_gwGeneralButton_clicked(self, *args):
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
