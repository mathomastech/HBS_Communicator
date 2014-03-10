from configuration import *
import mysql.connector

DB = ""

class Database:
    def establish_connection():
        global DB 
        DB = mysql.connector.connect(host=DB_IP,
                            user=DB_USER,
                            password=DB_PASSWORD,
                            db=DB_NAME
                            )
    
    def login(uname,passwd):
        Database.establish_connection()
        
        flag = Database.check_user(uname,passwd)
            
        if flag:
            userPermissions = Database.get_user_permissions(uname)
            channelPermissions = Database.get_channel_permissions()
            return flag, userPermissions, channelPermissions

        else:
            login_status_label.set_label("Incorrect Username or Password")
            return flag, "", ""

    def check_user(uname, passwd):
        cur = DB.cursor()
        query = ("SELECT username, password FROM gbgraphi_vbulletin.user WHERE user.username = '" + uname + "' and password = md5( concat(md5('" + passwd + "'), salt))")
        cur.execute(query)
           
        for (username, password) in cur:
            login_status_label.set_label("Success!")
            login_button.set_label(username)
            authorize.close()
            return True
        return False

    def get_user_permissions(uname):
        cur = DB.cursor()
        query = ("SELECT usergroupid, membergroupids FROM gbgraphi_vbulletin.user WHERE user.username = '" + uname + "'")
        cur.execute(query)
        for (usergroupid, membergroupids) in cur:
            perm = "{},{}".format(usergroupid,membergroupids)
            permissionsTemp = perm.split(',')
            permissions = [int(x) for x in permissionsTemp]
            return permissions
    
    def get_channel_permissions():
        Database.establish_connection()
        cur = DB.cursor()
        query = ("select usergroupid, usertitle from usergroup")
        cur.execute(query)
        queryString = ""
        for (usergroupid,usertitle) in cur:
            queryString += "{},{}".format(usergroupid, usertitle)
            queryString += "\n"
        arrTemp = queryString.split('\n')
        channelPermissions = []
        for i in range(0, len(arrTemp)):
            channelPermissions.append(arrTemp[i].split(","))        
        return channelPermissions
