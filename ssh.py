import paramiko
from config import *
#from communicator import *

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
        query = 'cat ' + log_path
        stdin, stdout, stderr = ssh.exec_command(query)
        log = stdout.readlines()
        log = ''.join(log)
        return log
        #if stdin != "null"
        #    return stdin
        #else
        #    return False

    def write_to_log(ssh,log_path,log):
        query = "echo '" + log + "' >> " + log_path
        ssh.exec_command(query)
        #Communicator.update_channel()
    
    #def connect_to_chat_server(ssh)
    #    query = "python client.py localhost 5000"
	#ssh.exec_command(query) 
