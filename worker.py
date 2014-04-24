import time
from PyQt4 import QtCore
from communicator import Communicator
from ssh import SSH
from gui import GUI

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
                    if Communicator.DELTA[i][0] == Communicator.ACTIVE_CHANNEL:
                        self.refresh_signal.emit()
    def run (self):
        while True:
            if(Communicator.ACTIVE_LOG_PATH != "" and
                Communicator.ACTIVE_LOG_PATH != "logs/welcomeMessage.txt"):
                self.update_all_channels()
        return

    def update_all_channels(self):
        delta,users = (SSH.get_all_logs(Communicator.SSH_CONNECTION, Communicator.USER, 
                                  Communicator.TCP_HOST, Communicator.TCP_PORT,Communicator.ONLINE_USERS))
        if delta:
            Communicator.DELTA.append(delta)
            self.channel_notification.emit()
            self.refresh()
        if users != Communicator.ONLINE_USERS:
            Communicator.ONLINE_USERS = users
        print(Communicator.ONLINE_USERS)

        return
