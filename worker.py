import time
from PyQt4 import QtCore
from communicator import Communicator

class Worker(QtCore.QThread):
    refresh_signal = QtCore.pyqtSignal()
    
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self)

    def refresh(self):
        # Send signal to refresh the chat logs.
        self.refresh_signal.emit()

    def run (self):
        while True:
            if(Communicator.ACTIVE_LOG_PATH != "" and
                Communicator.ACTIVE_LOG_PATH != "logs/welcomeMessage.txt"):
                self.refresh()
            time.sleep(1)
        return

    #def __del__(self):
    #    self.wait()

