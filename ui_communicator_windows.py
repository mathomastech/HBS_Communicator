# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_communicator_windows.ui'
#
# Created: Tue Apr 15 19:21:24 2014
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
        hbsCommunicator.setEnabled(True)
        hbsCommunicator.resize(788, 597)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(hbsCommunicator.sizePolicy().hasHeightForWidth())
        hbsCommunicator.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(hbsCommunicator)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.formLayout = QtGui.QFormLayout(self.centralwidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.contentNotebook = QtGui.QTabWidget(self.centralwidget)
        self.contentNotebook.setEnabled(True)
        self.contentNotebook.setTabsClosable(False)
        self.contentNotebook.setObjectName(_fromUtf8("contentNotebook"))
        self.channelTab = QtGui.QWidget()
        self.channelTab.setObjectName(_fromUtf8("channelTab"))
        self.channelDisplay = QtGui.QPlainTextEdit(self.channelTab)
        self.channelDisplay.setGeometry(QtCore.QRect(-1, -1, 622, 401))
        self.channelDisplay.setAcceptDrops(False)
        self.channelDisplay.setAutoFillBackground(False)
        self.channelDisplay.setFrameShadow(QtGui.QFrame.Sunken)
        self.channelDisplay.setReadOnly(True)
        self.channelDisplay.setCenterOnScroll(False)
        self.channelDisplay.setObjectName(_fromUtf8("channelDisplay"))
        self.loginGroupBox = QtGui.QGroupBox(self.channelTab)
        self.loginGroupBox.setGeometry(QtCore.QRect(-1, -1, 591, 391))
        self.loginGroupBox.setFlat(True)
        self.loginGroupBox.setObjectName(_fromUtf8("loginGroupBox"))
        self.gridGroupBox = QtGui.QGroupBox(self.loginGroupBox)
        self.gridGroupBox.setEnabled(True)
        self.gridGroupBox.setGeometry(QtCore.QRect(70, 0, 461, 261))
        self.gridGroupBox.setAutoFillBackground(False)
        self.gridGroupBox.setFlat(True)
        self.gridGroupBox.setObjectName(_fromUtf8("gridGroupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridGroupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.passwordLabel = QtGui.QLabel(self.gridGroupBox)
        self.passwordLabel.setObjectName(_fromUtf8("passwordLabel"))
        self.gridLayout_2.addWidget(self.passwordLabel, 1, 0, 1, 1)
        self.usernameEntry = QtGui.QLineEdit(self.gridGroupBox)
        self.usernameEntry.setEnabled(True)
        self.usernameEntry.setFocusPolicy(QtCore.Qt.StrongFocus)
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
        self.loginButton.setGeometry(QtCore.QRect(310, 295, 211, 31))
        self.loginButton.setAutoDefault(False)
        self.loginButton.setObjectName(_fromUtf8("loginButton"))
        self.loginStatusLabel = QtGui.QLabel(self.loginGroupBox)
        self.loginStatusLabel.setGeometry(QtCore.QRect(40, 295, 261, 31))
        self.loginStatusLabel.setObjectName(_fromUtf8("loginStatusLabel"))
        self.rememberLoginCheck = QtGui.QCheckBox(self.loginGroupBox)
        self.rememberLoginCheck.setEnabled(False)
        self.rememberLoginCheck.setGeometry(QtCore.QRect(373, 340, 141, 26))
        self.rememberLoginCheck.setObjectName(_fromUtf8("rememberLoginCheck"))
        self.contentNotebook.addTab(self.channelTab, _fromUtf8(""))
        self.rosterTab = QtGui.QWidget()
        self.rosterTab.setObjectName(_fromUtf8("rosterTab"))
        self.rosterDisplay = QtGui.QPlainTextEdit(self.rosterTab)
        self.rosterDisplay.setGeometry(QtCore.QRect(-1, -1, 621, 391))
        self.rosterDisplay.setReadOnly(True)
        self.rosterDisplay.setObjectName(_fromUtf8("rosterDisplay"))
        self.contentNotebook.addTab(self.rosterTab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.contentNotebook)
        self.formLayout.setLayout(2, QtGui.QFormLayout.FieldRole, self.verticalLayout)
        self.refreshButton = QtGui.QPushButton(self.centralwidget)
        self.refreshButton.setMaximumSize(QtCore.QSize(0, 0))
        self.refreshButton.setObjectName(_fromUtf8("refreshButton"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.refreshButton)
        self.submitLayout = QtGui.QHBoxLayout()
        self.submitLayout.setObjectName(_fromUtf8("submitLayout"))
        self.chatEntry = QtGui.QLineEdit(self.centralwidget)
        self.chatEntry.setEnabled(False)
        self.chatEntry.setAutoFillBackground(True)
        self.chatEntry.setObjectName(_fromUtf8("chatEntry"))
        self.submitLayout.addWidget(self.chatEntry)
        self.submitButton = QtGui.QPushButton(self.centralwidget)
        self.submitButton.setEnabled(False)
        self.submitButton.setObjectName(_fromUtf8("submitButton"))
        self.submitLayout.addWidget(self.submitButton)
        self.formLayout.setLayout(4, QtGui.QFormLayout.FieldRole, self.submitLayout)
        self.announcementLabel = QtGui.QLabel(self.centralwidget)
        self.announcementLabel.setAutoFillBackground(False)
        self.announcementLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.announcementLabel.setIndent(0)
        self.announcementLabel.setOpenExternalLinks(True)
        self.announcementLabel.setObjectName(_fromUtf8("announcementLabel"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.SpanningRole, self.announcementLabel)
        self.userButton = QtGui.QPushButton(self.centralwidget)
        self.userButton.setEnabled(False)
        self.userButton.setMinimumSize(QtCore.QSize(138, 28))
        self.userButton.setText(_fromUtf8(""))
        self.userButton.setFlat(True)
        self.userButton.setObjectName(_fromUtf8("userButton"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.userButton)
        self.channelNotebook = QtGui.QTabWidget(self.centralwidget)
        self.channelNotebook.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
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
        self.centralCommandButton.setAcceptDrops(False)
        self.centralCommandButton.setAutoDefault(True)
        self.centralCommandButton.setDefault(False)
        self.centralCommandButton.setFlat(True)
        self.centralCommandButton.setObjectName(_fromUtf8("centralCommandButton"))
        self.verticalLayout_2.addWidget(self.centralCommandButton)
        self.operationsCommandButton = QtGui.QPushButton(self.commandTab)
        self.operationsCommandButton.setAutoDefault(True)
        self.operationsCommandButton.setDefault(False)
        self.operationsCommandButton.setFlat(True)
        self.operationsCommandButton.setObjectName(_fromUtf8("operationsCommandButton"))
        self.verticalLayout_2.addWidget(self.operationsCommandButton)
        self.logisticsCommandButton = QtGui.QPushButton(self.commandTab)
        self.logisticsCommandButton.setAutoDefault(True)
        self.logisticsCommandButton.setFlat(True)
        self.logisticsCommandButton.setObjectName(_fromUtf8("logisticsCommandButton"))
        self.verticalLayout_2.addWidget(self.logisticsCommandButton)
        self.codCommandButton = QtGui.QPushButton(self.commandTab)
        self.codCommandButton.setAutoDefault(True)
        self.codCommandButton.setFlat(True)
        self.codCommandButton.setObjectName(_fromUtf8("codCommandButton"))
        self.verticalLayout_2.addWidget(self.codCommandButton)
        self.tfCommandButton = QtGui.QPushButton(self.commandTab)
        self.tfCommandButton.setAutoDefault(True)
        self.tfCommandButton.setFlat(True)
        self.tfCommandButton.setObjectName(_fromUtf8("tfCommandButton"))
        self.verticalLayout_2.addWidget(self.tfCommandButton)
        self.wowCommandButton = QtGui.QPushButton(self.commandTab)
        self.wowCommandButton.setAutoDefault(True)
        self.wowCommandButton.setFlat(True)
        self.wowCommandButton.setObjectName(_fromUtf8("wowCommandButton"))
        self.verticalLayout_2.addWidget(self.wowCommandButton)
        self.gwCommandButton = QtGui.QPushButton(self.commandTab)
        self.gwCommandButton.setAutoDefault(True)
        self.gwCommandButton.setFlat(True)
        self.gwCommandButton.setObjectName(_fromUtf8("gwCommandButton"))
        self.verticalLayout_2.addWidget(self.gwCommandButton)
        self.dayzCommandButton = QtGui.QPushButton(self.commandTab)
        self.dayzCommandButton.setAutoDefault(True)
        self.dayzCommandButton.setFlat(True)
        self.dayzCommandButton.setObjectName(_fromUtf8("dayzCommandButton"))
        self.verticalLayout_2.addWidget(self.dayzCommandButton)
        self.lolCommandButton = QtGui.QPushButton(self.commandTab)
        self.lolCommandButton.setAutoDefault(True)
        self.lolCommandButton.setFlat(True)
        self.lolCommandButton.setObjectName(_fromUtf8("lolCommandButton"))
        self.verticalLayout_2.addWidget(self.lolCommandButton)
        self.mcCommandButton = QtGui.QPushButton(self.commandTab)
        self.mcCommandButton.setAutoDefault(True)
        self.mcCommandButton.setFlat(True)
        self.mcCommandButton.setObjectName(_fromUtf8("mcCommandButton"))
        self.verticalLayout_2.addWidget(self.mcCommandButton)
        self.mpCommandButton = QtGui.QPushButton(self.commandTab)
        self.mpCommandButton.setAutoDefault(True)
        self.mpCommandButton.setFlat(True)
        self.mpCommandButton.setObjectName(_fromUtf8("mpCommandButton"))
        self.verticalLayout_2.addWidget(self.mpCommandButton)
        self.admissionsCommandButton = QtGui.QPushButton(self.commandTab)
        self.admissionsCommandButton.setAutoDefault(True)
        self.admissionsCommandButton.setFlat(True)
        self.admissionsCommandButton.setObjectName(_fromUtf8("admissionsCommandButton"))
        self.verticalLayout_2.addWidget(self.admissionsCommandButton)
        self.betaTestButton = QtGui.QPushButton(self.commandTab)
        self.betaTestButton.setAutoDefault(True)
        self.betaTestButton.setFlat(True)
        self.betaTestButton.setObjectName(_fromUtf8("betaTestButton"))
        self.verticalLayout_2.addWidget(self.betaTestButton)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.channelNotebook.addTab(self.commandTab, _fromUtf8(""))
        self.generalTab = QtGui.QWidget()
        self.generalTab.setObjectName(_fromUtf8("generalTab"))
        self.layoutWidget_2 = QtGui.QWidget(self.generalTab)
        self.layoutWidget_2.setGeometry(QtCore.QRect(-1, 6, 143, 381))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.generalButton = QtGui.QPushButton(self.layoutWidget_2)
        self.generalButton.setAutoDefault(True)
        self.generalButton.setFlat(True)
        self.generalButton.setObjectName(_fromUtf8("generalButton"))
        self.verticalLayout_3.addWidget(self.generalButton)
        self.codGeneralButton = QtGui.QPushButton(self.layoutWidget_2)
        self.codGeneralButton.setAutoDefault(True)
        self.codGeneralButton.setFlat(True)
        self.codGeneralButton.setObjectName(_fromUtf8("codGeneralButton"))
        self.verticalLayout_3.addWidget(self.codGeneralButton)
        self.tfGeneralButton = QtGui.QPushButton(self.layoutWidget_2)
        self.tfGeneralButton.setAutoDefault(True)
        self.tfGeneralButton.setFlat(True)
        self.tfGeneralButton.setObjectName(_fromUtf8("tfGeneralButton"))
        self.verticalLayout_3.addWidget(self.tfGeneralButton)
        self.wowGeneralButton = QtGui.QPushButton(self.layoutWidget_2)
        self.wowGeneralButton.setAutoDefault(True)
        self.wowGeneralButton.setFlat(True)
        self.wowGeneralButton.setObjectName(_fromUtf8("wowGeneralButton"))
        self.verticalLayout_3.addWidget(self.wowGeneralButton)
        self.gwGeneralButton = QtGui.QPushButton(self.layoutWidget_2)
        self.gwGeneralButton.setAutoDefault(True)
        self.gwGeneralButton.setFlat(True)
        self.gwGeneralButton.setObjectName(_fromUtf8("gwGeneralButton"))
        self.verticalLayout_3.addWidget(self.gwGeneralButton)
        self.dayzGeneralButton = QtGui.QPushButton(self.layoutWidget_2)
        self.dayzGeneralButton.setAutoDefault(True)
        self.dayzGeneralButton.setFlat(True)
        self.dayzGeneralButton.setObjectName(_fromUtf8("dayzGeneralButton"))
        self.verticalLayout_3.addWidget(self.dayzGeneralButton)
        self.lolGeneralButton = QtGui.QPushButton(self.layoutWidget_2)
        self.lolGeneralButton.setAutoDefault(True)
        self.lolGeneralButton.setFlat(True)
        self.lolGeneralButton.setObjectName(_fromUtf8("lolGeneralButton"))
        self.verticalLayout_3.addWidget(self.lolGeneralButton)
        self.mcGeneralButton = QtGui.QPushButton(self.layoutWidget_2)
        self.mcGeneralButton.setAutoDefault(True)
        self.mcGeneralButton.setFlat(True)
        self.mcGeneralButton.setObjectName(_fromUtf8("mcGeneralButton"))
        self.verticalLayout_3.addWidget(self.mcGeneralButton)
        self.socialMediaButton = QtGui.QPushButton(self.layoutWidget_2)
        self.socialMediaButton.setAutoDefault(True)
        self.socialMediaButton.setFlat(True)
        self.socialMediaButton.setObjectName(_fromUtf8("socialMediaButton"))
        self.verticalLayout_3.addWidget(self.socialMediaButton)
        self.channelNotebook.addTab(self.generalTab, _fromUtf8(""))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.channelNotebook)
        hbsCommunicator.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(hbsCommunicator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 788, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        hbsCommunicator.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(hbsCommunicator)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        hbsCommunicator.setStatusBar(self.statusbar)

        self.retranslateUi(hbsCommunicator)
        self.contentNotebook.setCurrentIndex(0)
        self.channelNotebook.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(hbsCommunicator)
        hbsCommunicator.setTabOrder(self.usernameEntry, self.passwordEntry)
        hbsCommunicator.setTabOrder(self.passwordEntry, self.loginButton)
        hbsCommunicator.setTabOrder(self.loginButton, self.channelNotebook)
        hbsCommunicator.setTabOrder(self.channelNotebook, self.centralCommandButton)
        hbsCommunicator.setTabOrder(self.centralCommandButton, self.operationsCommandButton)
        hbsCommunicator.setTabOrder(self.operationsCommandButton, self.logisticsCommandButton)
        hbsCommunicator.setTabOrder(self.logisticsCommandButton, self.codCommandButton)
        hbsCommunicator.setTabOrder(self.codCommandButton, self.tfCommandButton)
        hbsCommunicator.setTabOrder(self.tfCommandButton, self.wowCommandButton)
        hbsCommunicator.setTabOrder(self.wowCommandButton, self.gwCommandButton)
        hbsCommunicator.setTabOrder(self.gwCommandButton, self.dayzCommandButton)
        hbsCommunicator.setTabOrder(self.dayzCommandButton, self.lolCommandButton)
        hbsCommunicator.setTabOrder(self.lolCommandButton, self.mcCommandButton)
        hbsCommunicator.setTabOrder(self.mcCommandButton, self.mpCommandButton)
        hbsCommunicator.setTabOrder(self.mpCommandButton, self.admissionsCommandButton)
        hbsCommunicator.setTabOrder(self.admissionsCommandButton, self.betaTestButton)
        hbsCommunicator.setTabOrder(self.betaTestButton, self.chatEntry)
        hbsCommunicator.setTabOrder(self.chatEntry, self.submitButton)
        hbsCommunicator.setTabOrder(self.submitButton, self.contentNotebook)
        hbsCommunicator.setTabOrder(self.contentNotebook, self.refreshButton)
        hbsCommunicator.setTabOrder(self.refreshButton, self.rosterDisplay)
        hbsCommunicator.setTabOrder(self.rosterDisplay, self.userButton)
        hbsCommunicator.setTabOrder(self.userButton, self.generalButton)
        hbsCommunicator.setTabOrder(self.generalButton, self.codGeneralButton)
        hbsCommunicator.setTabOrder(self.codGeneralButton, self.tfGeneralButton)
        hbsCommunicator.setTabOrder(self.tfGeneralButton, self.wowGeneralButton)
        hbsCommunicator.setTabOrder(self.wowGeneralButton, self.gwGeneralButton)
        hbsCommunicator.setTabOrder(self.gwGeneralButton, self.dayzGeneralButton)
        hbsCommunicator.setTabOrder(self.dayzGeneralButton, self.lolGeneralButton)
        hbsCommunicator.setTabOrder(self.lolGeneralButton, self.channelDisplay)
        hbsCommunicator.setTabOrder(self.channelDisplay, self.mcGeneralButton)
        hbsCommunicator.setTabOrder(self.mcGeneralButton, self.socialMediaButton)

    def retranslateUi(self, hbsCommunicator):
        hbsCommunicator.setWindowTitle(_translate("hbsCommunicator", "HBS Communicator", None))
        self.passwordLabel.setText(_translate("hbsCommunicator", "Password:", None))
        self.usernameLabel.setText(_translate("hbsCommunicator", "Username:", None))
        self.loginButton.setText(_translate("hbsCommunicator", "Login", None))
        self.loginStatusLabel.setText(_translate("hbsCommunicator", "Hint: Same as forum", None))
        self.rememberLoginCheck.setText(_translate("hbsCommunicator", "Remember Login", None))
        self.contentNotebook.setTabText(self.contentNotebook.indexOf(self.channelTab), _translate("hbsCommunicator", "Channel", None))
        self.contentNotebook.setTabText(self.contentNotebook.indexOf(self.rosterTab), _translate("hbsCommunicator", "Roster", None))
        self.refreshButton.setText(_translate("hbsCommunicator", "Refresh", None))
        self.submitButton.setText(_translate("hbsCommunicator", "Submit", None))
        self.announcementLabel.setText(_translate("hbsCommunicator", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">HBS Communicator Version 0.6 - Beta</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Please report all bugs and features <a href=\"http://hellboundsoldiers.org/forums/forumdisplay.php?150-HBS-COMMUNICATOR\"><span style=\" text-decoration: underline; color:#0000ff;\">here</span></a></p></body></html>", None))
        self.centralCommandButton.setText(_translate("hbsCommunicator", "Central Command", None))
        self.operationsCommandButton.setText(_translate("hbsCommunicator", "Operations", None))
        self.logisticsCommandButton.setText(_translate("hbsCommunicator", "Logistics", None))
        self.codCommandButton.setText(_translate("hbsCommunicator", "Call of Duty", None))
        self.tfCommandButton.setText(_translate("hbsCommunicator", "Titanfall", None))
        self.wowCommandButton.setText(_translate("hbsCommunicator", "World of Warcraft", None))
        self.gwCommandButton.setText(_translate("hbsCommunicator", "Guild Wars", None))
        self.dayzCommandButton.setText(_translate("hbsCommunicator", "DayZ", None))
        self.lolCommandButton.setText(_translate("hbsCommunicator", "League of Legends", None))
        self.mcCommandButton.setText(_translate("hbsCommunicator", "Minecraft", None))
        self.mpCommandButton.setText(_translate("hbsCommunicator", "Military Police", None))
        self.admissionsCommandButton.setText(_translate("hbsCommunicator", "Admissions", None))
        self.betaTestButton.setText(_translate("hbsCommunicator", "Beta Testing", None))
        self.channelNotebook.setTabText(self.channelNotebook.indexOf(self.commandTab), _translate("hbsCommunicator", "Command", None))
        self.generalButton.setText(_translate("hbsCommunicator", "General", None))
        self.codGeneralButton.setText(_translate("hbsCommunicator", "Call of Duty", None))
        self.tfGeneralButton.setText(_translate("hbsCommunicator", "Titanfall", None))
        self.wowGeneralButton.setText(_translate("hbsCommunicator", "World of Warcraft", None))
        self.gwGeneralButton.setText(_translate("hbsCommunicator", "Guild Wars", None))
        self.dayzGeneralButton.setText(_translate("hbsCommunicator", "DayZ", None))
        self.lolGeneralButton.setText(_translate("hbsCommunicator", "League of Legends", None))
        self.mcGeneralButton.setText(_translate("hbsCommunicator", "Minecraft", None))
        self.socialMediaButton.setText(_translate("hbsCommunicator", "Social Media", None))
        self.channelNotebook.setTabText(self.channelNotebook.indexOf(self.generalTab), _translate("hbsCommunicator", "General", None))

