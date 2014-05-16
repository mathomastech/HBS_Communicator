import os, sys, os.path, time, datetime, socketserver, struct
from config import Config
from online import Online
from roster import Roster
from channels import Channels

class Server(socketserver.BaseRequestHandler):
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = str(self.request.recv(1024),"utf-8")
        self.argv = self.data.rstrip().split(',')
        
        if self.argv[0] == "get_active_log":
            log_path = self.argv[1]
            length = os.path.getsize(log_path)
            self.request.send(Server.convert_to_bytes(length))
            with open(log_path, 'r') as infile:
                log = infile.read(1024)
                while log:
                    self.request.sendall(bytes(log + "\n", "utf-8"))
                    log = infile.read(1024)
        
        elif self.argv[0] == "get_all_logs":
            self.time_stamps = ""
            for i in range(1,len(self.argv)):
                self.temp = ""
                if not os.path.exists(Config.c['LOG PATH'] + self.argv[i]):
                    f = open(Config.c['LOG PATH'] + self.argv[i], 'w')
                    f.write("Fresh Log\n\n")
                    f.close()
                self.temp = os.stat(Config.c['LOG PATH'] + self.argv[i])
                self.time_stamps += str(self.temp.st_mtime) + ","
            
            self.time_stamps = self.time_stamps.encode(encoding='UTF-8')
            self.time_stamps = struct.pack('>I',len(self.time_stamps)) + self.time_stamps
            self.request.sendall(self.time_stamps)
            #self.request.sendall(bytes(self.time_stamps + "\n", "utf-8"))
        
        elif self.argv[0] == "get_channels":
            channels_raw = Channels()
            self.channels = channels_raw.get_list()
            self.channel_str = ""
            for i in range(0,len(self.channels)):
                self.channel_str += self.channels[i][0] + "/"
                for j in range(0,len(self.channels[i][1])):
                    self.channel_str += self.channels[i][1][j] + ","
                if len(self.channels[i][1]) == 0:
                    self.channel_str += "none,"
                self.channel_str = self.channel_str[:-1]
                self.channel_str += "/"
                self.channel_str += self.channels[i][2] + "/"
                for j in range(0,len(self.channels[i][3])):
                    self.channel_str += self.channels[i][3][j] + ","
                if len(self.channels[i][3]) == 0:
                    self.channel_str += "none,"
                self.channel_str = self.channel_str[:-1]
                self.channel_str += "//"

            self.channel_str = self.channel_str[:-2]
            self.request.sendall(bytes(self.channel_str + "\n", "utf-8"))

        elif self.argv[0] == "get_roster":
            roster = Roster()
            self.roster_arr = roster.get_roster()
            self.roster_str = ""
            for i in range(0,len(self.roster_arr)):
                self.roster_str += self.roster_arr[i][0] + ',' + self.roster_arr[i][1] + ',' + self.roster_arr[i][2] + '/'
            
            self.roster_str = self.roster_str.encode(encoding='UTF-8')
            self.roster_str = struct.pack('>I',len(self.roster_str)) + self.roster_str
            self.request.sendall(self.roster_str)
            #self.request.sendall(bytes(self.roster_str + "\n", "utf-8"))
        
        elif self.argv[0] == "new_post":
            log_path = self.argv[1]
            log = ""
            for i in range(2,len(self.argv)):
                log += self.argv[i] + ","
            log = log[:-1]
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%m/%d > %H:%M >')
            log = st + ' ' + log + '\n----------\n\n'
            f = open(log_path, 'a')
            f.write(log)
            f.close()
        
        elif self.argv[0] == "whos_online":
            self.users = Online.add(self.argv[1])
            self.online_users = ""
            for i in range(0,len(self.users)):
                self.online_users += self.users[i][0] + ","
            self.request.sendall(bytes(self.online_users + "\n", "utf-8"))
        

    def convert_to_bytes(no):
        result = bytearray()
        result.append(no & 255)
        for i in range(3):
            no = no >> 8
            result.append(no & 255)
        return result

    def bytes_to_number(b):
        res = 0
        for i in range(4):
            res += b[i] << (i*8)
        return res


if __name__ == "__main__":
    
    HOST, PORT = "0.0.0.0", Config.c['TCP PORT']

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), Server)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
