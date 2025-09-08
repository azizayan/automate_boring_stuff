from pathlib import Path


mac_dir = Path.home()

not_exist_dir = Path('This/Path/DoesNotExist')

file_path =( Path('/Users/azizemreayan/Desktop/automate_boring_stuff/bombgame_logfile.txt'))

print(mac_dir.is_dir())
print(mac_dir.exists())
print(not_exist_dir.exists())
print(file_path.is_dir())
print(file_path.is_file())