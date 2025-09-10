import zipfile,os
from pathlib import Path


def backup_to_zip(folder):

    folder = Path(folder)

    number = 1

    while True:

        zip_filename = Path(folder.parts[-1] + '_' + str(number) + '.zip')
        if not zip_filename.exists():
            break
        
        number = number + 1


        with zipfile.ZipFile(zip_filename,'w') as current_zip:
            current_zip.write('',compress_type=zipfile.ZIP_DEFLATED,compresslevel = 9)

