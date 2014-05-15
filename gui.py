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
    CS_CMD = ""
    WS_CMD = ""
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
    CS = ""
    WS = ""
    SM = ""
    RAFFLE = ""
    
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
        ['Central Command',(LOG_PATH + 'centcom.txt'),(),(CENTCOM),["Central Command"],(""),(LOGS + 'centcom.txt'),('centcom.txt'),('command'),(["Central Command"]),([])],
        ['Operations Command',(LOG_PATH + 'operationsCommand.txt'),(),(OP_CMD),["Central Command"],(""),(LOGS + 'operationsCommand.txt'),('operationsCommand.txt'),('command'),(["Operations Officer","Brigade Officer"]),([])],
        ['Logistics Command',(LOG_PATH + 'logisticsCommand.txt'),(),(LOG_CMD),["Central Command", "Regulations Officer", "General Administrative Officer","Chief of Staff","MP Commanding Officer","MP Executive Officer","Director of Admissions","Director of Social Media","Director of Awards"],(""),(LOGS + 'logisticsCommand.txt'),('logisticsCommand.txt'),('command'),(["Logistics Officer","MP Commanding Officer","MP Executive Officer","Director of Admissions","Chief of Staff","Director of Awards","Regulations Officer","General Administrative Officer","Director of Financial Affairs","Director of Entertainment","Director of Social Media","Editor in Chief"]),([])],
        ['General',(LOG_PATH + 'general.txt'),(),(GEN),([]),(""),(LOGS + 'general.txt'),('general.txt'),('general'),([]),([])],
        ['DayZ Command',(LOG_PATH + 'dayzCommand.txt'),(),(DAYZ_CMD),["Central Command","DayZ Commanding Officer","DayZ Executive Officer","DayZ Chief Training Officer"],(""),(LOGS + 'dayzCommand.txt'),('dayzCommand.txt'),('command'),(["DayZ"]),([])],
        ['DayZ',(LOG_PATH + 'dayz.txt'),(),(DAYZ),([]),(""),(LOGS + 'dayz.txt'),('dayz.txt'),('general'),(["DayZ"]),([])],
        ['Titanfall Command',(LOG_PATH + 'tfCommand.txt'),(),(TF_CMD),["Central Command","Titanfall Commanding Officer","Titanfall Executive Officer","Titanfall Chief Training Officer"],(""),(LOGS + 'tfCommand.txt'),('tfCommand.txt'),('command'),(["TitanFall"]),([])],
        ['Titanfall',(LOG_PATH + 'tf.txt'), (),(TF),([]),(""),(LOGS + 'tf.txt'),('tf.txt'),('general'),(["TitanFall"]),([])],
        ['Call of Duty Command',(LOG_PATH + 'codCommand.txt'),(),(COD_CMD),["Central Command","CoD Commanding Officer","CoD Executive Officer","CoD Chief Training Officer"],(""),(LOGS + 'codCommand.txt'),('codCommand.txt'),('command'),(["Call of Duty Ghosts"]),([])],
        ['Call of Duty',(LOG_PATH + 'cod.txt'),(),(COD),([]),(""),(LOGS + 'cod.txt'),('cod.txt'),('general'),(["Call of Duty Ghosts","Call of Duty Black Ops 2"]),([])],
        ['World of Warcraft Command',(LOG_PATH + 'wowCommand.txt'),(),(WOW_CMD),["Central Command","WoW Commanding Officer","WoW Executive Officer","WoW Chief Training Officer"],(""),(LOGS + 'wowCommand.txt'),('wowCommand.txt'),('command'),(["World of Warcraft"]),([])],
        ['World of Warcraft',(LOG_PATH + 'wow.txt'),([]),(WOW),(),(""),(LOGS + 'wow.txt'),('wow.txt'),('general'),(["World of Warcraft"]),([])],
        ['Guild Wars Command',(LOG_PATH + 'gwCommand.txt'),(),(GW_CMD),["Central Command","Guild Wars Commanding Officer","Guild Wars Executive Officer","Guild Wars Chief Training Officer"],(""),(LOGS + 'gwCommand.txt'),('gwCommand.txt'),('command'),(["Guild Wars 2"]),([])],
        ['Guild Wars',(LOG_PATH + 'gw.txt'),(),(GW),([]),(""),(LOGS + 'gw.txt'),('gw.txt'),('general'),(["Guild Wars 2"]),([])],
        ['League of Legends Command',(LOG_PATH + 'lolCommand.txt'),(),(LOL_CMD),["Central Command","LoL Platoon Leader"],(""),(LOGS + 'lolCommand.txt'),('lolCommand.txt'),('command'),(["League of Legends"]),([])],
        ['League of Legends',(LOG_PATH + 'lol.txt'),([]),(LOL),(),(""),(LOGS + 'lol.txt'),('lol.txt'),('general'),(["League of Legends"]),([])],
        ['Counter Strike Command',(LOG_PATH + 'csCommand.txt'),(),(CS_CMD),(["Central Command","Counter Strike Commanding Officer","Counter Strike Executive Officer","Counter Strike Chief Training Officer","CS:GO Platoon Leader"]),(""),(LOGS + 'csCommand.txt'),('csCommand.txt'),('command'),(["Counter Strike Global Offensive"]),([])],
        ['Counter Strike',(LOG_PATH + 'cs.txt'),(),(CS),([]),(""),(LOGS + 'cs.txt'),('cs.txt'),('general'),(["Counter Strike Global Offensive"]),([])],
        ['Minecraft Command',(LOG_PATH + 'mcCommand.txt'),(),(MC_CMD),["Central Command","Minecraft Platoon Leader"],(""),(LOGS + 'mcCommand.txt'),('mcCommand.txt'),('command'),(["Minecraft"]),([])],
        ['Minecraft',(LOG_PATH + 'mc.txt'),(),(MC),([]),(""),(LOGS + 'mc.txt'),('mc.txt'),('general'),(["Minecraft"]),([])],
        #['WildStar Command',(LOG_PATH + 'wsCommand.txt'),(),(WS_CMD),(["Central Command","WildStar Platoon Leader"]),(""),(LOGS + 'wsCommand.txt'),('wsCommand.txt'),('command'),(["WildStar"]),([])],
        #['WildStar',(LOG_PATH + 'ws.txt'),(),(WS),([]),(""),(LOGS + 'ws.txt'),('ws.txt'),('general'),(["WildStar"]),([])],
        ['Social Media',(LOG_PATH + 'sm.txt'),(),(SM),([]),(""),(LOGS + 'sm.txt'),('sm.txt'),('general'),(["SocO Officer","Director of Social Media"]),([])],
        ['Raffle',(LOG_PATH + 'raffle.txt'),(),(RAFFLE),([]),(""),(LOGS + 'raffle.txt'),('raffle.txt'),('general'),([]),([])],
        ['Military Police',(LOG_PATH + 'mp.txt'),(),(MP_CMD),["Central Command","MP Commanding Officer","MP Executive Officer"],(""),(LOGS + 'mp.txt'),('mp.txt'),('command'),(["Military Police Department"]),([])],
        ['Admissions',(LOG_PATH + 'admissions.txt'),(),(ADM),["Central Command","Admissions Department"],(""),(LOGS + 'admissions.txt'),('admissions.txt'),('command'),(["Admissions Department"]),([])],
        ['Beta Test',(LOG_PATH + 'betaTest.txt'),(),(BETA),([]),(""),(LOGS + 'betaTest.txt'),('betaTest.txt'),('command'),(["Beta Test"]),([])]
        ]
