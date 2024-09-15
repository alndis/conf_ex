import argparse
import socket
from vfs import VFS
from commands import execute_command
import os

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
    parser = argparse.ArgumentParser(description="Virtual File System Shell Emulator")
    parser.add_argument("hostname", help="Hostname for prompt")
    parser.add_argument("vfs_zip", help="Path to the VFS zip file")
    parser.add_argument("start_script", help="Path to the startup script", nargs="?")
    args = parser.parse_args()
    file_path = 'D:/python/dz1/vfs_log.csv'
    if os.path.exists(file_path):
        os.remove(file_path)
    vfs = VFS(args.vfs_zip)
    run_shell(vfs, args.start_script)


if __name__ == "__main__":
    main()