import paramiko
from config import Config
from gui import GUI
import os.path, socket, struct

class SSH():
    def connect_to_ssh():
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(
            paramiko.AutoAddPolicy())
        ssh.connect(Config.c['SSH IP'], 
                    username=Config.c['SSH User'], 
                    password=Config.c['SSH Password'])
        return ssh

    def get_active_log(ssh,log_path, tcp_host, tcp_port):
        # Get log for current channel and return to communicator.
        
        '''
        # Non-Functioning code for TCP based log retrieving. Logs are recieved but the 
        #            msglen = struct.unpack('>I', raw_msg_len)[0]
        # line of code seems to increase the size dramatically. Causing log retrieval 
        # to not occur 
        
        prefix = "get_active_log"
        received = ""
        log_path = Config.LOG_PATH + log_path
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((tcp_host, tcp_port))
            # Create string to be sent to server
            data = prefix + "," + log_path
            sock.sendall(bytes(data + "\n", "utf-8"))
            
            raw_msg_len = SSH.recvall(sock,4)
            if not raw_msg_len:
                return None
            msglen = struct.unpack('>I', raw_msg_len)[0]
            received = SSH.recvall(sock,msglen)
            print(received)
            return received
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

        '''
        log_path = Config.LOG_PATH + log_path
        query = 'cat ' + log_path
        stdin, stdout, stderr = ssh.exec_command(query)
        log = stdout.readlines()
        log = ''.join(log)
    
        return log
        

    def get_all_logs(tcp_host, tcp_port):
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
            raw_msg_len = SSH.recvall(sock,4)
            if not raw_msg_len:
                return None
            msglen = struct.unpack('>I', raw_msg_len)[0]
            received = str(SSH.recvall(sock,msglen),"utf-8")
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

            raw_msg_len = SSH.recvall(sock,4)
            if not raw_msg_len:
                return None
            msglen = struct.unpack('>I', raw_msg_len)[0]
            received = str(SSH.recvall(sock,msglen),"utf-8")
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
            raw_msg_len = SSH.recvall(sock,4)
            if not raw_msg_len:
                return None
            msglen = struct.unpack('>I', raw_msg_len)[0]
            received = str(SSH.recvall(sock,msglen),"utf-8")
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

    def recvall(sock,n):
        data = bytearray()
        while len(data) < n:
            packet = sock.recv(n-len(data))
            if not packet:
                return None
            data += packet
        return data

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
        log_path = Config.LOG_PATH + log_path
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
