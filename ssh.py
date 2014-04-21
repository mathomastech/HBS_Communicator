import paramiko
from config import Config
from gui import GUI
import os.path

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


    def get_all_logs(ssh, user):
        # Get remote logs for all channels and return to communicator.
        delta = []
        user_path = Config.USERS_PATH + user + '/'
        
        
        query = 'python ' + Config.SERVER_PATH + ' ' + '"' + GUI.CHANNELS[12][GUI.CHANNEL_NAME] + '"' + ' ' + GUI.CHANNELS[12][1] + ' ' + user_path +  'betaTestLog.txt'
        #print(query)
        stdin, stdout, stderr = ssh.exec_command(query) 
        log = stdout.readlines()
        log = log[0].rstrip('\n')
        print(log)

        '''
        for i in range(0, len(GUI.CHANNELS)):
            query = 'cat ' + GUI.CHANNELS[i][GUI.SERVER_LOG_PATH]
            stdin, stdout, stderr = ssh.exec_command(query)
            log = stdout.readlines()
            log = ''.join(log)
            if (GUI.CHANNELS[i][GUI.STORED_LOG] != log):
                delta.append(GUI.CHANNELS[i][GUI.CHANNEL_NAME])
                GUI.CHANNELS[i][GUI.STORED_LOG] = log
                if not os.path.exists(GUI.LOGS):
                    os.makedirs(GUI.LOGS)
                f = open(GUI.CHANNELS[i][GUI.LOCAL_LOG_PATH],'w')
                f.write(log)
                f.close()
        '''        
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
