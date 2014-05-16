import paramiko
from config import Config
from gui import GUI
import os.path, socket

class SSH():
    def connect_to_ssh():
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(
            paramiko.AutoAddPolicy())
        ssh.connect(Config.c['SSH IP'], 
                    username=Config.c['SSH User'], 
                    password=Config.c['SSH Password'])
        return ssh

    def convert_to_bytes(no):
        result = bytearray()
        result.append(no & 255)
        for i in range(3):
            no = no >> 8
            result.append(no & 255)
        return result

    def bytes_to_number(b):
        # if Python2.x                  
        # b = map(ord, b)
        res = 0
        for i in range(4):   
            res += b[i] << (i*8)                     
        return res

    def get_active_log(ssh,log_path): #, tcp_host, tcp_port):
        # Get log for current channel and return to communicator.
        '''
        # Functioning code for TCP based log retrieving. Unfortunatelly it appears the performance
        # over TCP is less than over SSH so until performance can be improved, SSH will be the 
        # default method of retrieving logs
        prefix = "get_active_log"
        log = ""
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socksize = 1024
        try:
            sock.connect((tcp_host, tcp_port))
            # Create string to be sent to server
            data = prefix + "," + log_path
            sock.sendall(bytes(data + "\n", "utf-8"))
            size = sock.recv(4)
            size = SSH.bytes_to_number(size)
            current_size = 0
            buffer = b""
            while current_size < size:
                data = sock.recv(socksize)
                #if not data:
                #    break
                if len(data) + current_size > size:
                    data = data[:size-current_size]
                log += data.decode(encoding='UTF-8')
                current_size += len(data)
        finally:
            sock.close()
        '''
        query = 'cat ' + log_path
        stdin, stdout, stderr = ssh.exec_command(query)
        log = stdout.readlines()
        log = ''.join(log)
    
        return log


    def get_all_logs(user, tcp_host, tcp_port):
        # Get remote logs for all channels and return to communicator.
        delta = []
        prefix = "get_all_logs"
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            sock.connect((tcp_host, tcp_port))
            data = prefix
            # Create string to be sent to server
            for i in range(0, len(GUI.CHANNELS)):
                data += "," + GUI.CHANNELS[i][GUI.CHANNEL_FILE]    
            sock.sendall(bytes(data + "\n", "utf-8"))
            received = str(sock.recv(4096),"utf-8")
            # Parse string recieved from server and compare timestamps
            data = received.rstrip().split(',')
            for i in range(0,len(GUI.CHANNELS)):
                if GUI.CHANNELS[i][GUI.LOCAL_TIME_STAMP] != data[i]:
                    delta.append(GUI.CHANNELS[i][GUI.CHANNEL_NAME])
                    GUI.CHANNELS[i][GUI.LOCAL_TIME_STAMP] = data[i]
                    if not os.path.exists(GUI.LOGS):
                        os.makedirs(GUI.LOGS)
                    f = open(GUI.CHANNELS[i][GUI.LOCAL_LOG_PATH],'w')
                    f.write(data[i])
                    f.close()
            # Return any updates that have occurred
            return delta
        except ConnectionRefusedError:
            pass
        except TimeoutError:
            pass
        except socket.gaierror:
            pass
        except ConnectionResetError:
            pass
        finally:
            sock.close()
   
    def get_all_rosters(tcp_host, tcp_port):
        roster = []
        prefix = "get_roster"
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        received = ""
        try:
            sock.connect((tcp_host, tcp_port))
            data = prefix
            # Create string to be sent to server
            sock.sendall(bytes(data + "\n", "utf-8"))
            received = str(sock.recv(8192),"utf-8")
        except ConnectionRefusedError:
            pass
        except TimeoutError:
            pass
        except socket.gaierror:
            pass
        except ConnectionResetError:
            pass
        finally:
            sock.close()

        if received:
            temp_roster = received.split('/')
            for i in range(0,len(temp_roster)):
                roster.append(temp_roster[i].split(','))
            roster.pop(len(roster)-1)
            #print(roster)
        return roster

    def get_channels(tcp_host, tcp_port):
        prefix ="get_channels"
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        received = ""
        try:
            sock.connect((tcp_host, tcp_port))
            data = prefix
            # Create string to be sent to server
            sock.sendall(bytes(data + "\n", "utf-8"))
            received = str(sock.recv(8192),"utf-8")
            received = received[:-1]
            raw = received.split("//")
            channels = []
            for i in range(0,len(raw)):
                channel_array = []
                channel_data = raw[i].split('/')
                for j in range(0,len(channel_data)):
                    data = channel_data[j].split(",")
                    channel_array.append(data)
                channels.append(channel_array)
            #print(channels)
            return channels
            

        except ConnectionRefusedError:
            pass
        except TimeoutError:
            pass
        except socket.gaierror:
            pass
        except ConnectionResetError:
            pass
        finally:
            sock.close()

    def whos_online(tcp_host, tcp_port, online_users, user):
        # Get a list of all currently logged in clients to the server
        users = []
        prefix = "whos_online"
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((tcp_host, tcp_port))
            # Create string to be sent to server
            data = prefix + "," + user
            sock.sendall(bytes(data + "\n", "utf-8"))
            received = str(sock.recv(2048),"utf-8")
            # Parse string recieved from server and return online list to worker for analysis
            online = received.rstrip().split(',')
            online.pop(len(online)-1)
            online.sort()
            return online
        except ConnectionRefusedError:
            pass
        except TimeoutError:
            pass
        except socket.gaierror:
            pass
        except ConnectionResetError:
            pass
        finally:
            sock.close()

    def write_to_log(log_path,log, tcp_host, tcp_port):
        prefix = "new_post"
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((tcp_host, tcp_port))
            # Create string to be sent to server
            data = prefix + "," + log_path + "," + log
            sock.sendall(bytes(data + "\n", "utf-8"))
        except ConnectionRefusedError:
            pass
        except TimeoutError:
            pass
        except socket.gaierror:
            pass
        except ConnectionResetError:
            pass
        finally:
            sock.close()
