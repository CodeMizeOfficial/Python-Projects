# Imports
import os
import shutil

'''
Things to add-
1. Directory Tree
'''

create_file = ["m fi", "fi m", "make file", "file make"]
create_folder = ["m fo", "fo m", "make folder", "folder make"]
remove_file = ["rem fi", "fi rem", "remove file", "file remove"]
remove_folder = ["rem fo", "fo rem", "remove folder", "folder remove"]
move_file = ["mo fi", "fi mo", "move file", "file move"]
move_folder = ["mo fo", "fo mo", "move folder", "folder move"]
del_folder_without_files = ["d fo", "fo d", "delete folder without files", "folder delete"]
exit_func = ["exit", "bye", "leave", "nothing"]
same_cmd_mutli_times = ["sc mt", "mt sc", "same command multiple times", "mutiple commands"]

# <-- Add the list whenever more commands are added -->
all_cmd_entries = create_file + create_folder + remove_file + remove_folder + move_file
all_cmd_entries += move_folder + del_folder_without_files + exit_func

def create_file(need_output, file_name):
    try:
        file_open = open(f"{file_name}", "w+")
        file_open.write("")
        file_open.close()
        if need_output == True:
            print(f'{file_name} Made!')
    except FileNotFoundError:
        if need_output == True:
            print("No included file or folder found.")

def create_folder(need_output, folder_name):
    try:
        if not os.path.isdir(folder_name):
            os.mkdir(f'./{folder_name}/')
            if need_output == True:
                print(f'{folder_name} Made!')
        else:
            if need_output == True:
                print("Folder already exists.")
    except OSError as err:
        if need_output == True:
            print(err)

def remove_file(need_output, file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
        if need_output == True:
            print(f"{file_name} Removed!")
    else:
        if need_output == True:
            print(f"{file_name} doesn't exist!")

def remove_folder(need_output, folder_name):
    if os.path.isdir(folder_name):
        shutil.rmtree(folder_name)
        if need_output == True:
            print(f'{folder_name} Removed!')
    else:
        if need_output == True:
            print("Folder doesn't exist!")

def move_file(need_output, file_name, folder_name):
    if os.path.exists(file_name):
        file = open(f'{file_name}', 'r')
        contents = file.read()
        file.close()
    else:
        contents = ""
        if need_output == True:
            print("File not found.")
        return

    create_folder(False, folder_name)
    create_file(False, f'{folder_name}/{file_name}')
    file = open(f'{folder_name}/{file_name}', 'w+')
    file.write(contents)
    file.close()
    remove_file(False, file_name)
    if need_output == True:
        print(f"{file_name} has been moved to {folder_name}.")

def move_folder(need_output, folder_name, folder_name_to):
    files, contents = [], []
    if os.path.isdir(folder_name):
        create_folder(False, folder_name_to)
        if need_output == True:
            print('Files being Moved:')
        for file_n in os.scandir(folder_name):
            file_name = f'{file_n}'[11:-2]
            if need_output == True:
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
        if need_output == True:
            print(f"\n{folder_name} is shifted to {folder_name_to}.")
    else:
        if need_output == True:
            print("File not found.")
        return

def delete_folder_without_files(need_output, folder_name):
    files, contents = [], []
    if need_output == True:
        print(f"\nPresent Files in {folder_name}:")
    for file_n in os.scandir(folder_name):
        file_name = f'{file_n}'[11:-2]
        if need_output == True:
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
    if need_output == True:
        print(f"\nAll the files present in {folder_name} are shifted to the present directory.")

def same_command__multiple_times(need_output, cmd, all_cmds = all_cmd_entries):
    cmd = cmd.lower().strip()
    times = 0
    try:
        times = int(input('Enter the amount of times you want to run the command: '))
    except:
        print('The number of times you entered doesn\'t seem to be a number. Please try again.')
        return 'Command Not Executed!'
    print()
    if cmd in all_cmds:
        inner_execute(pre_cmd = cmd, times = times)

def inner_execute(pre_cmd = '', times = 0, create_file = create_file, create_folder = create_folder, remove_file = remove_file, remove_folder = remove_folder, move_file = move_file, move_folder = move_folder, del_folder_without_files = del_folder_without_files, same_cmd_mutli_times = same_cmd_mutli_times, exit_func = exit_func):
    command_execute, cmd_method, i = True, True, False
    if pre_cmd != '':
        command_execute = False
        cmd = pre_cmd
        cmd_method = times
        i = 0
    while i != cmd_method:
        if command_execute == True: cmd = input("Enter the Command: ")
        cmd = cmd.lower().strip()
        if cmd in create_file:
            create_file(True, input('Enter the File Name (With Extension): ').strip())
        elif cmd in create_folder:
            create_folder(True, input("Enter the Folder Name: ").strip())
        elif cmd in remove_file:
            remove_file(True, input("Enter the File Name (With Extension): ").strip())
        elif cmd in remove_folder:
            remove_folder(True, input("Enter the Folder Name: ").strip())
        elif cmd in move_file:
            move_file(True, input("Enter the File Name you want to move (With Extension): ").strip(), input("Enter the Folder Name you want to move the file to: ").strip())
        elif cmd in move_folder:
            move_folder(True, input("Enter the Folder Name you want to move: ").strip(), input("Enter the Folder Name you want to move the first folder to: ").strip())
        elif cmd in del_folder_without_files:
            delete_folder_without_files(True, input("Enter the Folder Name: ").strip())
        elif cmd in same_cmd_mutli_times:
            same_command__multiple_times(True, input("Enter the Command you want to execute multipe times: "))
        elif cmd in exit_func:
            break
        else:
            print("Please provide a valid command!")
        if type(i) == int: i += 1
        print()

inner_execute = True
if inner_execute == True: inner_execute()
