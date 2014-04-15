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
    channel_notification = QtCore.pyqtSignal()
    
    # Threading
    QtCore.QThread.currentThread().setObjectName("MAIN")
    thread = QtCore.QThread()
    thread.name = "auto_refresh"
    worker = Worker()
    worker.moveToThread(thread)
    worker.start()
    worker.refresh_signal.connect(Communicator.update_active_channel)
    worker.channel_notification.connect(Communicator.update_selected_channels)
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
   
    def switch_command_channel(channel):
        if Communicator.check_user_permissions(channel):
            log_path = Config.LOG_PATHS[channel]
            roster_path = Config.ROSTER_PATHS[channel]
            Communicator.populate_channel(log_path,roster_path)
        else: 
            Communicator.invalid_permissions()
    
    def switch_general_channel(channel):
        log_path = Config.LOG_PATHS[channel]
        roster_path = Config.ROSTER_PATHS[channel]
        Communicator.populate_channel(log_path,roster_path)
   
    def on_centralCommandButton_clicked(self, *args):
        channel = "Central Command"
        Handler.switch_command_channel(channel)

    def on_operationsCommandButton_clicked(self, *args):
        channel = "Operations Command"
        Handler.switch_command_channel(channel)
   
    def on_codCommandButton_clicked(self, *args):
        channel = "Call of Duty Command"
        Handler.switch_command_channel(channel)
 
    def on_tfCommandButton_clicked(self, *args):
        channel = "Titanfall Command"
        Handler.switch_command_channel(channel)
    
    def on_lolCommandButton_clicked(self, *args):
        channel = "League of Legends Command"
        Handler.switch_command_channel(channel)

    def on_gwCommandButton_clicked(self, *args):
        channel = "Guild Wars Command"
        Handler.switch_command_channel(channel)
    
    def on_wowCommandButton_clicked(self, *args):
        channel = "World of Warcraft Command"
        Handler.switch_command_channel(channel)
    
    def on_mcCommandButton_clicked(self, *args):
        channel = "Minecraft Command"
        Handler.switch_command_channel(channel)
    
    def on_dayzCommandButton_clicked(self, *args):
        channel = "DayZ Command"
        Handler.switch_command_channel(channel)
   
    def on_logisticsCommandButton_clicked(self, *args):
        channel = "Logistics Command"
        Handler.switch_command_channel(channel)
    
    def on_mpCommandButton_clicked(self, *args):
        channel = "Military Police"
        Handler.switch_command_channel(channel)
    
    def on_admissionsCommandButton_clicked(self, *args):
        channel = "Admissions"
        Handler.switch_command_channel(channel)
   
    def on_betaTestButton_clicked(self, *args):
        channel = "Beta Test"
        Handler.switch_general_channel(channel)
    
    # General Communicator Channels
    
    def on_generalButton_clicked(self, *args):
        channel = "General"
        Handler.switch_general_channel(channel)

    def on_codGeneralButton_clicked(self, *args):
        channel = "Call of Duty"
        Handler.switch_general_channel(channel)

    def on_tfGeneralButton_clicked(self, *args):
        channel = "Titanfall"
        Handler.switch_general_channel(channel)

    def on_lolGeneralButton_clicked(self, *args):
        channel = "League of Legends"
        Handler.switch_general_channel(channel)
    
    def on_gwGeneralButton_clicked(self, *args):
        channel = "Guild Wars"
        Handler.switch_general_channel(channel)

    def on_wowGeneralButton_clicked(self, *args):
        channel = "World of Warcraft"
        Handler.switch_general_channel(channel)

    def on_mcGeneralButton_clicked(self, *args):
        channel = "Minecraft"
        Handler.switch_general_channel(channel)

    def on_dayzGeneralButton_clicked(self, *args):
        channel = "DayZ"
        Handler.switch_general_channel(channel)

    def on_socialMediaButton_clicked(self, *args):
        channel = "Social Media"
        Handler.switch_general_channel(channel)
