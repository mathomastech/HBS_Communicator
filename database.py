#!/usr/bin/python3.3
from gui import GUI
from config import Config
import mysql.connector


class Database:
    DB = ""
    def establish_connection():
        Database.DB = mysql.connector.connect(host=Config.c['DB IP'],
                            user=Config.c['DB User'],
                            password=Config.c['DB Password'],
                            db=Config.c['DB Name']
                            )
    
    def login(uname,passwd):
        Database.establish_connection()
        
        flag = Database.check_user(uname,passwd)
            
        if flag:
            userPermissions = Database.get_user_permissions(uname)
            channelPermissions = Database.get_channel_permissions()
            return flag, userPermissions, channelPermissions

        else:
            GUI.LOGIN_STATUS_LABEL.setText("Incorrect Username or Password")
            return flag, "", ""

    def check_user(uname, passwd):
        cur = Database.DB.cursor()
        query = ("SELECT username, password FROM gbgraphi_vbulletin.user WHERE user.username = '" + uname + "' and password = md5( concat(md5('" + passwd + "'), salt))")
        cur.execute(query)
           
        for (username, password) in cur:
            GUI.LOGIN_STATUS_LABEL.setText("Success!")
            GUI.USER_BTN.setText(username)
            return True
        return False

    def get_user_permissions(uname):
        cur = Database.DB.cursor()
        query = ("SELECT usergroupid, membergroupids FROM gbgraphi_vbulletin.user WHERE user.username = '" + uname + "'")
        cur.execute(query)
        for (usergroupid, membergroupids) in cur:
            perm = "{},{}".format(usergroupid,membergroupids)
            permissionsTemp = perm.split(',')
            permissions = [int(x) for x in permissionsTemp]
            return permissions
    
    def get_channel_permissions():
        Database.establish_connection()
        cur = Database.DB.cursor()
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
