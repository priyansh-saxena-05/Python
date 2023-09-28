# Following Code Comprises of letting you connect your local machine to server using ssh conectivity using a pem file.

import paramiko
import os


def download_files_from_remote(remote_dir, local_dir, hostname, username, key_filename):
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname, username=username, key_filename=key_filename)
        sftp = ssh_client.open_sftp()
        remote_files = sftp.listdir(remote_dir)
        os.makedirs(local_dir, exist_ok=True)
        for remote_file in remote_files:
            remote_path = os.path.join(remote_dir, remote_file)
            local_path = os.path.join(local_dir, remote_file)
            sftp.get(remote_path, local_path)
        sftp.close()
        ssh_client.close()
        print(f"All files from '{remote_dir}' downloaded to '{local_dir}'")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


# Example usage:
if __name__ == "__main__":
    remote_dir = '/path/to/server/folder/'
    local_dir = '/local/folder/path/where/to/save'
    hostname = '123.140.70.144' Ip address
    username = 'user'
    key_filename = 'path/server.pem'
    download_files_from_remote(remote_dir, local_dir, hostname, username, key_filename)
