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
   
    LOG_PATH = Config.LOG_PATH
    ROSTER_PATH = Config.ROSTER_PATH
    # [0] = Channel Name, [1] = Log Path, [2] = Roster Path, [3] = GUI Element, [4] = Permissions,  [5] = Local Log, [6] = Remote Log 
    CHANNELS = [
        #['Welcome Message',(LOG_PATH + 'welcomeMessage.txt'),(ROSTER_PATH + 'generalRoster.txt'),(),(),()],
        ['Central Command',(LOG_PATH + 'centcomLog.txt'),(ROSTER_PATH + 'centcomRoster.txt'),(CENTCOM),[9,10],()],
        ['Operations Command',(LOG_PATH + 'operationsCommandLog.txt'),(ROSTER_PATH + 'operationsCommandRoster.txt'),(OP_CMD),[9,10],()],
        ['Call of Duty Command',(LOG_PATH + 'codCommandLog.txt'),(ROSTER_PATH + 'codCommandRoster.txt'),(COD_CMD),[9,10,57],()],
        ['Titanfall Command',(LOG_PATH + 'tfCommandLog.txt'),(ROSTER_PATH + 'tfCommandRoster.txt'),(TF_CMD),[9,10,54],()],
        ['League of Legends Command',(LOG_PATH + 'lolCommandLog.txt'),(ROSTER_PATH + 'lolCommandRoster.txt'),(LOL_CMD),[9,10,67],()],
        ['Guild Wars Command',(LOG_PATH + 'gwCommandLog.txt'),(ROSTER_PATH + 'gwCommandRoster.txt'),(GW_CMD),[9,10,66],()],
        ['World of Warcraft Command',(LOG_PATH + 'wowCommandLog.txt'),(ROSTER_PATH + 'wowCommandRoster.txt'),(WOW_CMD),[9,10,63],()],
        ['Minecraft Command',(LOG_PATH + 'mcCommandLog.txt'),(ROSTER_PATH + 'mcCommandRoster.txt'),(MC_CMD),[9,10,59],()],
        ['DayZ Command',(LOG_PATH + 'dayzCommandLog.txt'),(ROSTER_PATH + 'dayzCommandLog.txt'),(DAYZ_CMD),[9,10,11],()],
        ['Logistics Command',(LOG_PATH + 'logisticsCommandLog.txt'),(ROSTER_PATH + 'logisticsCommandRoster.txt'),(LOG_CMD),[9,10,58],()],
        ['Military Police',(LOG_PATH + 'mpCommandLog.txt'),(ROSTER_PATH + 'mpCommandRoster.txt'),(MP_CMD),[9,10,58,17,18],()],
        ['Admissions',(LOG_PATH + 'admissionsCommandLog.txt'),(ROSTER_PATH + 'admissionsCommandRoster.txt'),(ADM),[9,10,58,16,56],()],
        ['Beta Test',(LOG_PATH + 'betaTestLog.txt'),(ROSTER_PATH + 'betaTestRoster.txt'),(BETA),(),()],
        ['General',(LOG_PATH + 'generalLog.txt'),(ROSTER_PATH + 'generalRoster.txt'),(GEN),(),()],
        ['Call of Duty',(LOG_PATH + 'codLog.txt'),(ROSTER_PATH + 'codRoster.txt'),(COD),(),()],
        ['Titanfall',(LOG_PATH + 'tfLog.txt'), (ROSTER_PATH + 'tfRoster.txt'),(TF),(),()],
        ['League of Legends',(LOG_PATH + 'lolLog.txt'),(ROSTER_PATH + 'lolRoster.txt'),(LOL),(),()],
        ['Guild Wars',(LOG_PATH + 'gwLog.txt'),(ROSTER_PATH + 'gwRoster.txt'),(GW),(),()],
        ['World of Warcraft',(LOG_PATH + 'wowLog.txt'),(ROSTER_PATH + 'wowRoster.txt'),(WOW),(),()],
        ['Minecraft',(LOG_PATH + 'mcLog.txt'),(ROSTER_PATH + 'mcRoster.txt'),(MC),(),()],
        ['DayZ',(LOG_PATH + 'dayzLog.txt'),(ROSTER_PATH + 'dayzLog.txt'),(DAYZ),(),()],
        ['Social Media',(LOG_PATH + 'smLog.txt'),(ROSTER_PATH + 'smRoster.txt'),(SM),(),()]
        ]


