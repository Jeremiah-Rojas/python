'''
This code is meant to help you find all types of files in a single directory. 
'''

import os
path = input("Enter your path: ")
extension = input("Enter an extension (.py | .sh | .log | .txt): ")
try:
    if os.path.isfile(path):
        print(f"The path {path} is a file.")
    else:
        all_files = os.listdir(path)
        if len(all_files) == 0:
            print("No files in this directory.")
        else:
            found = False
            for i in all_files:
                if i.endswith(extension):
                    print(i)
                    found = True
            if found != True:
                print(f"No {extension} files in this directory.")
except FileNotFoundError:
    print("Not a working directory")
except NotADirectoryError:
    print("Not a working directory.") 
