# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginWindow.ui'
#
# Created: Tue Mar 25 19:31:37 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_loginWindow(object):
    def setupUi(self, loginWindow):
        loginWindow.setObjectName(_fromUtf8("loginWindow"))
        loginWindow.resize(400, 300)
        self.gridLayoutWidget = QtGui.QWidget(loginWindow)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(19, 39, 361, 141))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.usernameLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.usernameLabel.setObjectName(_fromUtf8("usernameLabel"))
        self.gridLayout.addWidget(self.usernameLabel, 0, 0, 1, 1)
        self.passwordLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.passwordLabel.setObjectName(_fromUtf8("passwordLabel"))
        self.gridLayout.addWidget(self.passwordLabel, 1, 0, 1, 1)
        self.usernameEntry = QtGui.QLineEdit(self.gridLayoutWidget)
        self.usernameEntry.setObjectName(_fromUtf8("usernameEntry"))
        self.gridLayout.addWidget(self.usernameEntry, 0, 1, 1, 1)
        self.passwordEntry = QtGui.QLineEdit(self.gridLayoutWidget)
        self.passwordEntry.setObjectName(_fromUtf8("passwordEntry"))
        self.gridLayout.addWidget(self.passwordEntry, 1, 1, 1, 1)
        self.loginButton = QtGui.QPushButton(loginWindow)
        self.loginButton.setGeometry(QtCore.QRect(270, 220, 97, 31))
        self.loginButton.setObjectName(_fromUtf8("loginButton"))
        self.loginStatusLabel = QtGui.QLabel(loginWindow)
        self.loginStatusLabel.setGeometry(QtCore.QRect(40, 220, 65, 21))
        self.loginStatusLabel.setText(_fromUtf8(""))
        self.loginStatusLabel.setObjectName(_fromUtf8("loginStatusLabel"))

        self.retranslateUi(loginWindow)
        QtCore.QMetaObject.connectSlotsByName(loginWindow)

    def retranslateUi(self, loginWindow):
        loginWindow.setWindowTitle(_translate("loginWindow", "Dialog", None))
        self.usernameLabel.setText(_translate("loginWindow", "Username:", None))
        self.passwordLabel.setText(_translate("loginWindow", "Password:", None))
        self.loginButton.setText(_translate("loginWindow", "Login", None))

