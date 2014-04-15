import time
from PyQt4 import QtCore
from communicator import Communicator
from ssh import SSH

class Worker(QtCore.QThread):
    refresh_signal = QtCore.pyqtSignal()
    channel_notification = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self)

    def refresh(self):
        # Send signal to refresh the chat logs.   
        self.refresh_signal.emit()

    def update_all_channels(self):
        local_logs, remote_logs, Communicator.DELTA = SSH.get_all_logs(
                                        Communicator.SSH_CONNECTION,
                                        Communicator.LOCAL_LOGS,
                                        Communicator.REMOTE_LOGS)
        if Communicator.DELTA:
            self.channel_notification.emit()
            #print(delta)
        return

    def run (self):
        while True:
            if(Communicator.ACTIVE_LOG_PATH != "" and
                Communicator.ACTIVE_LOG_PATH != "logs/welcomeMessage.txt"):
                self.refresh()
                self.update_all_channels()
            time.sleep(5)
        return

   # def __del__(self):
   #     self.wait()

