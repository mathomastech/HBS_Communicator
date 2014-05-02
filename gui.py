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
    ONLINE_LIST = ""
    CHANNEL_TAB = ""

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
    #UNUSED INDEX = 2
    GUI_ELEMENT = 3
    PERMISSIONS = 4
    LOCAL_TIME_STAMP = 5
    LOCAL_LOG_PATH = 6
    CHANNEL_FILE = 7 
    CHANNEL_GROUP = 8
    ROSTER_GROUP_NAME = 9
    ROSTER = 10
    CHANNELS = [
        ['Central Command',(LOG_PATH + 'centcom.txt'),(),(CENTCOM),[9,10],(""),(LOGS + 'centcom.txt'),('centcom.txt'),('command'),(["Central Command"]),([])],
        ['Operations Command',(LOG_PATH + 'operationsCommand.txt'),(),(OP_CMD),[9,10],(""),(LOGS + 'operationsCommand.txt'),('operationsCommand.txt'),('command'),(["Operations Officer","Central Command Support Staff"]),([])],
        ['Call of Duty Command',(LOG_PATH + 'codCommand.txt'),(),(COD_CMD),[9,10,57],(""),(LOGS + 'codCommand.txt'),('codCommand.txt'),('command'),(["Call of Duty Ghosts", "Call of Duty Black Ops 2"]),([])],
        ['Titanfall Command',(LOG_PATH + 'tfCommand.txt'),(),(TF_CMD),[9,10,54],(""),(LOGS + 'tfCommand.txt'),('tfCommand.txt'),('command'),(["TitanFall"]),([])],
        ['League of Legends Command',(LOG_PATH + 'lolCommand.txt'),(),(LOL_CMD),[9,10,67],(""),(LOGS + 'lolCommand.txt'),('lolCommand.txt'),('command'),(["League of Legends"]),([])],
        ['Guild Wars Command',(LOG_PATH + 'gwCommand.txt'),(),(GW_CMD),[9,10,66],(""),(LOGS + 'gwCommand.txt'),('gwCommand.txt'),('command'),(["Guild Wars 2"]),([])],
        ['World of Warcraft Command',(LOG_PATH + 'wowCommand.txt'),(),(WOW_CMD),[9,10,63],(""),(LOGS + 'wowCommand.txt'),('wowCommand.txt'),('command'),(["World of Warcraft"]),([])],
        ['Minecraft Command',(LOG_PATH + 'mcCommand.txt'),(),(MC_CMD),[9,10,59],(""),(LOGS + 'mcCommand.txt'),('mcCommand.txt'),('command'),(["Minecraft"]),([])],
        ['DayZ Command',(LOG_PATH + 'dayzCommand.txt'),(),(DAYZ_CMD),[9,10,11],(""),(LOGS + 'dayzCommand.txt'),('dayzCommand.txt'),('command'),(["DayZ"]),([])],
        ['Logistics Command',(LOG_PATH + 'logisticsCommand.txt'),(),(LOG_CMD),[9,10,58],(""),(LOGS + 'logisticsCommand.txt'),('logisticsCommand.txt'),('command'),(["Logistics Officer"]),([])],
        ['Military Police',(LOG_PATH + 'mp.txt'),(),(MP_CMD),[9,10,58,17,18],(""),(LOGS + 'mp.txt'),('mp.txt'),('command'),(["Military Police Department"]),([])],
        ['Admissions',(LOG_PATH + 'admissions.txt'),(),(ADM),[9,10,58,16,56],(""),(LOGS + 'admissions.txt'),('admissions.txt'),('command'),(["Admissions Department"]),([])],
        ['Beta Test',(LOG_PATH + 'betaTest.txt'),(),(BETA),([]),(""),(LOGS + 'betaTest.txt'),('betaTest.txt'),('command'),(["Beta Test"]),([])],
        ['General',(LOG_PATH + 'general.txt'),(),(GEN),([]),(""),(LOGS + 'general.txt'),('general.txt'),('general'),(["General"]),([])],
        ['Call of Duty',(LOG_PATH + 'cod.txt'),(),(COD),([]),(""),(LOGS + 'cod.txt'),('cod.txt'),('general'),(["Call of Duty Ghosts","Call of Duty Black Ops 2"]),([])],
        ['Titanfall',(LOG_PATH + 'tf.txt'), (),(TF),([]),(""),(LOGS + 'tf.txt'),('tf.txt'),('general'),(["TitanFall"]),([])],
        ['League of Legends',(LOG_PATH + 'lol.txt'),([]),(LOL),(),(""),(LOGS + 'lol.txt'),('lol.txt'),('general'),(["League of Legends"]),([])],
        ['Guild Wars',(LOG_PATH + 'gw.txt'),(),(GW),([]),(""),(LOGS + 'gw.txt'),('gw.txt'),('general'),(["Guild Wars 2"]),([])],
        ['World of Warcraft',(LOG_PATH + 'wow.txt'),([]),(WOW),(),(""),(LOGS + 'wow.txt'),('wow.txt'),('general'),(["World of Warcraft"]),([])],
        ['Minecraft',(LOG_PATH + 'mc.txt'),(),(MC),([]),(""),(LOGS + 'mc.txt'),('mc.txt'),('general'),(["Minecraft"]),([])],
        ['DayZ',(LOG_PATH + 'dayz.txt'),(),(DAYZ),([]),(""),(LOGS + 'dayz.txt'),('dayz.txt'),('general'),(["DayZ"]),([])],
        ['Social Media',(LOG_PATH + 'sm.txt'),(),(SM),([]),(""),(LOGS + 'sm.txt'),('sm.txt'),('general'),(["Director of Social Media"]),([])]
        ]
