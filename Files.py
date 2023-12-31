file = open("file.txt",'r')
content = file.read()
print(content)

# Another way
file_path = "file.txt"
with open(file_path,'r') as file:
    content = file.read()
    print(content)

# Reads a single line from the file
with open(file_path,'r') as file:
    content = file.readline()
    print(content)

# Reads all lines of the file and returns a list
with open(file_path,'r') as file:
    content = file.readlines()
    print(content)

# New content appended to the text file
with open(file_path,'a') as file:
    append = file.write("\nThis is a appended content")

# If file is opened in 'w' mode and anything is written, the previous data is overwritten but in appened mode new data is added at the last
with open("text_file_2.txt",'w') as file:
    content = file.write("This is the content in a new file")

# Ideal method to open a file (try except block)
try:
    with open("non_existing_file.txt",'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found...")
except PermissionError:
    print("Permission not granted...")

# For advanced file handling OS and SHUTIL moduls are used