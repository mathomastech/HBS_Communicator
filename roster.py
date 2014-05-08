from config import Config
import mysql.connector

class Roster:
    DB = ""
    ROSTER = []
    SORT_ORDER = []
    
    def establish_connection():
        Roster.DB = mysql.connector.connect(host=Config.c['DB IP'],
                            user=Config.c['DB User'],
                            password=Config.c['DB Password'],
                            db=Config.c['DB Name']
                            )

    def get_roster():
        Roster.get_roster_raw()
        Roster.sort_roster()
        return Roster.ROSTER
    
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

        query = ("select rank \
                 from gbgraphi_vbulletin.clan_members_ranks \
                order by rankorder;")
        cur.execute(query)
        for rank in cur:
            Roster.SORT_ORDER.append(rank[0])
        
    def sort_roster():
        temp_roster = []
        for i in range (0,len(Roster.SORT_ORDER)):
            for j in range(0,len(Roster.ROSTER)):
                if Roster.ROSTER[j][2] == Roster.SORT_ORDER[i]:
                    temp_roster.append(Roster.ROSTER[j])
        
        Roster.ROSTER = temp_roster


