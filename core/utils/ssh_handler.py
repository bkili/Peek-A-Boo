# core/utils/ssh_handler.py
import paramiko
from core.utils.formatter import printc

def create_ssh_client(host, port, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(hostname=host, port=port, username=username, password=password)
        return ssh

    except Exception as e:
        #printc(f"[ssh_handler] Connection failed : {e}", level="error")
        raise


def ssh_exec(ssh, command):
    stdin, stdout, stderr = ssh.exec_command(command)
    return stdin, stdout.read().decode(), stderr.read().decode()


def sftp_upload(ssh, local_path, remote_path):
    sftp = ssh.open_sftp()
    try:
        sftp.put(str(local_path), remote_path)
    finally:
        sftp.close()


def sftp_download(ssh, remote_path, local_path):
    sftp = ssh.open_sftp()
    try:
        sftp.get(remote_path, local_path)
    finally:
        sftp.close()
