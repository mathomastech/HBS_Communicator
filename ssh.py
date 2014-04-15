import paramiko
from config import Config

class SSH():
    def connect_to_ssh():
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(
            paramiko.AutoAddPolicy())
        ssh.connect(Config.c['SSH IP'], 
                    username=Config.c['SSH User'], 
                    password=Config.c['SSH Password'])
	#SSH.connect_to_chat_server(ssh)
        return ssh

    def get_log(ssh,log_path):
        # Get log for current channel and return to communicator.
        query = 'cat ' + log_path
        stdin, stdout, stderr = ssh.exec_command(query)
        log = stdout.readlines()
        log = ''.join(log)

        return log


    def get_logs(ssh, LOCAL_LOGS, REMOTE_LOGS):
        # Get remote logs for all channels and return to communicator.
        keys = [k for k,v in Config.LOG_PATHS.items()]
        for i in range (0, len(keys)):
            for j in range (0, len(keys)):
                if(keys[i] == REMOTE_LOGS[j][0]):
                    query = 'cat ' + Config.LOG_PATHS[keys[i]]
                    stdin, stdout, stderr = ssh.exec_command(query)
                    log = stdout.readlines()
                    log = ''.join(log)
                    REMOTE_LOGS[j][1] = log
                    #break
                    
        print(REMOTE_LOGS)
        return LOCAL_LOGS, REMOTE_LOGS


    def write_to_log(ssh,log_path,log):
        # Get and parse timestamp from server
        stdin,stdout,stderr = ssh.exec_command('date +"%H:%M:%S |"')
        timestamp = stdout.readlines()
        timestamp = timestamp[0]
        timestamp = timestamp.rstrip()

        # Write timestamp and log to appropriate file
        query = 'echo "' + timestamp + ' ' + log + '" >> ' + log_path
        ssh.exec_command(query)
    
