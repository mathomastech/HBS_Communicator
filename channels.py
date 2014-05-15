from gui import GUI

class Channels():

    def __init__(self):
        super(Channels,self).__init__()
         
        lst = [["Central Command",["Central Command","Operations Command"],"command",["Central Command","Operations Command"]],
                ["Operations Command",["Central Command","Operations Officer","Brigade Officer"],"command",["Operations Officer","Brigade Officer"]],
                ['Logistics Command',["Central Command", "Regulations Officer", "General Administrative Officer","Chief of Staff","MP Commanding Officer","MP Executive Officer","Director of Admissions","Director of Social Media","Director of Awards"],'command',["Logistics Officer","MP Commanding Officer","MP Executive Officer","Director of Admissions","Chief of Staff","Director of Awards","Regulations Officer","General Administrative Officer","Director of Financial Affairs","Director of Entertainment","Director of Social Media","Editor in Chief"]],
                ['General',[],'general',[]],
                ['DayZ Command',["Central Command","DayZ Commanding Officer","DayZ Executive Officer","DayZ Chief Training Officer"],'command',["DayZ"]],
                ['DayZ',[],"gemeral",["DayZ"]],
                ['Titanfall Command',["Central Command","Titanfall Commanding Officer","Titanfall Executive Officer","Titanfall Chief Training Officer"],'command',["TitanFall"]],
                ['Titanfall',[],'general',["TitanFall"]],
                ['Call of Duty Command',["Central Command","CoD Commanding Officer","CoD Executive Officer","CoD Chief Training Officer"],'command',["Call of Duty Ghosts"]],
                ['Call of Duty',[],'general',["Call of Duty Ghosts","Call of Duty Black Ops 2"]],
                ['World of Warcraft Command',["Central Command","WoW Commanding Officer","WoW Executive Officer","WoW Chief Training Officer"],('command'),["World of Warcraft"]],
                ['World of Warcraft',[],('general'),["World of Warcraft"]],
                ['Guild Wars Command',["Central Command","Guild Wars Commanding Officer","Guild Wars Executive Officer","Guild Wars Chief Training Officer"],('command'),["Guild Wars 2"]],
                ['Guild Wars',[],'general',["Guild Wars 2"]],
                ['League of Legends Command',["Central Command","LoL Platoon Leader"],('command'),["League of Legends"]],
                ['League of Legends',[],('general'),["League of Legends"]],
                ['Counter Strike Command',["Central Command","Counter Strike Commanding Officer","Counter Strike Executive Officer","Counter Strike Chief Training Officer","CS:GO Platoon Leader"],'command',["Counter Strike Global Offensive"]],
                ['Counter Strike',([]),'general',["Counter Strike Global Offensive"]],
                ['Minecraft Command',["Central Command","Minecraft Platoon Leader"],'command',["Minecraft"]],
                ['Minecraft',[],'general',["Minecraft"]],
                ['WildStar Command',["Central Command","WildStar Platoon Leader"],'command',["WildStar"]],
                ['WildStar',[],'general',["WildStar"]],
                ['Social Media',[],'general',["SocO Officer","Director of Social Media"]],
                ['Raffle',[],'general',[]],
                ['Military Police',["Central Command","MP Commanding Officer","MP Executive Officer"],'command',["Military Police Department"]],
                ['Admissions',["Central Command","Admissions Department"],'command',["Admissions Department"]],
                ['Beta Test',[],'command',["Beta Test"]]
                ]
        
        for i in range(0,len(lst)):
            channel = lst[i][0]
            permissions = ""
            for j in range(0,len(lst[i][1])):
                permissions += lst[i][1][j] + ","
            permissions = permissions[:-1] 
            tab_group = lst[i][2]
            roster_groups = ""
            for j in range(0,len(lst[i][3])):
                roster_groups += lst[i][3][j] + ","
            roster_groups = roster_groups[:-1] 
        
            GUI.CHANNELS.append(self.generate_channel_info(channel,permissions,tab_group,roster_groups))
    
        print(GUI.CHANNELS[3])
    
    def generate_channel_info(self,channel,permissions,tab_group,roster_groups):
        chan_arr = []
        lower = channel.lower()
        lower = lower.replace(" ", "")
        gui_element = lower.upper()
        filename = lower + ".txt"
        server_log_path = GUI.LOG_PATH + filename
        permissions = permissions.split(",")
        roster_groups = roster_groups.split(",")

        chan_arr.append(channel)                            #Channel Name
        chan_arr.append(server_log_path)                    #Server Log Path
        chan_arr.append("")                                 #Unused Index
        chan_arr.append(gui_element)                        #GUI Element
        chan_arr.append(permissions)                        #Permissions
        chan_arr.append("")                                 #Local Time Stamp
        chan_arr.append(GUI.LOGS + filename)                #Local Log Path
        chan_arr.append(filename)                           #Channel File
        chan_arr.append(tab_group)                          #Tab Group
        chan_arr.append(roster_groups)                      #Roster Group
        chan_arr.append([])                                 #Roster
        
        return chan_arr
