import os
import csv
import zipfile
from pathlib import Path
import platform

class VFS:
    def __init__(self, zip_path):
        self.fs_path = r'\alndis\vfs'
        self.extract_zip(zip_path)
        self.current_path = self.fs_path
        self.log_file = 'vfs_log.csv'

    def extract_zip(self, zip_path):
        print(zip_path)
        with zipfile.ZipFile(zip_path, 'r') as zip:
            zip.extractall(self.fs_path)

    def list_files(self):
        with open(self.log_file, 'a', newline='') as csvfile:
            log_writer = csv.writer(csvfile)
            log_writer.writerow([f"ls"])
        return os.listdir(self.current_path)


    def change_directory(self, path):
        if path == '~':
            self.current_path = self.fs_path
        elif path == '/':
            self.current_path = self.fs_path
        elif path == '..':
            parent_path = os.path.dirname(self.current_path)
            self.current_path = parent_path
        elif path.count('.')>2:
            return f"cd: no such file or directory: {path}"
        elif path[0]=='/' and len(path)>1:
            return f"cd: no such file or directory: {path}"
        else:
            new_path = os.path.normpath(os.path.join(self.current_path, path))
            if os.path.isdir(new_path):
                self.current_path = new_path
            else:
                return f"cd: no such file or directory: {path}"
        with open(self.log_file, 'a', newline='') as csvfile:
            log_writer = csv.writer(csvfile)
            log_writer.writerow([f"cd {path}", self.current_path])
        return None

    def execute_rmdir(self, vfs, path):
        try:
            with open(self.log_file, 'a', newline='') as csvfile:
                log_writer = csv.writer(csvfile)
                log_writer.writerow([f"rmdir {path}", self.current_path])
            os.rmdir(os.path.join(vfs.current_path, path))
            return None
        except FileNotFoundError:
            return f"Directory '{path}' not found"
        except OSError as e:
            return f"Error removing directory '{path}': {e}"

    def read_file(self, file_path):
        with open(file_path, 'r') as f:
            return f.read()

    def execute_quit(self):
        with open(self.log_file, 'a', newline='') as csvfile:
            log_writer = csv.writer(csvfile)
            log_writer.writerow(["quit"])
        exit(0)

    def execute_uname(self):
        with open(self.log_file, 'a', newline='') as csvfile:
            log_writer = csv.writer(csvfile)
            log_writer.writerow([f"uname"])
        output = []
        output.append(f"System: {platform.system()}")
        output.append(f"Release: {platform.release()}")
        output.append(f"Version: {platform.version()}")
        output.append(f"Machine: {platform.machine()}")
        output.append(f"Processor: {platform.processor()}")
        return "\n".join(output)


