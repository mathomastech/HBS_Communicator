import sys
from PyQt4 import QtGui
from designer.communicator import Ui_hbsCommunicator #, Ui_loginWindow
from gui import *
from config import *
from communicator import *


class Handler(QtGui.QMainWindow):
    #Handler Class Level Variables
    USERNAME_ENTRY = ""
    PASSWORD_ENTRY = ""

    def __init__(self):
        super(Handler,self).__init__()
        com=Ui_hbsCommunicator()
        com.setupUi(self)
    
        Handler.USERNAME_ENTRY = com.usernameEntry
        Handler.PASSWORD_ENTRY = com.passwordEntry
        GUI.CHANNEL_DISPLAY = com.channelDisplay
        GUI.CHAT_ENTRY = com.chatEntry
        GUI.ROSTER_DISPLAY = com.rosterDisplay
        GUI.LOGIN_STATUS_LABEL = com.loginStatusLabel
        GUI.USER_LABEL = com.userLabel

        self.show()

    def on_loginWindowButton_clicked(self, *args):
        authorize.show_all()

    def on_loginButton_clicked(self, *args):
        username = Handler.USERNAME_ENTRY.text()
        password = Handler.PASSWORD_ENTRY.text()
        print(username)
        Communicator.login(username,password)

    def on_submitButton_clicked(self, *args):
        Communicator.write_chat_to_channel()

    def on_chatEntry_activate(self, *args):
        Handler.on_submitButton_clicked(self, *args)

    def on_passwordEntry_activate(self, *args):
        Handler.on_loginButton_clicked(self, *args)

    def on_usernameEntry_activate(self, *args):
        Handler.on_loginButton_clicked(self, *args)

    # Command Communication Channels
    
    def on_centralCommandButton_clicked(self, *args):
        if Communicator.check_user_permissions("Central Command"):
            log_path = Config.c['Logs'] + 'centcomLog.txt'
            roster_path = Config.c['Rosters'] + 'centcomRoster.txt'
            Communicator.populate_channel(log_path,roster_path)

        else: 
            Communicator.invalid_permissions()
    def on_operationsCommandButton_clicked(self, *args):
        if Communicator.check_user_permissions("Operations Command"):
            log_path = Config.c['Logs'] + 'operationsCommandLog.txt'
            roster_path = Config.c['Rosters'] + 'operationsCommandRoster.txt'
            Communicator.populate_channel(log_path,roster_path)
        else: 
            Communicator.invalid_permissions()
   
    def on_codCommandButton_clicked(self, *args):
        if Communicator.check_user_permissions("Call of Duty Command"):
            log_path = Config.c['Logs'] + 'codCommandLog.txt'
            roster_path = Config.c['Rosters'] + 'codCommandRoster.txt'
            Communicator.populate_channel(log_path,roster_path)
        else: 
            Communicator.invalid_permissions()

    def on_rustCommandButton_clicked(self, *args):
        if Communicator.check_user_permissions("Rust Command"):
            log_path = Config.c['Logs'] + 'rustCommandLog.txt'
            roster_path = Config.c['Rosters'] + 'rustCommandRoster.txt'
            Communicator.populate_channel(log_path,roster_path)
        else: 
            Communicator.invalid_permissions()
    
    def on_gwCommandButton_clicked(self, *args):
        if Communicator.check_user_permissions("Guild Wars Command"):
            log_path = Config.c['Logs'] + 'gwCommandLog.txt'
            roster_path = Config.c['Rosters'] + 'gwCommandRoster.txt'
            Communicator.populate_channel(log_path,roster_path)
        else: 
            Communicator.invalid_permissions()
    
    def on_wowCommandButton_clicked(self, *args):
        if Communicator.check_user_permissions("World of Warcraft Command"):
            log_path = Config.c['Logs'] + 'wowCommandLog.txt'
            roster_path = Config.c['Rosters'] + 'wowCommandRoster.txt'
            Communicator.populate_channel(log_path,roster_path)
        else: 
            Communicator.invalid_permissions()
    
    def on_mcCommandButton_clicked(self, *args):
        if Communicator.check_user_permissions("Minecraft Command"):
            log_path = Config.c['Logs'] + 'mcCommandLog.txt'
            roster_path = Config.c['Rosters'] + 'mcCommandRoster.txt'
            Communicator.populate_channel(log_path,roster_path)
        else: 
            Communicator.invalid_permissions()
    
    def on_dayzCommandButton_clicked(self, *args):
        if Communicator.check_user_permissions("DayZ Command"):
            log_path = Config.c['Logs'] + 'armaCommandLog.txt'
            roster_path = Config.c['Rosters'] + 'armaCommandRoster.txt'
            Communicator.populate_channel(log_path,roster_path)
        else: 
            Communicator.invalid_permissions()
    
    def on_logisticsCommandButton_clicked(self, *args):
        if Communicator.check_user_permissions("Logistics Command"):
            log_path = Config.c['Logs'] + 'logisticsCommandLog.txt'
            roster_path = Config.c['Rosters'] + 'logisticsCommandRoster.txt'
            Communicator.populate_channel(log_path,roster_path)
        else: 
            Communicator.invalid_permissions()
    
    def on_mpCommandButton_clicked(self, *args):
        if Communicator.check_user_permissions("Military Police"):
            log_path = Config.c['Logs'] + 'mpCommandLog.txt'
            roster_path = Config.c['Rosters'] + 'mpCommandRoster.txt'
            Communicator.populate_channel(log_path,roster_path)
        else: 
            Communicator.invalid_permissions()
    
    def on_admissionsCommandButton_clicked(self, *args):
        if Communicator.check_user_permissions("Admissions"):
            log_path = Config.c['Logs'] + 'admissionsCommandLog.txt'
            roster_path = Config.c['Rosters'] + 'admissionsCommandRoster.txt'
            Communicator.populate_channel(log_path,roster_path)
        else: 
            Communicator.invalid_permissions()
    
    # General Communicator Channels
    
    def on_generalButton_clicked(self, *args):
        log_path = Config.c['Logs'] + 'generalLog.txt'
        roster_path = Config.c['Rosters'] + 'generalRoster.txt'
        Communicator.populate_channel(log_path,roster_path)

    def on_codGeneralButton_clicked(self, *args):
        log_path = Config.c['Logs'] + 'codLog.txt'
        roster_path = Config.c['Rosters'] + 'codRoster.txt'
        Communicator.populate_channel(log_path,roster_path)
    
    def on_rustGeneralButton_clicked(self, *args):
        log_path = Config.c['Logs'] + 'rustLog.txt'
        roster_path = Config.c['Rosters'] + 'rustRoster.txt'
        Communicator.populate_channel(log_path,roster_path)
    
    def on_gwGeneralButton_clicked(self, *args):
        log_path = Config.c['Logs'] + 'gwLog.txt'
        roster_path = Config.c['Rosters'] + 'gwRoster.txt'
        Communicator.populate_channel(log_path,roster_path)
    
    def on_wowGeneralButton_clicked(self, *args):
        log_path = Config.c['Logs'] + 'wowLog.txt'
        roster_path = Config.c['Rosters'] + 'wowRoster.txt'
        Communicator.populate_channel(log_path,roster_path)
    
    def on_mcGeneralButton_clicked(self, *args):
        log_path = Config.c['Logs'] + 'mcLog.txt'
        roster_path = Config.c['Rosters'] + 'mcRoster.txt'
        Communicator.populate_channel(log_path,roster_path)
    
    def on_armaGeneralButton_clicked(self, *args):
        log_path = Config.c['Logs'] + 'armaLog.txt'
        roster_path = Config.c['Rosters'] + 'armaRoster.txt'
        Communicator.populate_channel(log_path,roster_path)

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Handler()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()
