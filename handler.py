import sys, time, os.path, functools
from PyQt4 import QtGui, QtCore
from ui_communicator import Ui_hbsCommunicator
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
        self.worker.update_online_list.connect(self.online_list)
        self.worker.channels_received.connect(self.generate_channels)
    
        self.com=Ui_hbsCommunicator()
        self.com.setupUi(self)
        self.USERNAME_ENTRY = self.com.usernameEntry
        self.PASSWORD_ENTRY = self.com.passwordEntry
       
        #channels = generate_channels(self.com)
        #channels.button_map.connect(self.channel_clicked)

        self.connect_elements()
        #self.connect_channels()
        #self.generate_channels()

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
   
    def channel_clicked(self,channel,flag):
        Communicator.switch_channel(channel)
    
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
        GUI.CHANNEL_TAB = self.com.channelNotebook
        # Disabled the Roster tab. 
        # Move this line into ui_communicator.py either manually or
        # through QTDesigner somehow. Qt Designer does not appear
        # to allow me to disable individual tabs in a notebook,
        # only the notebook as a while.
        GUI.USERNAME_ENTRY.setFocus()
        GUI.CONTENT_NOTEBOOK.setTabEnabled(1, False)
        GUI.ONLINE_LAYOUT = self.com.onlineLayout

    def on_chatEntry_returnPressed(self, *args):
        self.on_submitButton_clicked(self, *args)
    
    def generate_channels(self):
        for i in range(0,len(Communicator.CHANNEL_LIST)):
            GUI.generate_channel_info(Communicator.CHANNEL_LIST[i][0],
                                        Communicator.CHANNEL_LIST[i][1],
                                        Communicator.CHANNEL_LIST[i][2],
                                        Communicator.CHANNEL_LIST[i][3]
                                     )

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GUI.CHANNEL_DISPLAY.sizePolicy().hasHeightForWidth())
        
        for i in range(0,len(GUI.CHANNELS)):
            self.button = QtGui.QPushButton(GUI.CHANNELS[i][GUI.CHANNEL_NAME])
            self.button.clicked.connect(functools.partial(self.channel_clicked,GUI.CHANNELS[i][GUI.CHANNEL_NAME]))
            GUI.CHANNELS[i][GUI.GUI_ELEMENT] = self.button
            self.button.setFlat(True)
            self.button.setSizePolicy(sizePolicy)
            self.button.setAutoDefault(True)
            if GUI.CHANNELS[i][GUI.CHANNEL_GROUP] == "command":
                self.com.commandLayout.addWidget(self.button)
            elif GUI.CHANNELS[i][GUI.CHANNEL_GROUP] == "general": 
                 self.com.generalLayout.addWidget(self.button)

    def on_loginButton_pressed(self, *args):
        username = self.USERNAME_ENTRY.text()
        password = self.PASSWORD_ENTRY.text()
        Communicator.login(username,password)
    
    def on_passwordEntry_returnPressed(self, *args):
        self.on_loginButton_pressed(self, *args)
    
    def on_rememberLoginCheck_stateChanged(self, *args):
        self.flag = args
        if self.flag[0] == 0:
            Communicator.REMEMBER_LOGIN = False
        else:
            Communicator.REMEMBER_LOGIN = True
    
    def on_submitButton_clicked(self, *args):
        Communicator.write_chat_to_channel()
    
    def online_list(self):
        # Get a list of all currently logged in users
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GUI.CHANNEL_DISPLAY.sizePolicy().hasHeightForWidth())
   
        print(GUI.ONLINE_USERS)
        for i in range(0,len(GUI.ONLINE_USERS)):
            GUI.ONLINE_USERS[0].setVisible(False)
            GUI.ONLINE_LAYOUT.removeWidget(GUI.ONLINE_USERS[0])
            GUI.ONLINE_USERS.pop(0)

        for i in range(0,len(Communicator.ONLINE_USERS)):
            self.button = QtGui.QPushButton(Communicator.ONLINE_USERS[i])
            self.button.clicked.connect(functools.partial(self.channel_clicked,Communicator.ONLINE_USERS[i]))
            self.button.setSizePolicy(sizePolicy)
            self.button.setAutoDefault(True)
            self.button.setEnabled(False)
            GUI.ONLINE_USERS.append(self.button)
            GUI.ONLINE_LAYOUT.addWidget(self.button)

    def on_usernameEntry_returnPressed(self, *args):
        self.on_loginButton_pressed(self, *args)


