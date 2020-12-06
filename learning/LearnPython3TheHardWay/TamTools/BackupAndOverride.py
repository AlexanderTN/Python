# This script is to copy 

# Rename the up-coming override files (put a '.bak' string at the end of the file extension)
# Then copy the new files to replace the renamed files

# Algorithm
# 1. Get files list (of the new files)
# 2. Iterate over all the files in the folder
#     If the name matchs => Rename the file in the folder
# 3. Copy the new files to the old file
import os
from pathlib import Path
# with open("test.txt", 'r+') as f:
#     #print(f.read())
#     f.seek(0)
#     data = 'Some data to write into the file xxx'
#     f.write(data)
#     f.flush()
#     f.seek(0)
#     #print(f.read())

# with os.scandir('.') as dir_contents:
#     for entry in dir_contents:
#         info = entry.stat()
#         #print(info.st_mtime)

# currentPath = Path('.')

# for dirpath, dirnames, files in os.walk('.'): # os walk is the only way to walk through files in
#     print(f"Found directory: {dirpath}")
#     for file_name in files:
#         print(file_name)

#SRC_DIR = input("Source Directory (for example: C:\FileToCopy\):")
#DES_DIR = input("Destination Directory ( for example C:\DestinationCopy\):")

#SRC_DIR = 'K:\TamCloud\OneDrive\TrainingProgram_byTam3\ProductionTraining\Language\Python\LearnPythonTheHardway\Exercises_LearnPython3TheHardway\TamTools\TestFolder\src'
#DES_DIR = 'K:\TamCloud\OneDrive\TrainingProgram_byTam3\ProductionTraining\Language\Python\LearnPythonTheHardway\Exercises_LearnPython3TheHardway\TamTools\TestFolder\Test2'

SRC_DIR = 'K:\Games\Games\steamapps\common\eFootball PES 2020\Backup'
DES_DIR = 'K:\Games\Games\steamapps\common\eFootball PES 2020'
src_path = Path(SRC_DIR)
list_src = list(src_path.glob('**\*.*'))
print(list_src)

dst_path = Path(DES_DIR)
list_des = list(dst_path.glob('**\*.*'))
print(list_des)
for path_src in list_src:
    head_src,tail_src = os.path.split(path_src)
    
    for path_des in list_des:
        head_des, tail_des = os.path.split(path_des)
        if tail_des == tail_src:
            path_des.rename(str(path_des.resolve()) + '.beo')
    
            
    
        










