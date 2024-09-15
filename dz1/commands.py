def execute_command(vfs, command):
    parts = command.split()
    cmd = parts[0]

    if cmd == "ls":
        print("\n".join(vfs.list_files()))
        
    elif cmd == "cd":
        if parts[1] == '..' and vfs.current_path == vfs.fs_path:
            print("You cannot exit the archive directory.")
            return
        if len(parts) > 1:
            vfs.change_directory(parts[1])
        else:
            print("cd: missing operand")
    elif cmd == "quit":
        vfs.execute_quit()
    elif cmd == "uname":
        vfs.execute_uname()
    elif cmd == "rmdir":
        if len(parts) < 2:
            print("Usage: rmdir <directory>")
        else:
            vfs.execute_rmdir(vfs, parts[1])
    else:
        print(f"{cmd}: command not found")
