from config import Config
import mysql.connector

class Roster:
    DB = ""
    ROSTER = []
    SORT_ORDER = ['Commander in Chief','Deputy Commander in Chief','General of the Army','Operations Officer', 'Logistics Officer',
            'Technical Expert Command Officer','Social Officer','Regulations Officer','General Administrative Officer',
            'Brigade Officer','Chief of Staff','Directory of Financial Affairs','Director of Admissions','Director of Social Media',
            'Awards Director','MP Commanding Officer', 'Editor In Chief','MP Executive Officer','Senior Admissions Officer',
            'Titanfall Commanding Officer','Titanfall Executive Officer','Titanfall Chief Training Officer','CoD Commanding Officer',
            'CoD Executive Officer','CoD Chief Training Officer','DayZ Commanding Officer','DayZ Executive Officer','DayZ Chief Training Officer',
            'GW2 Commanding Officer','GW2 Executive Officer','GW2 Chief Training Officer','WoW Commanding Officer','WoW Executive Officer',
            'WoW Chief Training Officer','LoL Platoon Leader','Minecraft Platoon Leader','CS:GO Platoon Leader',
            '5* General','General','Lieutenant General','Major General','Brigadier General','Colonel', 'Lieutenant Colonel',
            'Major','Captain','First Lieutenant','Second Lieutenant','Command Sergeant Major', 'Sergeant Major',
            'First Sergeant','Master Sergeant','Sergeant First Class','Staff Sergeant','Sergeant','Corporal',
            'Private First Class','Private','Recruit']

    def establish_connection():
        Roster.DB = mysql.connector.connect(host=Config.c['DB IP'],
                            user=Config.c['DB User'],
                            password=Config.c['DB Password'],
                            db=Config.c['DB Name']
                            )

    def get_roster_raw():
        Roster.establish_connection()
        Roster.ROSTER = []
        cur = Roster.DB.cursor()
        query = ("select game.gname, rank.rank, user.username \
                from gbgraphi_vbulletin.clan_games as game, gbgraphi_vbulletin.clan_members_ranks as rank, gbgraphi_vbulletin.user as user, gbgraphi_vbulletin.clan_members_members as member \
                where user.userid = member.userid \
                and rank.rid = member.rank \
                and member.gid = game.gid;")
        cur.execute(query)
        for(gname, rank, username) in cur:
            Roster.ROSTER.append([gname,username,rank])

    def sort_roster():
        temp_roster = []
        for i in range (0,len(Roster.SORT_ORDER)):
            for j in range(0,len(Roster.ROSTER)):
                if Roster.ROSTER[j][2] == Roster.SORT_ORDER[i]:
                    temp_roster.append(Roster.ROSTER[j])
        
        Roster.ROSTER = temp_roster


    def get_roster():
        Roster.get_roster_raw()
        Roster.sort_roster()
        return Roster.ROSTER
