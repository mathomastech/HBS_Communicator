'''
This file is to be run on the remote server that hosts the logs
It's primary purpose is to reduce the network requirements of the
client applications and shift the processing to the remote server

This will produce less network bandwidth and better performance 
overall
'''

import sys, os.path, time

#argv[0] = Channel Name, argv[1] = Log Path, argv[2] = Client Log

def main(argv):
    flag = True
    count = 0
    while flag:
        try:
            time.sleep(1)
            server = open(argv[1], 'r')
            client = open(argv[2], 'r')
            server_log = server.read()
            client_log = client.read()
            if client_log != server_log:
                client = open(argv[2], 'w')
                client.write(server_log)
                print(argv[0])
                flag = False
            else:
                count = count+1
        except FileNotFoundError:
                # Irrelevant line of code. When a file is being written to, it throws
                # File not found error, causing the loop to exit. This gives it something
                # to do as the file is being writted 
                one=1

main(sys.argv[1:])
