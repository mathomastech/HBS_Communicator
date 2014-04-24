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

    def get_active_log(ssh,log_path):
        # Get log for current channel and return to communicator.
        query = 'cat ' + log_path
        stdin, stdout, stderr = ssh.exec_command(query)
        log = stdout.readlines()
        log = ''.join(log)

        return log


    def get_all_logs(ssh, user, tcp_host, tcp_port):
        # Get remote logs for all channels and return to communicator.
        delta = []
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            sock.connect((tcp_host, tcp_port))
            data = user
            for i in range(0, len(GUI.CHANNELS)):
                data += "," + GUI.CHANNELS[i][GUI.SERVER_LOG_PATH]
            data = data[:-1]
            
            sock.sendall(bytes(data + "\n", "utf-8"))
            received = str(sock.recv(1024),"utf-8")
        finally:
            sock.close()
       
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

        return delta

    def write_to_log(ssh,log_path,log):
        # Get and parse timestamp from server
        stdin,stdout,stderr = ssh.exec_command('date +"%H:%M:%S |"')
        timestamp = stdout.readlines()
        timestamp = timestamp[0]
        timestamp = timestamp.rstrip()

        # Write timestamp and log to appropriate file
        query = 'echo "' + timestamp + ' ' + log + "\n" + '" >> ' + log_path
        ssh.exec_command(query)
