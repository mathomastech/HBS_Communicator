import sys
from PyQt4 import QtGui
from gui import Ui_hbsCommunicator
from communicator import *
from handler import *

class Editor(QtGui.QMainWindow):
    def __init__(self):
        super(Editor, self).__init__()
        self.ui=Ui_hbsCommunicator()
        self.ui.setupUi(self)
        self.ui.centralCommandButton.clicked.connect(self.on_channel_clicked)
        self.show()

    def on_channel_clicked(self):
        sender = self.sender()
        print(sender.text())

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Editor()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
