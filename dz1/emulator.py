import argparse
import socket
from vfs import VFS
from commands import execute_command
import os
import configparser

def run_shell(vfs, start_script):
    if start_script:
        with open(start_script, 'r') as script:
            for line in script:
                execute_command(vfs, line.strip())

    while True:
        prompt = f"{socket.gethostname()}:{vfs.current_path}$ "
        try:
            command = input(prompt).strip()
            if command == "exit":
                break
            execute_command(vfs, command)
        except EOFError:
            break


def main():
    config = configparser.ConfigParser()
    config.read('config.ini')

    archive_path = config['vfs']['archive']
    file_path = config['log']['file']
    start_script = config['startup']['script']

    if os.path.exists(file_path):
        os.remove(file_path)
    vfs = VFS(archive_path)
    run_shell(vfs, start_script)


if __name__ == "__main__":
    main()