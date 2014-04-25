import os, sys, os.path, time, socketserver
from online import Online

class Server(socketserver.BaseRequestHandler):
    def handle(self):
        # self.request is the TCP socket connected to the client
        time.sleep(.2)
        self.data = str(self.request.recv(1024),"utf-8")
        self.argv = self.data.rstrip().split(',')
        if self.argv[0] == "whos_online":
            self.users = Online.add(self.argv[1])
            self.online_users = ""
            for i in range(0,len(self.users)):
                self.online_users += self.users[i][0] + ","
            print(self.online_users)
            self.request.sendall(bytes(self.online_users + "\n", "utf-8"))
        elif self.argv[0] == "get_all_logs":
            self.time_stamps = ""
            for i in range(1,len(self.argv)):
                self.temp = ""
                if not os.path.exists(self.argv[i]):
                    f = open(self.argv[i], 'w')
                    f.write("Fresh Log\n\n")
                    f.close()
                self.temp = os.stat(self.argv[i])
                self.time_stamps += str(self.temp.st_mtime) + ","
            self.request.sendall(bytes(self.time_stamps + "\n", "utf-8"))
    
if __name__ == "__main__":
    #HOST, PORT = "0.0.0.0", 9999  #Production Server
    HOST, PORT = "0.0.0.0", 9998 # Developer Server

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), Server)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
