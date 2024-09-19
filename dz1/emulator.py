import os
import configparser
import socket
import threading
from locale import setlocale

from vfs import VFS
from commands import execute_command

class TerminalEmulator:
    def __init__(self, vfs, start_script):
        self.vfs = vfs
        self.start_script = start_script

    def run_script(self):
        if self.start_script:
            with open(self.start_script, 'r') as script:
                for line in script:
                    self.execute_command(line.strip())

    def execute_command(self, command):
        if command == "exit":
            return False
        else:
            output = execute_command(self.vfs, command)
            if output.startswith("Error") or output.startswith("cd: no such file or directory:"):
                print(f"Error: {output}")
            else:
                print(output)
            return True

    def run_terminal(self):
        os.system("title Virtual Terminal")
        if self.start_script:
            self.run_script()
        while True:
            command = input(f"{socket.gethostname()}:{self.vfs.current_path}$ ")
            if not self.execute_command(command):
                break

    def start(self):
        threading.Thread(target=self.run_terminal).start()

def main():
    config = configparser.ConfigParser()
    config.read('config.ini')

    archive_path = config['vfs']['archive']
    file_path = config['log']['file']
    start_script = config['startup']['script']

    if os.path.exists(file_path):
        os.remove(file_path)
    vfs = VFS(archive_path)
    emulator = TerminalEmulator(vfs, start_script)
    emulator.start()

if __name__ == "__main__":
    main()
