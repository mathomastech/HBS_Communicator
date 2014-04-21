from PyQt4 import QtGui
from config import Config
class GUI():
    CHANNEL_DISPLAY = ""
    ROSTER_DISPLAY = ""
    CHAT_ENTRY = ""
    SUBMIT_BTN = ""
    CHANNEL_NOTEBOOK = ""
    CONTENT_NOTEBOOK = ""
    USER_BTN = ""
    ANNOUNCEMENT_LABEL = ""
    LOGIN_GROUP_BOX = ""
    USERNAME_ENTRY = ""
    REMEMBER_LOGIN_CHECK = ""
    # Command Buttons
    CENTCOM = ""
    OP_CMD = ""
    COD_CMD = "" 
    TF_CMD = ""
    LOL_CMD = ""
    GW_CMD = ""
    WOW_CMD = ""
    MC_CMD = ""
    DAYZ_CMD = ""
    LOG_CMD = ""
    MP_CMD = ""
    ADM = ""
    BETA = ""
    
    # General Buttons
    GEN = ""
    COD = ""
    TF = ""
    LOL = ""
    GW = ""
    WOW = ""
    MC = ""
    DAYZ = ""
    SM = ""

    #Configurations
    LOGS = Config.LOGS
    LOG_PATH = Config.LOG_PATH
    ROSTER_PATH = Config.ROSTER_PATH
    WELCOME_LOG = LOG_PATH + "welcomeMessage.txt"
    
    #Index Indicators
    CHANNEL_NAME = 0
    SERVER_LOG_PATH = 1
    SERVER_ROSTER_PATH = 2
    GUI_ELEMENT = 3
    PERMISSIONS = 4
    STORED_LOG = 5
    LOCAL_LOG_PATH = 6
    
    CHANNELS = [
        ['Central Command',(LOG_PATH + 'centcomLog.txt'),(ROSTER_PATH + 'centcomRoster.txt'),(CENTCOM),[9,10],(""),(LOGS + 'centcomLog.txt')],
        ['Operations Command',(LOG_PATH + 'operationsCommandLog.txt'),(ROSTER_PATH + 'operationsCommandRoster.txt'),(OP_CMD),[9,10],(""),(LOGS + 'operationsCommandLog.txt')],
        ['Call of Duty Command',(LOG_PATH + 'codCommandLog.txt'),(ROSTER_PATH + 'codCommandRoster.txt'),(COD_CMD),[9,10,57],(""),(LOGS + 'codCommandLog.txt')],
        ['Titanfall Command',(LOG_PATH + 'tfCommandLog.txt'),(ROSTER_PATH + 'tfCommandRoster.txt'),(TF_CMD),[9,10,54],(""),(LOGS + 'tfCommandLog.txt')],
        ['League of Legends Command',(LOG_PATH + 'lolCommandLog.txt'),(ROSTER_PATH + 'lolCommandRoster.txt'),(LOL_CMD),[9,10,67],(""),(LOGS + 'lolCommandLog.txt')],
        ['Guild Wars Command',(LOG_PATH + 'gwCommandLog.txt'),(ROSTER_PATH + 'gwCommandRoster.txt'),(GW_CMD),[9,10,66],(""),(LOGS + 'gwCommandLog.txt')],
        ['World of Warcraft Command',(LOG_PATH + 'wowCommandLog.txt'),(ROSTER_PATH + 'wowCommandRoster.txt'),(WOW_CMD),[9,10,63],(""),(LOGS + 'wowCommandLog.txt')],
        ['Minecraft Command',(LOG_PATH + 'mcCommandLog.txt'),(ROSTER_PATH + 'mcCommandRoster.txt'),(MC_CMD),[9,10,59],(""),(LOGS + 'mcCommandLog.txt')],
        ['DayZ Command',(LOG_PATH + 'dayzCommandLog.txt'),(ROSTER_PATH + 'dayzCommandLog.txt'),(DAYZ_CMD),[9,10,11],(""),(LOGS + 'dayzCommandLog.txt')],
        ['Logistics Command',(LOG_PATH + 'logisticsCommandLog.txt'),(ROSTER_PATH + 'logisticsCommandRoster.txt'),(LOG_CMD),[9,10,58],(""),(LOGS + 'logisticsCommandLog.txt')],
        ['Military Police',(LOG_PATH + 'mpCommandLog.txt'),(ROSTER_PATH + 'mpCommandRoster.txt'),(MP_CMD),[9,10,58,17,18],(""),(LOGS + 'mpCommandLog.txt')],
        ['Admissions',(LOG_PATH + 'admissionsCommandLog.txt'),(ROSTER_PATH + 'admissionsCommandRoster.txt'),(ADM),[9,10,58,16,56],(""),(LOGS + 'admissionsCommandLog.txt')],
        ['Beta Test',(LOG_PATH + 'betaTestLog.txt'),(ROSTER_PATH + 'betaTestRoster.txt'),(BETA),(),(""),(LOGS + 'betaTestCommandLog.txt')],
        ['General',(LOG_PATH + 'generalLog.txt'),(ROSTER_PATH + 'generalRoster.txt'),(GEN),(),(""),(LOGS + 'generalLog.txt')],
        ['Call of Duty',(LOG_PATH + 'codLog.txt'),(ROSTER_PATH + 'codRoster.txt'),(COD),(),(""),(LOGS + 'codLog.txt')],
        ['Titanfall',(LOG_PATH + 'tfLog.txt'), (ROSTER_PATH + 'tfRoster.txt'),(TF),(),(""),(LOGS + 'tfLog.txt')],
        ['League of Legends',(LOG_PATH + 'lolLog.txt'),(ROSTER_PATH + 'lolRoster.txt'),(LOL),(),(""),(LOGS + 'lolLog.txt')],
        ['Guild Wars',(LOG_PATH + 'gwLog.txt'),(ROSTER_PATH + 'gwRoster.txt'),(GW),(),(""),(LOGS + 'gwLog.txt')],
        ['World of Warcraft',(LOG_PATH + 'wowLog.txt'),(ROSTER_PATH + 'wowRoster.txt'),(WOW),(),(""),(LOGS + 'wowLog.txt')],
        ['Minecraft',(LOG_PATH + 'mcLog.txt'),(ROSTER_PATH + 'mcRoster.txt'),(MC),(),(""),(LOGS + 'mcLog.txt')],
        ['DayZ',(LOG_PATH + 'dayzLog.txt'),(ROSTER_PATH + 'dayzLog.txt'),(DAYZ),(),(""),(LOGS + 'dayzLog.txt')],
        ['Social Media',(LOG_PATH + 'smLog.txt'),(ROSTER_PATH + 'smRoster.txt'),(SM),(),(""),(LOGS + 'smLog.txt')]
        ]
