import sys, time, os.path
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
        GUI.USERNAME_ENTRY = com.usernameEntry 
        GUI.PASSWORD_ENTRY = com.passwordEntry
        GUI.REMEMBER_LOGIN_CHECK = com.rememberLoginCheck
        # Disabled the Roster tab. 
        # Move this line into ui_communicator.py either manually or
        # through QTDesigner somehow. Qt Designer does not appear
        # to allow me to disable individual tabs in a notebook,
        # only the notebook as a while.
        GUI.USERNAME_ENTRY.setFocus()
        GUI.CONTENT_NOTEBOOK.setTabEnabled(1, False)

        # Command Buttons        
        GUI.CHANNELS[0][3] = com.centralCommandButton
        GUI.CHANNELS[1][3] = com.operationsCommandButton
        GUI.CHANNELS[2][3] = com.codCommandButton 
        GUI.CHANNELS[3][3] = com.tfCommandButton
        GUI.CHANNELS[4][3] = com.lolCommandButton
        GUI.CHANNELS[5][3] = com.gwCommandButton
        GUI.CHANNELS[6][3] = com.wowCommandButton
        GUI.CHANNELS[7][3] = com.mcCommandButton
        GUI.CHANNELS[8][3] = com.dayzCommandButton
        GUI.CHANNELS[9][3] = com.logisticsCommandButton
        GUI.CHANNELS[10][3] = com.mpCommandButton
        GUI.CHANNELS[11][3] = com.admissionsCommandButton
        GUI.CHANNELS[12][3] = com.betaTestButton
        
        # General Buttons
        GUI.CHANNELS[13][3] = com.generalButton
        GUI.CHANNELS[14][3] = com.codGeneralButton
        GUI.CHANNELS[15][3] = com.tfGeneralButton
        GUI.CHANNELS[16][3] = com.lolGeneralButton
        GUI.CHANNELS[17][3] = com.gwGeneralButton
        GUI.CHANNELS[18][3] = com.wowGeneralButton
        GUI.CHANNELS[19][3] = com.mcGeneralButton
        GUI.CHANNELS[20][3] = com.dayzGeneralButton
        GUI.CHANNELS[21][3] = com.socialMediaButton
    
        if os.path.exists('credentials.txt'):
            f = open('credentials.txt', 'r')
            username = f.readline()
            password = f.readline()
            Communicator.REMEMBER_LOGIN = True
            GUI.REMEMBER_LOGIN_CHECK.setChecked(True)            
            GUI.USERNAME_ENTRY.setText(username)
            GUI.PASSWORD_ENTRY.setText(password) 
        self.show()
    
    def on_loginButton_pressed(self, *args):
        username = Handler.USERNAME_ENTRY.text()
        password = Handler.PASSWORD_ENTRY.text()
        Communicator.login(username,password)

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
            Communicator.REMEMBER_LOGIN = False
        else:
            Communicator.REMEMBER_LOGIN = True

    # Command Communication Channels
                    
    def on_centralCommandButton_clicked(self, *args):
        Communicator.switch_command_channel("Central Command")
        
    def on_operationsCommandButton_clicked(self, *args):
        Communicator.switch_command_channel("Operations Command")
   
    def on_codCommandButton_clicked(self, *args):
        Communicator.switch_command_channel("Call of Duty Command")
 
    def on_tfCommandButton_clicked(self, *args):
        Communicator.switch_command_channel("Titanfall Command")
    
    def on_lolCommandButton_clicked(self, *args):
        Communicator.switch_command_channel("League of Legends Command")

    def on_gwCommandButton_clicked(self, *args):
        Communicator.switch_command_channel("Guild Wars Command")
    
    def on_wowCommandButton_clicked(self, *args):
        Communicator.switch_command_channel("World of Warcraft Command")

    def on_tfGeneralButton_clicked(self, *args):
        Communicator.switch_general_channel("Titanfall")

    def on_lolGeneralButton_clicked(self, *args):
        Communicator.switch_general_channel("League of Legends")
    
    def on_mcCommandButton_clicked(self, *args):
        Communicator.switch_command_channel("Minecraft Command")
    
    def on_dayzCommandButton_clicked(self, *args):
        Communicator.switch_command_channel("DayZ Command")
   
    def on_logisticsCommandButton_clicked(self, *args):
        Communicator.switch_command_channel("Logistics Command")
    
    def on_mpCommandButton_clicked(self, *args):
        Communicator.switch_command_channel("Military Police")
    
    def on_admissionsCommandButton_clicked(self, *args):
        Communicator.switch_command_channel("Admissions")
   
    def on_betaTestButton_clicked(self, *args):
        Communicator.switch_general_channel("Beta Test")
    
    # General Communicator Channels
    
    def on_generalButton_clicked(self, *args):
        Communicator.switch_general_channel("General")

    def on_codGeneralButton_clicked(self, *args):
        Communicator.switch_general_channel("Call of Duty")

    def on_tfGeneralButton_clicked(self, *args):
        Communicator.switch_general_channel("Titanfall")

    def on_lolGeneralButton_clicked(self, *args):
        Communicator.switch_general_channel("League of Legends")
    
    def on_gwGeneralButton_clicked(self, *args):
        Communicator.switch_general_channel("Guild Wars")

    def on_wowGeneralButton_clicked(self, *args):
        Communicator.switch_general_channel("World of Warcraft")

    def on_mcGeneralButton_clicked(self, *args):
        Communicator.switch_general_channel("Minecraft")

    def on_dayzGeneralButton_clicked(self, *args):
        Communicator.switch_general_channel("DayZ")

    def on_socialMediaButton_clicked(self, *args):
        Communicator.switch_general_channel("Social Media")
