import sys, time
from PyQt4 import QtGui, QtCore
from ui_communicator import Ui_hbsCommunicator
from gui import GUI
from config import Config
from communicator import Communicator
from worker import Worker

class Handler(QtGui.QMainWindow):
    # Handler Class Level Variables
    USERNAME_ENTRY = ""
    PASSWORD_ENTRY = ""
    refresh_signal = QtCore.pyqtSignal()

    # Threading
    QtCore.QThread.currentThread().setObjectName("MAIN")
    thread = QtCore.QThread()
    thread.name = "auto_refresh"
    worker = Worker()
    worker.moveToThread(thread)
    worker.start()
    worker.refresh_signal.connect(Communicator.update_channel)
    #thread.connect(thread, QtCore.SIGNAL('refresh_signal'), Communicator.update_channel)
    
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
        GUI.REFRESH_BUTTON = com.refreshButton
        
        # Login Window Widgets
        GUI.LOGIN_GROUP_BOX = com.loginGroupBox
        GUI.USERNAME_LABEL = com.usernameLabel
        GUI.USERNAME_ENTRY = com.usernameEntry
        GUI.PASSWORD_LABEL = com.passwordLabel
        GUI.PASSWORD_ENTRY = com.passwordEntry
        GUI.LOGIN_BTN = com.loginButton
        
        self.show()

    def on_loginButton_clicked(self, *args):
        username = Handler.USERNAME_ENTRY.text()
        password = Handler.PASSWORD_ENTRY.text()
        Communicator.login(username,password)

    def on_submitButton_clicked(self, *args):
        Communicator.write_chat_to_channel()

    def on_chatEntry_returnPressed(self, *args):
        Handler.on_submitButton_clicked(self, *args)

    def on_passwordEntry_returnPressed(self, *args):
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
    
    def on_tfCommandButton_clicked(self, *args):
        if Communicator.check_user_permissions("Titan Fall Command"):
            log_path = Config.c['Logs'] + 'tfCommandLog.txt'
            roster_path = Config.c['Rosters'] + 'tfCommandRoster.txt'
            Communicator.populate_channel(log_path,roster_path)
        else: 
            Communicator.invalid_permissions()
    
    def on_csCommandButton_clicked(self, *args):
        if Communicator.check_user_permissions("Counter Strike Command"):
            log_path = Config.c['Logs'] + 'csCommandLog.txt'
            roster_path = Config.c['Rosters'] + 'csCommandRoster.txt'
            Communicator.populate_channel(log_path,roster_path)
        else: 
            Communicator.invalid_permissions()
    
    def on_lolCommandButton_clicked(self, *args):
        if Communicator.check_user_permissions("League of Legends Command"):
            log_path = Config.c['Logs'] + 'lolCommandLog.txt'
            roster_path = Config.c['Rosters'] + 'lolCommandRoster.txt'
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
    
    def on_tfGeneralButton_clicked(self, *args):
        log_path = Config.c['Logs'] + 'tfLog.txt'
        roster_path = Config.c['Rosters'] + 'tfRoster.txt'
        Communicator.populate_channel(log_path,roster_path)
    
    def on_csGeneralButton_clicked(self, *args):
        log_path = Config.c['Logs'] + 'csLog.txt'
        roster_path = Config.c['Rosters'] + 'csRoster.txt'
        Communicator.populate_channel(log_path,roster_path)
    
    def on_lolGeneralButton_clicked(self, *args):
        log_path = Config.c['Logs'] + 'lolLog.txt'
        roster_path = Config.c['Rosters'] + 'lolRoster.txt'
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
    
    def on_dayzGeneralButton_clicked(self, *args):
        log_path = Config.c['Logs'] + 'armaLog.txt'
        roster_path = Config.c['Rosters'] + 'armaRoster.txt'
        Communicator.populate_channel(log_path,roster_path)
