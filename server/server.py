import os, sys, os.path, time, datetime, socketserver
from online import Online
from roster import Roster

class Server(socketserver.BaseRequestHandler):
    LOG_PATH = "/home/hbs/communicator/logs/"
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
                if not os.path.exists(self.LOG_PATH + self.argv[i]):
                    f = open(self.LOG_PATH + self.argv[i], 'w')
                    f.write("Fresh Log\n\n")
                    f.close()
                self.temp = os.stat(self.LOG_PATH + self.argv[i])
                self.time_stamps += str(self.temp.st_mtime) + ","
            self.request.sendall(bytes(self.time_stamps + "\n", "utf-8"))
        
        elif self.argv[0] == "get_channels":
            channels = Channels(self.LOG_PATH)

        elif self.argv[0] == "get_roster":
            roster = Roster()
            self.roster_arr = roster.get_roster()
            self.roster_str = ""
            for i in range(0,len(self.roster_arr)):
                self.roster_str += self.roster_arr[i][0] + ',' + self.roster_arr[i][1] + ',' + self.roster_arr[i][2] + '/'
            self.request.sendall(bytes(self.roster_str + "\n", "utf-8"))
        
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
    #HOST, PORT = "0.0.0.0", 9998  #Production Server
    HOST, PORT = "0.0.0.0", 8888 # Dev Server

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), Server)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
