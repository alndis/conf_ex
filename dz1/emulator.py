import argparse
import socket
from vfs import VFS
from commands import execute_command
import os
import configparser
import tkinter as tk

class TerminalEmulator:
    def __init__(self, vfs, start_script):
        self.root = tk.Tk()
        self.root.title("Terminal Emulator")
        self.root.configure(background='black')  # Set background color to black

        self.text_area = tk.Text(self.root, bg='black',
                                 fg='green')  # Set text area background to black and text to green
        self.text_area.pack(fill="both", expand=True)

        self.entry_field = tk.Entry(self.root, bg='black',
                                    fg='green')  # Set input field background to black and text to green
        self.entry_field.pack(fill="x")

        self.send_button = tk.Button(self.root, text="Send", command=self.send_command)
        self.send_button.pack(side=tk.LEFT, padx=10, pady=10)  # Move send button to the left of the input field

        self.vfs = vfs
        self.start_script = start_script
        self.run_script()

    def run_script(self):
        if self.start_script:
            with open(self.start_script, 'r') as script:
                for line in script:
                    self.execute_command(line.strip())

    def send_command(self):
        command = self.entry_field.get()
        self.entry_field.delete(0, tk.END)
        output = self.execute_command(command)  # Call execute_command on self
        if output:
            self.text_area.insert(tk.END, output + '\n')
        else:
            self.text_area.insert(tk.END, command + '\n')

    def execute_command(self, command):
        if command == "exit":
            self.root.destroy()
        else:
            self.text_area.insert("end", f"{socket.gethostname()}:{self.vfs.current_path}$ {command}\n")
            output = execute_command(self.vfs, command)
            if output.startswith("Error") or output.startswith("cd: no such file or directory:"):
                self.text_area.insert("end", f"Error: {output}\n", "error")
                self.text_area.tag_config("error", foreground="red")
            else:
                self.text_area.insert("end", f"{output}\n")
            self.entry_field.delete(0, tk.END)

    def run(self):
        self.root.mainloop()

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
    emulator.run()

if __name__ == "__main__":
    main()
