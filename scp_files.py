import traceback
import subprocess
import os

from constants.constant import SOURCE_HOST
from utils.logger_util import LoggerUtil

error_logger = LoggerUtil().error_logger()
common_logger = LoggerUtil().common_logger()

def scp_move_file(destination_path):
    try:
        destination_dir = os.path.dirname(destination_path)
        ssh_command = [
            'ssh',
            SOURCE_HOST,
            f'mkdir -p {destination_dir}'
        ]
        common_logger.info(" ".join(ssh_command))
        scp_command = [
            'scp',
            f'{destination_path}',
            f'{SOURCE_HOST}:{destination_path}'
        ]
        common_logger.info(" ".join(scp_command))
        subprocess.run(ssh_command, check=True)
        subprocess.run(scp_command, check=True)
        common_logger.info(f"File '{destination_path}' moved to '{destination_path}'")
    except subprocess.CalledProcessError as e:
        error_logger.error(e)
        error_logger.error(traceback.format_exc())
      
def scp_get_file(destination_path, host):
    try:
        try:
            destination_dir = os.path.dirname(destination_path)
            subprocess.run(["mkdir", "-p", f"{destination_dir}"], check=True)
        except Exception as e:
            error_logger.error(e)
            error_logger.error(traceback.format_exc())
        scp_command = [
            'scp',
            f'{host}:{destination_path}',
            f'{destination_path}'
        ]
        common_logger.info(" ".join(scp_command))
        subprocess.run(scp_command, check=True)
        common_logger.info(f"File '{destination_path}' moved to '{destination_path}'")
    except subprocess.CalledProcessError as e:
        error_logger.error(e)
        error_logger.error(traceback.format_exc())
      
def scp_move_folder(destination_path):
    try:
        destination_dir = os.path.dirname(destination_path)
        ssh_command = [
            'ssh',
            SOURCE_HOST,
            f'mkdir -p {destination_dir}'
        ]
        common_logger.info(" ".join(ssh_command))
        scp_command = [
            'scp',
            '-r',
            f'{destination_path}',
            f'{SOURCE_HOST}:{destination_dir}/'
        ]
        common_logger.info(" ".join(scp_command))
        subprocess.run(ssh_command, check=True)
        subprocess.run(scp_command, check=True)
        common_logger.info(f"Folder '{destination_path}' moved to '{destination_dir}'")
    except subprocess.CalledProcessError as e:
        error_logger.error(e)
        error_logger.error(traceback.format_exc())
      
def ssh_rm_file(destination_path):
    try:
        ssh_command = [
            'ssh',
            SOURCE_HOST,
            f'rm {destination_path}'
        ]
        common_logger.info(" ".join(ssh_command))
        subprocess.run(ssh_command, check=True)
        common_logger.info(f"File '{destination_path}' removed from '{SOURCE_HOST}'")
    except subprocess.CalledProcessError as e:
        error_logger.error(e)
        error_logger.error(traceback.format_exc())
      
def ssh_rm_folder(destination_path):
    try:
        ssh_command = [
            'ssh',
            SOURCE_HOST,
            f'rm -r {destination_path}'
        ]
        common_logger.info(" ".join(ssh_command))
        subprocess.run(ssh_command, check=True)
        common_logger.info(f"File '{destination_path}' removed from '{SOURCE_HOST}'")
    except subprocess.CalledProcessError as e:
        error_logger.error(e)
        error_logger.error(traceback.format_exc())
