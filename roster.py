from config import Config
import mysql.connector

class Roster:
    DB = ""
    ROSTER = []
    def establish_connection():
        Roster.DB = mysql.connector.connect(host=Config.c['DB IP'],
                            user=Config.c['DB User'],
                            password=Config.c['DB Password'],
                            db=Config.c['DB Name']
                            )

    def get_roster_raw():
        Roster.establish_connection()
        
        cur = Roster.DB.cursor()
        query = ("select game.gname, rank.rank, user.username \
                from gbgraphi_vbulletin.clan_games as game, gbgraphi_vbulletin.clan_members_ranks as rank, gbgraphi_vbulletin.user as user, gbgraphi_vbulletin.clan_members_members as member \
                where user.userid = member.userid \
                and rank.rid = member.rank \
                and member.gid = game.gid;")
        cur.execute(query)
        for(gname, rank, username) in cur:
            Roster.ROSTER.append([gname,username,rank])
        return Roster.ROSTER
