import platform
def execute_command(vfs, command):
    parts = command.split()
    cmd = parts[0]

    if cmd == "ls":
        return "\n".join(vfs.list_files())

    elif cmd == "cd":
        if parts[1] == '..' and vfs.current_path == vfs.fs_path:
            return "You cannot exit the archive directory."
        if len(parts) > 1:
            output = vfs.change_directory(parts[1])
            if output:
                return output
            else:
                return f"Changed directory to {vfs.current_path}"
        else:
            return "cd: missing operand"

    elif cmd == "quit":
        vfs.execute_quit()
        return "Goodbye!"

    elif cmd == "uname":
        return vfs.execute_uname()

    elif cmd == "rmdir":
        if len(parts) < 2:
            return "Usage: rmdir <directory>"
        else:
            output = vfs.execute_rmdir(vfs, parts[1])
            if output:
                return output
            else:
                return f"Removed directory {parts[1]}"

    else:
        return f"{cmd}: command not found"
