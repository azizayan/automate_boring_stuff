import zipfile,os
from pathlib import Path
import logging
logging.basicConfig(filename= 'backup_log_file.txt',level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')




def backup_to_zip(folder):

    folder = Path(folder)

    number = 100
    logging.debug('Start of program')
    while True:

        zip_filename = Path(folder.parts[-1] + '_' + str(number) + '.zip')
        if not zip_filename.exists():
            logging.debug(f'There is no file as {zip_filename}')
            break
        
        number = number + 1

        #create the zip file
    logging.debug(f'Creating{zip_filename}')
    try:
        backup_zip = zipfile.ZipFile(zip_filename,'w')
        logging.debug(f'Zip file created as {zip_filename}')
    except Exception as e:
        print(f'Error: Could not create the ZIP file. {e}')
        return
        
       # walk the dir 
    logging.debug('Starting backup')
    for folder_name, subfolders, filenames in os.walk(folder):
        folder_name = Path(folder_name)
        logging.debug(f'Adding files from {folder_name}')
        for filename in filenames:
            file_path = folder_name / filename
                
            try:
                rel_path = file_path.relative_to(folder.parent)
                backup_zip.write(rel_path)
            except Exception as e:
                print(f' Error: Could not add {file_path}')
                
    backup_zip.close()
    logging.debug(f'Backup created succesfully {zip_filename}')



if __name__ == '__main__':
    folder_to_backup = Path.cwd()
    for i in range(1):
        backup_to_zip(folder_to_backup)
