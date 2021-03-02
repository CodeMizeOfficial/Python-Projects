# pylint: disable = missing-docstring
# Imports
import os
import shutil

# Things to add-
# 1. Directory Tree

create__file = ["m fi", "fi m", "make file", "file make"]
create__folder = ["m fo", "fo m", "make folder", "folder make"]
remove__file = ["rem fi", "fi rem", "remove file", "file remove"]
remove__folder = ["rem fo", "fo rem", "remove folder", "folder remove"]
move__file = ["mo fi", "fi mo", "move file", "file move"]
move__folder = ["mo fo", "fo mo", "move folder", "folder move"]
del_folder__without_files = ["d fo", "fo d", "delete folder without files", "folder delete"]
exit__func = ["exit", "bye", "leave", "nothing"]
same_cmd__multi_times = ["sc mt", "mt sc", "same command multiple times", "mutiple commands"]

# <-- Add the list whenever more commands are added -->
all_cmd_entries = create__file + create__folder + remove__file + remove__folder + move__file
all_cmd_entries += move__folder + del_folder__without_files + exit__func

def create_file(need_output, file_name):
    try:
        file_open = open(f"{file_name}", "w+")
        file_open.write("")
        file_open.close()
        if need_output:
            print(f'{file_name} Made!')
    except FileNotFoundError:
        if need_output:
            print("No included file or folder found.")

def create_folder(need_output, folder_name):
    try:
        if not os.path.isdir(folder_name):
            os.mkdir(f'./{folder_name}/')
            if need_output:
                print(f'{folder_name} Made!')
        else:
            if need_output:
                print("Folder already exists.")
    except OSError as err:
        if need_output:
            print(err)

def remove_file(need_output, file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
        if need_output:
            print(f"{file_name} Removed!")
    else:
        if need_output:
            print(f"{file_name} doesn't exist!")

def remove_folder(need_output, folder_name):
    if os.path.isdir(folder_name):
        shutil.rmtree(folder_name)
        if need_output:
            print(f'{folder_name} Removed!')
    else:
        if need_output:
            print("Folder doesn't exist!")

def move_file(need_output, file_name, folder_name):
    if os.path.exists(file_name):
        file = open(f'{file_name}', 'r')
        contents = file.read()
        file.close()
    else:
        contents = ""
        if need_output:
            print("File not found.")
        return

    create_folder(False, folder_name)
    create_file(False, f'{folder_name}/{file_name}')
    file = open(f'{folder_name}/{file_name}', 'w+')
    file.write(contents)
    file.close()
    remove_file(False, file_name)
    if need_output:
        print(f"{file_name} has been moved to {folder_name}.")

def move_folder(need_output, folder_name, folder_name_to):
    files, contents = [], []
    if os.path.isdir(folder_name):
        create_folder(False, folder_name_to)
        if need_output:
            print('Files being Moved:')
        for file_n in os.scandir(folder_name):
            file_name = f'{file_n}'[11:-2]
            if need_output:
                print(file_name)
            files.append(file_name)
            file_open = open(f'{folder_name}/{file_name}', 'r')
            contents.append(file_open.read())
            file_open.close()

        remove_folder(False, folder_name)
        create_folder(False, f'{folder_name_to}/{folder_name}')

        for file_make in range(len(files)):
            file_open = open(f'{folder_name_to}/{folder_name}/{files[file_make]}', 'w+')
            file_open.write(contents[file_make])
            file_open.close()
        if need_output:
            print(f"\n{folder_name} is shifted to {folder_name_to}.")
    else:
        if need_output:
            print("File not found.")
        return

def delete_folder_without_files(need_output, folder_name):
    files, contents = [], []
    if need_output:
        print(f"\nPresent Files in {folder_name}:")
    for file_n in os.scandir(folder_name):
        file_name = f'{file_n}'[11:-2]
        if need_output:
            print(file_name)
        files.append(file_name)
        file_open = open(f'{folder_name}/{file_name}', 'r')
        contents.append(file_open.read())
        file_open.close()
    remove_folder(False, folder_name)
    for file_make in range(len(files)):
        file_open = open(f'{files[file_make]}', 'w+')
        file_open.write(contents[file_make])
        file_open.close()
    if need_output:
        print(f"\nAll the files present in {folder_name} are shifted to the present directory.")

def same_command__multiple_times(cmd, all_cmds = all_cmd_entries):
    cmd = cmd.lower().strip()
    times = 0
    run_ahead = True
    try:
        times = int(input('Enter the amount of times you want to run the command: '))
    except ValueError:
        print('The number of times you entered doesn\'t seem to be a number. Please try again.')
        run_ahead = False
    print()
    if cmd in all_cmds and bool(run_ahead):
        inner_execute(pre_cmd = cmd, times = times)

def inner_execute(pre_cmd = '', times = 0, all_cmd_entries = all_cmd_entries, same_cmd__multi_times = same_cmd__multi_times):
    command_execute, cmd_method, i = True, True, False
    if pre_cmd != '':
        command_execute = False
        cmd = pre_cmd
        cmd_method = times
        i = 0
    while i != cmd_method:
        if command_execute:
            cmd = input("Enter the Command: ")
        cmd = cmd.lower().strip()
        if cmd in all_cmd_entries[0]:
            create_file(True, input('Enter the File Name (With Extension): ').strip())
        elif cmd in all_cmd_entries[1]:
            create_folder(True, input("Enter the Folder Name: ").strip())
        elif cmd in all_cmd_entries[2]:
            remove_file(True, input("Enter the File Name (With Extension): ").strip())
        elif cmd in all_cmd_entries[3]:
            remove_folder(True, input("Enter the Folder Name: ").strip())
        elif cmd in all_cmd_entries[4]:
            file_name = input("Enter the File Name you want to move (With Extension): ").strip()
            folder_name = input("Enter the Folder Name you want to move the file to: ").strip()
            move_file(True, file_name, folder_name)
        elif cmd in all_cmd_entries[5]:
            folder_name = input("Enter the Folder Name you want to move: ").strip()
            folder_name_to = input("Enter the Folder Name you want to move the first folder to: ").strip()
            move_folder(True, folder_name, folder_name_to)
        elif cmd in all_cmd_entries[6]:
            delete_folder_without_files(True, input("Enter the Folder Name: ").strip())
        elif cmd in same_cmd__multi_times:
            command_m = input("Enter the Command you want to execute multipe times: ")
            same_command__multiple_times(True, command_m)
        elif cmd in all_cmd_entries[7]:
            break
        else:
            print("Please provide a valid command!")
        if isinstance(i, int):
            i += 1
        print()

INNER_EXECUTE = True
if INNER_EXECUTE: inner_execute()
