import time
from PyQt4 import QtCore
from communicator import Communicator

class Worker(QtCore.QThread):
    refresh = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self)

    def refresh(self):
        # Send signal to refresh the chat logs.
        print("Refresh")
        QtCore.QThread.emit(QtCore.SIGNAL('refresh'))

    def run (self):
        while True:
            if(Communicator.ACTIVE_LOG_PATH != "" and
                Communicator.ACTIVE_LOG_PATH != "logs/welcomeMessage.txt"):
                print(Communicator.ACTIVE_LOG_PATH)
                self.refresh()
            time.sleep(1)
        return

    #def __del__(self):
    #    self.wait()

