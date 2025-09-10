import os,shutil
from pathlib import Path

home = Path.cwd()

for folder_name,subfolders,filenames in os.walk(home):
    print('The curr folder is: ' + folder_name)

    for subfolder in subfolders:
        print('Subfodler of: ' + folder_name + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folder_name + ': '+ filename)
        # Rename file to uppercase:
        p = Path(folder_name)
        shutil.move(p / filename, p / filename.lower())
   
    print('')