import paramiko
from configuration import *
from communicator import *

class SSH():
    def connect_to_ssh():
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(
            paramiko.AutoAddPolicy())
        ssh.connect(Configuration.c['SSH IP'], 
                    username=Configuration.c['SSH User'], 
                    password=Configuration.c['SSH Password'])
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
