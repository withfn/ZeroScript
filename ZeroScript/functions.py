#Functions of the project

import os

source_dir = ""
source_files = []
file_dir = ''
data = ''

#Print files
def print_files():
    i = 1
    print("Archives: ")
    for file in source_files:
        print(f'[{i}] {file}')
        i += 1
    print("[*] Select all files")

#Open source
def open_source(source):
    with os.scandir(source) as entries:
        for entry in entries:
            if "REP" == entry.name[:3]:
                source_files.append(entry.name)


#Zero input
def zero_input():
    for i in range(len(data)):
        data[i] = data[i].strip()
        if len(data[i]) == 30:
            data[i] = data[i][:-4] + '000000000000' + data[i][-4:]
    return data

#Open File
def open_file(file):
    global data
    global source_files
    global file_dir
    
    file_dir = source_files[int(file) - 1]
    
    file_dir = f'{source_dir}/{file_dir}'
    f = open(file_dir, "r")
    data = f.read()
    data = data.split('\n')
    data = zero_input()
    f.close()

#Save file
def save_file():
    global data
    global file_dir
    global source_dir
    
    formatted_data = '\n'.join(data)
    save_path = source_dir
    file_name = f'{file_dir[:-4]}' + '-formatted.txt' 
    complete_path = os.path.join(save_path, file_name)
    
    f = open(complete_path, "w")
    f.write(formatted_data)
    f.close()
