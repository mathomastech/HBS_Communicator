import os, sys, os.path, time, socketserver
from online import Online

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # self.request is the TCP socket connected to the client
        time.sleep(.2)
        self.data = str(self.request.recv(1024),"utf-8")
        self.argv = self.data.rstrip().split(',')
        self.time_stamps = ""
        Online.add(self.argv[0])
        Online.remove()
        for i in range(1,len(self.argv)):
            self.temp = ""
            if not os.path.exists(self.argv[i]):
                f = open(self.argv[i], 'w')
                f.write("Fresh Log\n\n")
                f.close()
            self.temp = os.stat(self.argv[i])
            self.time_stamps += str(self.temp.st_mtime) + ", "

        self.request.sendall(bytes(self.time_stamps + "\n", "utf-8"))
    
if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 9998


    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
