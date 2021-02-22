import os, shutil

create_file = ["m fi", "fi m", "make file", "file make"]
create_folder = ["m fo", "fo m", "make folder", "folder make"]
remove_file = ["rem fi", "fi rem", "remove file", "file remove"]
remove_folder = ["rem fo", "fo rem", "remove folder", "folder remove"]
move_file = ["mo fi", "fi mo", "move file", "file move"]
move_folder = ["mo fo", "fo mo", "move folder", "folder move"]
del_folder_without_files = ["d fo", "fo d", "delete folder without files", "folder delete"]
exit_func = ["exit", "bye", "leave", "nothing"]
same_cmd_mutli_times = ["sc mt", "mt sc", "same command multiple times", "command multiple", "mutiple", "multiple command"]

# <-- Add the list whenever more commands are added -->
all_cmd_entries = create_file + create_folder + remove_file + remove_folder + move_file + move_folder + del_folder_without_files + exit_func

def Create_File(need_output, fileName):
    try:
        file_open = open(f"{fileName}", "w+")
        file_open.write("")
        file_open.close()
        if need_output == True:
            print(f'{fileName} Made!')
    except FileNotFoundError:
        if need_output == True:
            print("No included file or folder found.")

def Create_Folder(need_output, folderName):
    try:
        if not os.path.isdir(folderName):
            os.mkdir(f'./{folderName}/')
            if need_output == True:
                print(f'{folderName} Made!')
        else:
            if need_output == True:
                print("Folder already exists.")
    except OSError as err:
        if need_output == True:
            print(err)

def Remove_File(need_output, fileName):
    if os.path.exists(fileName):
        os.remove(fileName)
        if need_output == True:
            print(f"{fileName} Removed!")
    else:
        if need_output == True:
            print(f"{fileName} doesn't exist!")

def Remove_Folder(need_output, folderName):
    if os.path.isdir(folderName):
        shutil.rmtree(folderName)
        if need_output == True:
            print(f'{folderName} Removed!')
    else:
        if need_output == True:
            print("Folder doesn't exist!")

def Move_File(need_output, fileName, folderName):
    if os.path.exists(fileName):
        file = open(f'{fileName}', 'r')
        contents = file.read()
        file.close()
    else:
        contents = ""
        if need_output == True:
            print("File not found.")
        return

    Create_Folder(False, folderName)
    Create_File(False, f'{folderName}/{fileName}')
    file = open(f'{folderName}/{fileName}', 'w+')
    file.write(contents)
    file.close()
    Remove_File(False, fileName)
    if need_output == True:
        print(f"{fileName} has been moved to {folderName}.")

def Move_Folder(need_output, folderName, folderName_to):
    files, contents = [], []
    if os.path.isdir(folderName):
        Create_Folder(False, folderName_to)
        if need_output == True:
            print('Files being Moved:')
        for file_n in os.scandir(folderName):
            fileName = f'{file_n}'[11:-2]
            if need_output == True:
                print(fileName)
            files.append(fileName)
            file_open = open(f'{folderName}/{fileName}', 'r')
            contents.append(file_open.read())
            file_open.close()

        Remove_Folder(False, folderName)
        Create_Folder(False, f'{folderName_to}/{folderName}')
        
        for file_make in range(len(files)):
            file_open = open(f'{folderName_to}/{folderName}/{files[file_make]}', 'w+')
            file_open.write(contents[file_make])
            file_open.close()
        if need_output == True:
            print(f"\n{folderName} is shifted to {folderName_to}.")
    else:
        if need_output == True:
            print("File not found.")
        return

def Delete_Folder_Without_Files(need_output, folderName):
    files, contents = [], []
    if need_output == True:
        print(f"\nPresent Files in {folderName}:")
    for file_n in os.scandir(folderName):
        fileName = f'{file_n}'[11:-2]
        if need_output == True:
            print(fileName)
        files.append(fileName)
        file_open = open(f'{folderName}/{fileName}', 'r')
        contents.append(file_open.read())
        file_open.close()
    Remove_Folder(False, folderName)
    for file_make in range(len(files)):
        file_open = open(f'{files[file_make]}', 'w+')
        file_open.write(contents[file_make])
        file_open.close()
    if need_output == True:
        print(f"\nAll the files present in {folderName} are shifted to the present directory/folder.")

def Same_Command__Multiple_Times(need_output, cmd, all_cmds = all_cmd_entries):
    cmd = cmd.lower().strip()
    times = 0
    try:
        times = int(input('Enter the amount of times you want to run the command: '))
    except:
        print('The number of times you entered doesn\'t seem to be a number. Please try again.')
        return 'Command Not Executed!'
    print()
    if cmd in all_cmds:
        Inner_Execute(pre_cmd = cmd, times = times)

def Inner_Execute(pre_cmd = '', times = 0, create_file = create_file, create_folder = create_folder, remove_file = remove_file, remove_folder = remove_folder, move_file = move_file, move_folder = move_folder, del_folder_without_files = del_folder_without_files, same_cmd_mutli_times = same_cmd_mutli_times, exit_func = exit_func):
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
            Create_File(True, input('Enter the File Name (With Extension): ').strip())
        elif cmd in create_folder:
            Create_Folder(True, input("Enter the Folder Name: ").strip())
        elif cmd in remove_file:
            Remove_File(True, input("Enter the File Name (With Extension): ").strip())
        elif cmd in remove_folder:
            Remove_Folder(True, input("Enter the Folder Name: ").strip())
        elif cmd in move_file:
            Move_File(True, input("Enter the File Name you want to move (With Extension): ").strip(), input("Enter the Folder Name you want to move the file to: ").strip())
        elif cmd in move_folder:
            Move_Folder(True, input("Enter the Folder Name you want to move: ").strip(), input("Enter the Folder Name you want to move the first folder to: ").strip())
        elif cmd in del_folder_without_files:
            Delete_Folder_Without_Files(True, input("Enter the Folder Name: ").strip())
        elif cmd in same_cmd_mutli_times:
            Same_Command__Multiple_Times(True, input("Enter the Command you want to execute multipe times: "))
        elif cmd in exit_func:
            break
        else:
            print("Please provide a valid command!")
        if type(i) == int: i += 1
        print()

inner_execute = True
if inner_execute == True: Inner_Execute()