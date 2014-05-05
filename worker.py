import time
from PyQt4 import QtCore
from communicator import Communicator
from ssh import SSH
from gui import GUI

class Worker(QtCore.QThread):
    refresh_signal = QtCore.pyqtSignal()
    channel_notification = QtCore.pyqtSignal()
    update_online_list = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self)

    def run (self):
        while True:
            if Communicator.USER:
                self.update_online_users()
                self.update_all_channels()
        return

    def update_all_channels(self):
        if(Communicator.ACTIVE_LOG_PATH and
            Communicator.ACTIVE_LOG_PATH != "logs/welcomeMessage.txt"):
            delta = SSH.get_all_logs(Communicator.USER, Communicator.TCP_HOST, Communicator.TCP_PORT)
            if delta:
                Communicator.DELTA.append(delta)
                self.channel_notification.emit()
                for i in range(0,len(delta)):
                    if delta[i] == Communicator.ACTIVE_CHANNEL:
                        self.refresh_signal.emit()
        return
    
    def update_online_users(self): 
        users = SSH.whos_online(Communicator.TCP_HOST, Communicator.TCP_PORT, Communicator.ONLINE_USERS, Communicator.USER)
        if users != Communicator.ONLINE_USERS:
            Communicator.ONLINE_USERS = users
            self.update_online_list.emit()
        return
