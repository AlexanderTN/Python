# This script is to copy 

# Rename the up-coming override files (put a '.bak' string at the end of the file extension)
# Then copy the new files to replace the renamed files

# Algorithm
# 1. Get files list (of the new files)
# 2. Iterate over all the files in the folder
#     If the name matchs => Rename the file in the folder
# 3. Copy the new files to the old file
import os
with open("test.txt", 'r+') as f:
    #print(f.read())
    f.seek(0)
    data = 'Some data to write into the file xxx'
    f.write(data)
    f.flush()
    f.seek(0)
    #print(f.read())

with os.scandir('.') as dir_contents:
    for entry in dir_contents:
        info = entry.stat()
        print(info.st_mtime)

