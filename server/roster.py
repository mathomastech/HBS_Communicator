from config import Config
import mysql.connector

class Roster:
    
    ROSTER = []
    
    def __init__(self):
        super(Roster,self).__init__()
        
        self.DB = ""
        self.SORT_ORDER = []
        
        self.get_roster_raw()
        self.sort_roster()
        
    def establish_connection(self):
        self.DB = mysql.connector.connect(host=Config.c['DB IP'],
                            user=Config.c['DB User'],
                            password=Config.c['DB Password'],
                            db=Config.c['DB Name']
                            )

    def get_roster(self):
        return Roster.ROSTER
    
    def get_roster_raw(self):
        self.establish_connection()
        Roster.ROSTER = []
        self.cur = self.DB.cursor()
        self.query = ("select game.gname, rank.rank, user.username \
                from gbgraphi_vbulletin.clan_games as game, gbgraphi_vbulletin.clan_members_ranks as rank, gbgraphi_vbulletin.user as user, gbgraphi_vbulletin.clan_members_members as member \
                where user.userid = member.userid \
                and rank.rid = member.rank \
                and member.gid = game.gid;")
        self.cur.execute(self.query)
        for(gname, rank, username) in self.cur:
            Roster.ROSTER.append([gname,username,rank])

        self.query = ("select rank \
                 from gbgraphi_vbulletin.clan_members_ranks \
                order by rankorder;")
        self.cur.execute(self.query)
        for rank in self.cur:
            self.SORT_ORDER.append(rank[0])

    def sort_roster(self):
        self.temp_roster = []
        for i in range (0,len(self.SORT_ORDER)):
            for j in range(0,len(self.ROSTER)):
                if Roster.ROSTER[j][2] == self.SORT_ORDER[i]:
                    self.temp_roster.append(self.ROSTER[j])
        
        Roster.ROSTER = self.temp_roster


