import time
from PyQt4 import QtCore
from communicator import Communicator
from ssh import SSH
from gui import GUI

'''
class Worker(QtCore.Qthread, index):
    refresh_signal = QtCore.pyqtSignal()
    channel_notification = QtCore.pyqtSignal()

    def run(self, index):
        white True:
            if(Communicator.ACTIVE_LOG_PATH != "" and
                Communicator.ACTIVE_LOG_PATH != "logs/welcomeMessage.txt"):
                self.update_all_channels(index)

    def update_all_channels(self):
        Communicator.DELTA = SSH.get_all_logs(Communicator.SSH_CONNECTION, Communicator.USER, index)
        #if Communicator.DELTA:
        self.channel_notification.emit()
        self.refresh(index)

    def refresh(self, index):
        if Communicator.ACTIVE_CHANNEL == GUI.CHANNELS[index][CHANNEL_NAME]:
            self.refresh_signal.emit()
'''  
class Worker(QtCore.QThread):
    refresh_signal = QtCore.pyqtSignal()
    channel_notification = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self)

    def refresh(self):
        # Send signal to refresh the chat logs.
        for i in range(0,len(GUI.CHANNELS)):
            if (Communicator.ACTIVE_CHANNEL == GUI.CHANNELS[i][GUI.CHANNEL_NAME]):
                for i in range(0,len(Communicator.DELTA)):
                    if Communicator.DELTA[i] == Communicator.ACTIVE_CHANNEL:
                        self.refresh_signal.emit()

    def update_all_channels(self):
        Communicator.DELTA = SSH.get_all_logs(Communicator.SSH_CONNECTION, Communicator.USER)
        if Communicator.DELTA:
            self.channel_notification.emit()
            self.refresh()
        return

    def run (self):
        while True:
            if(Communicator.ACTIVE_LOG_PATH != "" and
                Communicator.ACTIVE_LOG_PATH != "logs/welcomeMessage.txt"):
                self.update_all_channels()
        return

   # def __del__(self):
   #     self.wait()

