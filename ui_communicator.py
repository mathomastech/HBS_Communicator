# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'communicatorui.ui'
#
# Created: Fri Mar 28 14:58:05 2014
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_hbsCommunicator(object):
    def setupUi(self, hbsCommunicator):
        hbsCommunicator.setObjectName(_fromUtf8("hbsCommunicator"))
        hbsCommunicator.resize(777, 604)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(hbsCommunicator.sizePolicy().hasHeightForWidth())
        hbsCommunicator.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(hbsCommunicator)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.formLayout = QtGui.QFormLayout(self.centralwidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.userLabel = QtGui.QLabel(self.centralwidget)
        self.userLabel.setObjectName(_fromUtf8("userLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.userLabel)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.chatEntry = QtGui.QLineEdit(self.centralwidget)
        self.chatEntry.setAutoFillBackground(True)
        self.chatEntry.setObjectName(_fromUtf8("chatEntry"))
        self.horizontalLayout_3.addWidget(self.chatEntry)
        self.submitButton = QtGui.QPushButton(self.centralwidget)
        self.submitButton.setObjectName(_fromUtf8("submitButton"))
        self.horizontalLayout_3.addWidget(self.submitButton)
        self.formLayout.setLayout(3, QtGui.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.contentNotebook = QtGui.QTabWidget(self.centralwidget)
        self.contentNotebook.setEnabled(True)
        self.contentNotebook.setObjectName(_fromUtf8("contentNotebook"))
        self.channelTab = QtGui.QWidget()
        self.channelTab.setObjectName(_fromUtf8("channelTab"))
        self.channelDisplay = QtGui.QPlainTextEdit(self.channelTab)
        self.channelDisplay.setGeometry(QtCore.QRect(-1, -1, 611, 421))
        self.channelDisplay.setReadOnly(True)
        self.channelDisplay.setObjectName(_fromUtf8("channelDisplay"))
        self.loginGroupBox = QtGui.QGroupBox(self.channelTab)
        self.loginGroupBox.setGeometry(QtCore.QRect(10, 10, 581, 351))
        self.loginGroupBox.setObjectName(_fromUtf8("loginGroupBox"))
        self.gridGroupBox = QtGui.QGroupBox(self.loginGroupBox)
        self.gridGroupBox.setGeometry(QtCore.QRect(70, 0, 461, 241))
        self.gridGroupBox.setObjectName(_fromUtf8("gridGroupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridGroupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.passwordLabel = QtGui.QLabel(self.gridGroupBox)
        self.passwordLabel.setObjectName(_fromUtf8("passwordLabel"))
        self.gridLayout_2.addWidget(self.passwordLabel, 1, 0, 1, 1)
        self.usernameEntry = QtGui.QLineEdit(self.gridGroupBox)
        self.usernameEntry.setEnabled(True)
        self.usernameEntry.setObjectName(_fromUtf8("usernameEntry"))
        self.gridLayout_2.addWidget(self.usernameEntry, 0, 1, 1, 1)
        self.passwordEntry = QtGui.QLineEdit(self.gridGroupBox)
        self.passwordEntry.setEnabled(True)
        self.passwordEntry.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordEntry.setObjectName(_fromUtf8("passwordEntry"))
        self.gridLayout_2.addWidget(self.passwordEntry, 1, 1, 1, 1)
        self.usernameLabel = QtGui.QLabel(self.gridGroupBox)
        self.usernameLabel.setObjectName(_fromUtf8("usernameLabel"))
        self.gridLayout_2.addWidget(self.usernameLabel, 0, 0, 1, 1)
        self.loginButton = QtGui.QPushButton(self.loginGroupBox)
        self.loginButton.setGeometry(QtCore.QRect(313, 261, 211, 31))
        self.loginButton.setObjectName(_fromUtf8("loginButton"))
        self.loginStatusLabel = QtGui.QLabel(self.loginGroupBox)
        self.loginStatusLabel.setGeometry(QtCore.QRect(40, 261, 261, 31))
        self.loginStatusLabel.setText(_fromUtf8(""))
        self.loginStatusLabel.setObjectName(_fromUtf8("loginStatusLabel"))
        self.contentNotebook.addTab(self.channelTab, _fromUtf8(""))
        self.rosterTab = QtGui.QWidget()
        self.rosterTab.setObjectName(_fromUtf8("rosterTab"))
        self.rosterDisplay = QtGui.QPlainTextEdit(self.rosterTab)
        self.rosterDisplay.setGeometry(QtCore.QRect(-1, -1, 611, 421))
        self.rosterDisplay.setReadOnly(True)
        self.rosterDisplay.setObjectName(_fromUtf8("rosterDisplay"))
        self.contentNotebook.addTab(self.rosterTab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.contentNotebook)
        self.formLayout.setLayout(2, QtGui.QFormLayout.FieldRole, self.verticalLayout)
        self.channelNotebook = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.channelNotebook.sizePolicy().hasHeightForWidth())
        self.channelNotebook.setSizePolicy(sizePolicy)
        self.channelNotebook.setTabPosition(QtGui.QTabWidget.North)
        self.channelNotebook.setTabShape(QtGui.QTabWidget.Rounded)
        self.channelNotebook.setElideMode(QtCore.Qt.ElideNone)
        self.channelNotebook.setTabsClosable(False)
        self.channelNotebook.setMovable(False)
        self.channelNotebook.setObjectName(_fromUtf8("channelNotebook"))
        self.commandTab = QtGui.QWidget()
        self.commandTab.setObjectName(_fromUtf8("commandTab"))
        self.gridLayout = QtGui.QGridLayout(self.commandTab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.centralCommandButton = QtGui.QPushButton(self.commandTab)
        self.centralCommandButton.setFlat(True)
        self.centralCommandButton.setObjectName(_fromUtf8("centralCommandButton"))
        self.verticalLayout_2.addWidget(self.centralCommandButton)
        self.operationsCommandButton = QtGui.QPushButton(self.commandTab)
        self.operationsCommandButton.setFlat(True)
        self.operationsCommandButton.setObjectName(_fromUtf8("operationsCommandButton"))
        self.verticalLayout_2.addWidget(self.operationsCommandButton)
        self.logisticsCommandButton = QtGui.QPushButton(self.commandTab)
        self.logisticsCommandButton.setFlat(True)
        self.logisticsCommandButton.setObjectName(_fromUtf8("logisticsCommandButton"))
        self.verticalLayout_2.addWidget(self.logisticsCommandButton)
        self.codCommandButton = QtGui.QPushButton(self.commandTab)
        self.codCommandButton.setFlat(True)
        self.codCommandButton.setObjectName(_fromUtf8("codCommandButton"))
        self.verticalLayout_2.addWidget(self.codCommandButton)
        self.tfCommandButton = QtGui.QPushButton(self.commandTab)
        self.tfCommandButton.setFlat(True)
        self.tfCommandButton.setObjectName(_fromUtf8("tfCommandButton"))
        self.verticalLayout_2.addWidget(self.tfCommandButton)
        self.gwCommandButton = QtGui.QPushButton(self.commandTab)
        self.gwCommandButton.setFlat(True)
        self.gwCommandButton.setObjectName(_fromUtf8("gwCommandButton"))
        self.verticalLayout_2.addWidget(self.gwCommandButton)
        self.wowCommandButton = QtGui.QPushButton(self.commandTab)
        self.wowCommandButton.setFlat(True)
        self.wowCommandButton.setObjectName(_fromUtf8("wowCommandButton"))
        self.verticalLayout_2.addWidget(self.wowCommandButton)
        self.csCommandButton = QtGui.QPushButton(self.commandTab)
        self.csCommandButton.setFlat(True)
        self.csCommandButton.setObjectName(_fromUtf8("csCommandButton"))
        self.verticalLayout_2.addWidget(self.csCommandButton)
        self.lolCommandButton = QtGui.QPushButton(self.commandTab)
        self.lolCommandButton.setFlat(True)
        self.lolCommandButton.setObjectName(_fromUtf8("lolCommandButton"))
        self.verticalLayout_2.addWidget(self.lolCommandButton)
        self.mcCommandButton = QtGui.QPushButton(self.commandTab)
        self.mcCommandButton.setFlat(True)
        self.mcCommandButton.setObjectName(_fromUtf8("mcCommandButton"))
        self.verticalLayout_2.addWidget(self.mcCommandButton)
        self.dayzCommandButton = QtGui.QPushButton(self.commandTab)
        self.dayzCommandButton.setFlat(True)
        self.dayzCommandButton.setObjectName(_fromUtf8("dayzCommandButton"))
        self.verticalLayout_2.addWidget(self.dayzCommandButton)
        self.rustCommandButton = QtGui.QPushButton(self.commandTab)
        self.rustCommandButton.setFlat(True)
        self.rustCommandButton.setObjectName(_fromUtf8("rustCommandButton"))
        self.verticalLayout_2.addWidget(self.rustCommandButton)
        self.mpCommandButton = QtGui.QPushButton(self.commandTab)
        self.mpCommandButton.setFlat(True)
        self.mpCommandButton.setObjectName(_fromUtf8("mpCommandButton"))
        self.verticalLayout_2.addWidget(self.mpCommandButton)
        self.admissionsCommandButton = QtGui.QPushButton(self.commandTab)
        self.admissionsCommandButton.setFlat(True)
        self.admissionsCommandButton.setObjectName(_fromUtf8("admissionsCommandButton"))
        self.verticalLayout_2.addWidget(self.admissionsCommandButton)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.channelNotebook.addTab(self.commandTab, _fromUtf8(""))
        self.generalTab = QtGui.QWidget()
        self.generalTab.setObjectName(_fromUtf8("generalTab"))
        self.layoutWidget_2 = QtGui.QWidget(self.generalTab)
        self.layoutWidget_2.setGeometry(QtCore.QRect(20, 10, 143, 366))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.generalButton = QtGui.QPushButton(self.layoutWidget_2)
        self.generalButton.setFlat(True)
        self.generalButton.setObjectName(_fromUtf8("generalButton"))
        self.verticalLayout_3.addWidget(self.generalButton)
        self.codGeneralButton = QtGui.QPushButton(self.layoutWidget_2)
        self.codGeneralButton.setFlat(True)
        self.codGeneralButton.setObjectName(_fromUtf8("codGeneralButton"))
        self.verticalLayout_3.addWidget(self.codGeneralButton)
        self.tfGeneralButton = QtGui.QPushButton(self.layoutWidget_2)
        self.tfGeneralButton.setFlat(True)
        self.tfGeneralButton.setObjectName(_fromUtf8("tfGeneralButton"))
        self.verticalLayout_3.addWidget(self.tfGeneralButton)
        self.wowGeneralButton = QtGui.QPushButton(self.layoutWidget_2)
        self.wowGeneralButton.setFlat(True)
        self.wowGeneralButton.setObjectName(_fromUtf8("wowGeneralButton"))
        self.verticalLayout_3.addWidget(self.wowGeneralButton)
        self.gwGeneralButton = QtGui.QPushButton(self.layoutWidget_2)
        self.gwGeneralButton.setFlat(True)
        self.gwGeneralButton.setObjectName(_fromUtf8("gwGeneralButton"))
        self.verticalLayout_3.addWidget(self.gwGeneralButton)
        self.csGeneralButton = QtGui.QPushButton(self.layoutWidget_2)
        self.csGeneralButton.setFlat(True)
        self.csGeneralButton.setObjectName(_fromUtf8("csGeneralButton"))
        self.verticalLayout_3.addWidget(self.csGeneralButton)
        self.lolGeneralButton = QtGui.QPushButton(self.layoutWidget_2)
        self.lolGeneralButton.setFlat(True)
        self.lolGeneralButton.setObjectName(_fromUtf8("lolGeneralButton"))
        self.verticalLayout_3.addWidget(self.lolGeneralButton)
        self.mcGeneralButton = QtGui.QPushButton(self.layoutWidget_2)
        self.mcGeneralButton.setFlat(True)
        self.mcGeneralButton.setObjectName(_fromUtf8("mcGeneralButton"))
        self.verticalLayout_3.addWidget(self.mcGeneralButton)
        self.rustGeneralButton = QtGui.QPushButton(self.layoutWidget_2)
        self.rustGeneralButton.setFlat(True)
        self.rustGeneralButton.setObjectName(_fromUtf8("rustGeneralButton"))
        self.verticalLayout_3.addWidget(self.rustGeneralButton)
        self.dayzGeneralButton = QtGui.QPushButton(self.layoutWidget_2)
        self.dayzGeneralButton.setFlat(True)
        self.dayzGeneralButton.setObjectName(_fromUtf8("dayzGeneralButton"))
        self.verticalLayout_3.addWidget(self.dayzGeneralButton)
        self.channelNotebook.addTab(self.generalTab, _fromUtf8(""))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.channelNotebook)
        hbsCommunicator.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(hbsCommunicator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 777, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        hbsCommunicator.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(hbsCommunicator)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        hbsCommunicator.setStatusBar(self.statusbar)

        self.retranslateUi(hbsCommunicator)
        self.contentNotebook.setCurrentIndex(0)
        self.channelNotebook.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(hbsCommunicator)

    def retranslateUi(self, hbsCommunicator):
        hbsCommunicator.setWindowTitle(_translate("hbsCommunicator", "MainWindow", None))
        self.userLabel.setText(_translate("hbsCommunicator", "User", None))
        self.submitButton.setText(_translate("hbsCommunicator", "Submit", None))
        self.passwordLabel.setText(_translate("hbsCommunicator", "Password:", None))
        self.usernameLabel.setText(_translate("hbsCommunicator", "Username:", None))
        self.loginButton.setText(_translate("hbsCommunicator", "Login", None))
        self.contentNotebook.setTabText(self.contentNotebook.indexOf(self.channelTab), _translate("hbsCommunicator", "Channel", None))
        self.contentNotebook.setTabText(self.contentNotebook.indexOf(self.rosterTab), _translate("hbsCommunicator", "Roster", None))
        self.centralCommandButton.setText(_translate("hbsCommunicator", "Central Command", None))
        self.operationsCommandButton.setText(_translate("hbsCommunicator", "Operations", None))
        self.logisticsCommandButton.setText(_translate("hbsCommunicator", "Logistics", None))
        self.codCommandButton.setText(_translate("hbsCommunicator", "Call of Duty", None))
        self.tfCommandButton.setText(_translate("hbsCommunicator", "Titan Fall", None))
        self.gwCommandButton.setText(_translate("hbsCommunicator", "Guild Wars", None))
        self.wowCommandButton.setText(_translate("hbsCommunicator", "World of Warcraft", None))
        self.csCommandButton.setText(_translate("hbsCommunicator", "Counter Strike", None))
        self.lolCommandButton.setText(_translate("hbsCommunicator", "League of Legends", None))
        self.mcCommandButton.setText(_translate("hbsCommunicator", "Minecraft", None))
        self.dayzCommandButton.setText(_translate("hbsCommunicator", "DayZ", None))
        self.rustCommandButton.setText(_translate("hbsCommunicator", "Rust", None))
        self.mpCommandButton.setText(_translate("hbsCommunicator", "Military Police", None))
        self.admissionsCommandButton.setText(_translate("hbsCommunicator", "Admissions", None))
        self.channelNotebook.setTabText(self.channelNotebook.indexOf(self.commandTab), _translate("hbsCommunicator", "Command", None))
        self.generalButton.setText(_translate("hbsCommunicator", "General", None))
        self.codGeneralButton.setText(_translate("hbsCommunicator", "Call of Duty", None))
        self.tfGeneralButton.setText(_translate("hbsCommunicator", "Titan Fall", None))
        self.wowGeneralButton.setText(_translate("hbsCommunicator", "World of Warcraft", None))
        self.gwGeneralButton.setText(_translate("hbsCommunicator", "Guild Wars", None))
        self.csGeneralButton.setText(_translate("hbsCommunicator", "Counter Strike", None))
        self.lolGeneralButton.setText(_translate("hbsCommunicator", "League of Legends", None))
        self.mcGeneralButton.setText(_translate("hbsCommunicator", "Minecraft", None))
        self.rustGeneralButton.setText(_translate("hbsCommunicator", "Rust", None))
        self.dayzGeneralButton.setText(_translate("hbsCommunicator", "DayZ", None))
        self.channelNotebook.setTabText(self.channelNotebook.indexOf(self.generalTab), _translate("hbsCommunicator", "General", None))

