import functions

#Open the file's path
active = 1
while active == 1:
    try:
        functions.source_dir = str(input("Enter the path: ")).replace("\\", "\\\\")
        functions.open_source(functions.source_dir)
        active = 0
    except FileNotFoundError:
        print("Path not found")
#print all files
i = 1
print("Archives: ")
for file in functions.source_files:
    print(f'[{i}] {file}')
    i += 1
print("[*] Select all files")


file = input("Select a file: ")

active = 1
while active == 1:
    if file == '*':
        for archive in range(len(functions.source_files)):
            functions.file_dir = archive + 1
            functions.open_file(functions.file_dir)    
            functions.save_file()
        active = 0

    else:
        try:
            functions.file_dir = file
            functions.open_file(functions.file_dir)    
            functions.save_file()
            active = 0
        except ValueError:
            file = input("Enter a numeric value inside the range or * to select all files: ")
print("Done!")
exit = input("Press enter to exit...")