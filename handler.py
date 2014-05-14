import sys, time, os.path, functools
from PyQt4 import QtGui, QtCore
#from ui_communicator import Ui_hbsCommunicator
from ui_communicator_windows import Ui_hbsCommunicator
from gui import GUI
from config import Config
from communicator import Communicator
from worker import Worker

class Handler(QtGui.QMainWindow):
    
    def __init__(self):
        super(Handler,self).__init__()
        
        self.USERNAME_ENTRY = ""
        self.PASSWORD_ENTRY = ""
    
        # Threading
        QtCore.QThread.currentThread().setObjectName("MAIN")
        self.thread = QtCore.QThread()
        self.thread.name = "auto_refresh"
   
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        self.worker.start()
        self.worker.refresh_signal.connect(Communicator.update_active_channel)
        self.worker.channel_notification.connect(Communicator.update_selected_channels)
        self.worker.update_online_list.connect(Communicator.online_list)
    
        self.com=Ui_hbsCommunicator()
        self.com.setupUi(self)
        self.USERNAME_ENTRY = self.com.usernameEntry
        self.PASSWORD_ENTRY = self.com.passwordEntry
       
        #channels = generate_channels(self.com)
        #channels.button_map.connect(self.channel_clicked)

        self.connect_elements()
        #self.connect_channels()
        self.generate_channels()

        if os.path.exists('credentials.txt'):
            f = open('credentials.txt', 'r')
            username = f.readline()
            password = f.readline()
            Communicator.REMEMBER_LOGIN = True
            GUI.REMEMBER_LOGIN_CHECK.setChecked(True)            
            GUI.USERNAME_ENTRY.setText(username)
            GUI.PASSWORD_ENTRY.setText(password) 
       
        # Set the application icon
        self.app_icon = QtGui.QIcon()
        self.app_icon.addFile('icons/comms16x16.ico', QtCore.QSize(16,16))
        self.app_icon.addFile('icons/comms24x24.ico', QtCore.QSize(24,24))
        self.app_icon.addFile('icons/comms32x32.ico', QtCore.QSize(32,32))
        self.app_icon.addFile('icons/comms48x48.ico', QtCore.QSize(48,48))
        self.app_icon.addFile('icons/comms256x256.ico', QtCore.QSize(256,256))
        
        self.setWindowIcon(self.app_icon)
        self.show()
   
    def generate_channels(self): 
        
        for i in range(0,len(GUI.CHANNELS)):
            self.button = QtGui.QPushButton(GUI.CHANNELS[i][GUI.CHANNEL_NAME])
            self.button.clicked.connect(functools.partial(self.channel_clicked,GUI.CHANNELS[i][GUI.CHANNEL_NAME]))
            GUI.CHANNELS[i][GUI.GUI_ELEMENT] = self.button
            self.button.setFlat(True)
            self.button.setAutoDefault(True)
            if GUI.CHANNELS[i][GUI.CHANNEL_GROUP] == "command":
                self.com.commandLayout.addWidget(self.button)
            elif GUI.CHANNELS[i][GUI.CHANNEL_GROUP] == "general": 
                self.com.generalLayout.addWidget(self.button)

    def channel_clicked(self,channel,flag):
        Communicator.switch_channel(channel)

    def on_loginButton_pressed(self, *args):
        username = self.USERNAME_ENTRY.text()
        password = self.PASSWORD_ENTRY.text()
        Communicator.login(username,password)

    def on_submitButton_clicked(self, *args):
        Communicator.write_chat_to_channel()

    def on_chatEntry_returnPressed(self, *args):
        self.on_submitButton_clicked(self, *args)

    def on_passwordEntry_returnPressed(self, *args):
        self.on_loginButton_pressed(self, *args)
    
    def on_usernameEntry_returnPressed(self, *args):
        self.on_loginButton_pressed(self, *args)

    #def on_usernameEntry_activate(self, *args):
    #    Handler.on_loginButton_pressed(self, *args)

    def on_rememberLoginCheck_stateChanged(self, *args):
        self.flag = args
        if self.flag[0] == 0:
            Communicator.REMEMBER_LOGIN = False
        else:
            Communicator.REMEMBER_LOGIN = True


    def connect_elements(self):
        GUI.CHANNEL_DISPLAY = self.com.channelDisplay
        GUI.CHAT_ENTRY = self.com.chatEntry
        GUI.SUBMIT_BTN = self.com.submitButton
        GUI.ROSTER_DISPLAY = self.com.rosterDisplay
        GUI.LOGIN_STATUS_LABEL = self.com.loginStatusLabel
        GUI.USER_BTN = self.com.userButton
        GUI.REFRESH_BUTTON = self.com.refreshButton        
        GUI.CHANNEL_NOTEBOOK = self.com.channelNotebook
        GUI.CONTENT_NOTEBOOK = self.com.contentNotebook
        GUI.ANNOUNCEMENT_LABEL = self.com.announcementLabel
        GUI.LOGIN_GROUP_BOX = self.com.loginGroupBox
        GUI.USERNAME_ENTRY = self.com.usernameEntry 
        GUI.PASSWORD_ENTRY = self.com.passwordEntry
        GUI.REMEMBER_LOGIN_CHECK = self.com.rememberLoginCheck
        GUI.ONLINE_LIST = self.com.onlineList
        GUI.CHANNEL_TAB = self.com.channelNotebook
        # Disabled the Roster tab. 
        # Move this line into ui_communicator.py either manually or
        # through QTDesigner somehow. Qt Designer does not appear
        # to allow me to disable individual tabs in a notebook,
        # only the notebook as a while.
        GUI.USERNAME_ENTRY.setFocus()
        GUI.CONTENT_NOTEBOOK.setTabEnabled(1, False)

    # =---------------------------------------------------------------------=#
    #    EVERYTHING FROM HERE DOWN IS BEING REPLACED BY generate_channels    #
    #                                                                        #

    def connect_channels(self):
        #This is being replace with generate_channels
        # Command Buttons        
        GUI.CHANNELS[0][GUI.GUI_ELEMENT] = self.com.centralCommandButton
        GUI.CHANNELS[1][GUI.GUI_ELEMENT] = self.com.operationsCommandButton
        GUI.CHANNELS[2][GUI.GUI_ELEMENT] = self.com.codCommandButton 
        GUI.CHANNELS[3][GUI.GUI_ELEMENT] = self.com.tfCommandButton
        GUI.CHANNELS[4][GUI.GUI_ELEMENT] = self.com.lolCommandButton
        GUI.CHANNELS[5][GUI.GUI_ELEMENT] = self.com.gwCommandButton
        GUI.CHANNELS[6][GUI.GUI_ELEMENT] = self.com.wowCommandButton
        GUI.CHANNELS[7][GUI.GUI_ELEMENT] = self.com.mcCommandButton
        GUI.CHANNELS[8][GUI.GUI_ELEMENT] = self.com.dayzCommandButton
        GUI.CHANNELS[9][GUI.GUI_ELEMENT] = self.com.logisticsCommandButton
        GUI.CHANNELS[10][GUI.GUI_ELEMENT] = self.com.mpCommandButton
        GUI.CHANNELS[11][GUI.GUI_ELEMENT] = self.com.admissionsCommandButton
        GUI.CHANNELS[12][GUI.GUI_ELEMENT] = self.com.betaTestButton
        
        # General Buttons
        GUI.CHANNELS[13][GUI.GUI_ELEMENT] = self.com.generalButton
        GUI.CHANNELS[14][GUI.GUI_ELEMENT] = self.com.codGeneralButton
        GUI.CHANNELS[15][GUI.GUI_ELEMENT] = self.com.tfGeneralButton
        GUI.CHANNELS[16][GUI.GUI_ELEMENT] = self.com.lolGeneralButton
        GUI.CHANNELS[17][GUI.GUI_ELEMENT] = self.com.gwGeneralButton
        GUI.CHANNELS[18][GUI.GUI_ELEMENT] = self.com.wowGeneralButton
        GUI.CHANNELS[19][GUI.GUI_ELEMENT] = self.com.mcGeneralButton
        GUI.CHANNELS[20][GUI.GUI_ELEMENT] = self.com.dayzGeneralButton
        GUI.CHANNELS[21][GUI.GUI_ELEMENT] = self.com.socialMediaButton
        GUI.CHANNELS[22][GUI.GUI_ELEMENT] = self.com.raffleButton
        GUI.CHANNELS[23][GUI.GUI_ELEMENT] = self.com.csCommandButton
        GUI.CHANNELS[24][GUI.GUI_ELEMENT] = self.com.csButton
        #GUI.CHANNELS[25][GUI.GUI_ELEMENT] = self.com.wsCommandButton
        #GUI.CHANNELS[26][GUI.GUI_ELEMENT] = self.com.wsButton
    # Command Communication Channels
             
    def on_centralCommandButton_clicked(self, *args):
        Communicator.switch_channel("Central Command")
        
    def on_operationsCommandButton_clicked(self, *args):
        Communicator.switch_channel("Operations Command")
   
    def on_codCommandButton_clicked(self, *args):
        Communicator.switch_channel("Call of Duty Command")
 
    def on_tfCommandButton_clicked(self, *args):
        Communicator.switch_channel("Titanfall Command")
    
    def on_lolCommandButton_clicked(self, *args):
        Communicator.switch_channel("League of Legends Command")

    def on_gwCommandButton_clicked(self, *args):
        Communicator.switch_channel("Guild Wars Command")
    
    def on_wowCommandButton_clicked(self, *args):
        Communicator.switch_channel("World of Warcraft Command")

    def on_tfGeneralButton_clicked(self, *args):
        Communicator.switch_channel("Titanfall")

    def on_lolGeneralButton_clicked(self, *args):
        Communicator.switch_channel("League of Legends")
    
    def on_mcCommandButton_clicked(self, *args):
        Communicator.switch_channel("Minecraft Command")
    
    def on_dayzCommandButton_clicked(self, *args):
        Communicator.switch_channel("DayZ Command")
    
    def on_csCommandButton_clicked(self, *args):
        Communicator.switch_channel("Counter Strike Command")
    
    def on_wsCommandButton_clicked(self, *args):
        Communicator.switch_channel("Wildstar Command")
   
    def on_logisticsCommandButton_clicked(self, *args):
        Communicator.switch_channel("Logistics Command")
    
    def on_mpCommandButton_clicked(self, *args):
        Communicator.switch_channel("Military Police")
    
    def on_admissionsCommandButton_clicked(self, *args):
        Communicator.switch_channel("Admissions")
   
    def on_betaTestButton_clicked(self, *args):
        Communicator.switch_channel("Beta Test")
    
    # General Communicator Channels
    
    def on_generalButton_clicked(self, *args):
        Communicator.switch_channel("General")
    
    def on_codGeneralButton_clicked(self, *args):
        Communicator.switch_channel("Call of Duty")

    def on_tfGeneralButton_clicked(self, *args):
        Communicator.switch_channel("Titanfall")

    def on_lolGeneralButton_clicked(self, *args):
        Communicator.switch_channel("League of Legends")
    
    def on_gwGeneralButton_clicked(self, *args):
        Communicator.switch_channel("Guild Wars")

    def on_wowGeneralButton_clicked(self, *args):
        Communicator.switch_channel("World of Warcraft")

    def on_mcGeneralButton_clicked(self, *args):
        Communicator.switch_channel("Minecraft")

    def on_dayzGeneralButton_clicked(self, *args):
        Communicator.switch_channel("DayZ")
    
    def on_csButton_clicked(self, *args):
        Communicator.switch_channel("Counter Strike")
    
    def on_wsButton_clicked(self, *args):
        Communicator.switch_channel("Wildstar")

    def on_socialMediaButton_clicked(self, *args):
        Communicator.switch_channel("Social Media")
    
    def on_raffleButton_clicked(self, *args):
        Communicator.switch_channel("Raffle")
   
'''
class generate_channels(QtGui.QMainWindow):
    button_map = QtCore.pyqtSignal()

    def __init__(self,com,parent=None):
        super(generate_channels,self).__init__(parent)
        signalMapper = QtCore.QSignalMapper()

        for i in range(0,len(GUI.CHANNELS)):
            button = QtGui.QPushButton(GUI.CHANNELS[i][GUI.CHANNEL_NAME])
            signalMapper.setMapping(button,GUI.CHANNELS[i][GUI.CHANNEL_NAME])
            button.clicked.connect(signalMapper.map)
                    
            if GUI.CHANNELS[i][GUI.CHANNEL_GROUP] == "command":
                com.commandLayout.addWidget(button)
            elif GUI.CHANNELS[i][GUI.CHANNEL_GROUP] == "general": 
                com.generalLayout.addWidget(button)

        signalMapper.mapped.connect(self.button_map)  
'''
