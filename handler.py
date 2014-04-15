import sys, time
from PyQt4 import QtGui, QtCore
#from ui_communicator import Ui_hbsCommunicator
from ui_communicator_windows import Ui_hbsCommunicator
from gui import GUI
from config import Config
from communicator import Communicator
from worker import Worker

class Handler(QtGui.QMainWindow):
    # Handler Class Level Variables
    USERNAME_ENTRY = ""
    PASSWORD_ENTRY = ""
    REMEMBER_LOGIN = "False"
    refresh_signal = QtCore.pyqtSignal()
    
    #Communicator Test
    #Communicator.LOCAL_LOGS.append(('Beta2','Testin!2'))
    #print(Communicator.LOCAL_LOGS)
    #Communicator.REMOTE_LOGS.append(('Beta3','Testin!3'))
    #print(Communicator.REMOTE_LOGS)

    # Threading
    QtCore.QThread.currentThread().setObjectName("MAIN")
    thread = QtCore.QThread()
    thread.name = "auto_refresh"
    worker = Worker()
    worker.moveToThread(thread)
    worker.start()
    worker.refresh_signal.connect(Communicator.update_channel)
    


    def __init__(self):
        super(Handler,self).__init__()
        com=Ui_hbsCommunicator()
        com.setupUi(self)
        Handler.USERNAME_ENTRY = com.usernameEntry
        Handler.PASSWORD_ENTRY = com.passwordEntry
        GUI.CHANNEL_DISPLAY = com.channelDisplay
        GUI.CHAT_ENTRY = com.chatEntry
        GUI.SUBMIT_BTN = com.submitButton
        GUI.ROSTER_DISPLAY = com.rosterDisplay
        GUI.LOGIN_STATUS_LABEL = com.loginStatusLabel
        GUI.USER_BTN = com.userButton
        GUI.REFRESH_BUTTON = com.refreshButton        
        GUI.CHANNEL_NOTEBOOK = com.channelNotebook
        GUI.CONTENT_NOTEBOOK = com.contentNotebook
        GUI.ANNOUNCEMENT_LABEL = com.announcementLabel
        GUI.LOGIN_GROUP_BOX = com.loginGroupBox
        
        # Disabled the Roster tab. 
        # Move this line into ui_communicator.py either manually or
        # through QTDesigner somehow. Qt Designer does not appear
        # to allow me to disable individual tabs in a notebook,
        # only the notebook as a while.
        GUI.CONTENT_NOTEBOOK.setTabEnabled(1, False)

        self.setWindowIcon(QtGui.QIcon('Com-Headset.png'))
        
        self.show()

    def on_loginButton_pressed(self, *args):
        username = Handler.USERNAME_ENTRY.text()
        password = Handler.PASSWORD_ENTRY.text()
        remember = Handler.REMEMBER_LOGIN #.checkState()
        Communicator.login(username,password,remember)

    def on_submitButton_clicked(self, *args):
        Communicator.write_chat_to_channel()

    def on_chatEntry_returnPressed(self, *args):
        Handler.on_submitButton_clicked(self, *args)

    def on_passwordEntry_returnPressed(self, *args):
        Handler.on_loginButton_pressed(self, *args)

    def on_usernameEntry_activate(self, *args):
        Handler.on_loginButton_pressed(self, *args)

    def on_rememberLoginCheck_stateChanged(self, *args):
        flag = args
        if flag[0] == 0:
            Handler.REMEMBER_LOGIN = 'False'
        else:
            Handler.REMEMBER_LOGIN = 'True'

    # Command Communication Channels
    
    def on_centralCommandButton_clicked(self, *args):
        if Communicator.check_user_permissions("Central Command"):
            log_path = Config.LOG_PATHS['Central Command Log']
            roster_path = Config.ROSTER_PATHS['Central Command Roster']
            Communicator.populate_channel(log_path,roster_path)

        else: 
            Communicator.invalid_permissions()

    def on_operationsCommandButton_clicked(self, *args):
        if Communicator.check_user_permissions("Operations Command"):
            log_path = Config.LOG_PATHS['Operations Command Log']
            roster_path = Config.ROSTER_PATHS['Operations Command Roster']
            Communicator.populate_channel(log_path,roster_path)
        else: 
            Communicator.invalid_permissions()
   
    def on_codCommandButton_clicked(self, *args):
        if Communicator.check_user_permissions("Call of Duty Command"):
            log_path = Config.LOG_PATHS['Call of Duty Command Log']
            roster_path = Config.ROSTER_PATHS['Call of Duty Command Roster']
            Communicator.populate_channel(log_path,roster_path)
        else: 
            Communicator.invalid_permissions()
 
    def on_tfCommandButton_clicked(self, *args):
        if Communicator.check_user_permissions("Titan Fall Command"):
            log_path = Config.LOG_PATHS['Titanfall Command Log']
            roster_path = Config.ROSTER_PATHS['Titanfall Command Roster']
            Communicator.populate_channel(log_path,roster_path)
        else: 
            Communicator.invalid_permissions()
    
    def on_lolCommandButton_clicked(self, *args):
        if Communicator.check_user_permissions("League of Legends Command"):
            log_path = Config.LOG_PATHS['League of Legends Command Log']
            roster_path = Config.ROSTER_PATHS['League of Legends Command Roster']
            Communicator.populate_channel(log_path,roster_path)
        else: 
            Communicator.invalid_permissions()

    def on_gwCommandButton_clicked(self, *args):
        if Communicator.check_user_permissions("Guild Wars Command"):
            log_path = Config.LOG_PATHS['Guild Wars Command Log']
            roster_path = Config.ROSTER_PATHS['Guild Wars Command Roster']
            Communicator.populate_channel(log_path,roster_path)
        else: 
            Communicator.invalid_permissions()
    
    def on_wowCommandButton_clicked(self, *args):
        if Communicator.check_user_permissions("World of Warcraft Command"):
            log_path = Config.LOG_PATHS['World of Warcraft Command Log']
            roster_path = Config.ROSTER_PATHS['World of Warcraft Command Roster']
            Communicator.populate_channel(log_path,roster_path)
        else: 
            Communicator.invalid_permissions()
    
    def on_mcCommandButton_clicked(self, *args):
        if Communicator.check_user_permissions("Minecraft Command"):
            log_path = Config.LOG_PATHS['Minecraft Command Log']
            roster_path = Config.ROSTER_PATHS['Minecraft Command Roster']
            
            Communicator.populate_channel(log_path,roster_path)
        else: 
            Communicator.invalid_permissions()
    
    def on_dayzCommandButton_clicked(self, *args):
        if Communicator.check_user_permissions("DayZ Command"):
            log_path = Config.LOG_PATHS['DayZ Command Log']
            roster_path = Config.ROSTER_PATHS['DayZ Command Roster']
            Communicator.populate_channel(log_path,roster_path)
        else: 
            Communicator.invalid_permissions()
    
    def on_logisticsCommandButton_clicked(self, *args):
        if Communicator.check_user_permissions("Logistics Command"):
            log_path = Config.LOG_PATHS['Logistics Command Log']
            roster_path = Config.ROSTER_PATHS['Logistics Command Roster']
            Communicator.populate_channel(log_path,roster_path)
        else: 
            Communicator.invalid_permissions()
    
    def on_mpCommandButton_clicked(self, *args):
        if Communicator.check_user_permissions("Military Police"):
            log_path = Config.LOG_PATHS['Military Police Command Log']
            roster_path = Config.ROSTER_PATHS['Military Police Command Roster']
            Communicator.populate_channel(log_path,roster_path)
        else: 
            Communicator.invalid_permissions()
    
    def on_admissionsCommandButton_clicked(self, *args):
        if Communicator.check_user_permissions("Admissions"):
            log_path = Config.LOG_PATHS['Admissions Command Log']
            roster_path = Config.ROSTER_PATHS['Admissions Command Roster']
            Communicator.populate_channel(log_path,roster_path)
        else: 
            Communicator.invalid_permissions()
   
    def on_betaTestButton_clicked(self, *args):
        log_path = Config.LOG_PATHS['Beta Test Command Log']
        roster_path = Config.ROSTER_PATHS['Beta Test Command Roster']
        Communicator.populate_channel(log_path,roster_path)
    
    # General Communicator Channels
    
    def on_generalButton_clicked(self, *args):
        log_path = Config.LOG_PATHS['General Log']
        roster_path = Config.ROSTER_PATHS['General Roster']
        Communicator.populate_channel(log_path,roster_path)

    def on_codGeneralButton_clicked(self, *args):
        log_path = Config.LOG_PATHS['Call of Duty Log']
        roster_path = Config.ROSTER_PATHS['Call of Duty Roster']
        Communicator.populate_channel(log_path,roster_path)

    def on_tfGeneralButton_clicked(self, *args):
        log_path = Config.LOG_PATHS['Titanfall Log']
        roster_path = Config.ROSTER_PATHS['Titanfall Roster']
        Communicator.populate_channel(log_path,roster_path)

    def on_lolGeneralButton_clicked(self, *args):
        log_path = Config.LOG_PATHS['League of Legends Log']
        roster_path = Config.ROSTER_PATHS['League of Legends Roster']
        Communicator.populate_channel(log_path,roster_path)

    def on_gwGeneralButton_clicked(self, *args):
        log_path = Config.LOG_PATHS['Guild Wars Log']
        roster_path = Config.ROSTER_PATHS['Guild Wars Roster']
        Communicator.populate_channel(log_path,roster_path)

    def on_wowGeneralButton_clicked(self, *args):
        log_path = Config.LOG_PATHS['World of Warcraft Log']
        roster_path = Config.ROSTER_PATHS['World of Warcraft Roster']
        Communicator.populate_channel(log_path,roster_path)

    def on_mcGeneralButton_clicked(self, *args):
        log_path = Config.LOG_PATHS['Minecraft Log']
        roster_path = Config.ROSTER_PATHS['Minecraft Roster']
        Communicator.populate_channel(log_path,roster_path)

    def on_dayzGeneralButton_clicked(self, *args):
        log_path = Config.LOG_PATHS['DayZ Log']
        roster_path = Config.ROSTER_PATHS['DayZ Roster']
        Communicator.populate_channel(log_path,roster_path)

    def on_socialMediaButton_clicked(self, *args):
        log_path = Config.LOG_PATHS['Social Media Log']
        roster_path = Config.ROSTER_PATHS['Social Media Roster']
        Communicator.populate_channel(log_path,roster_path)
