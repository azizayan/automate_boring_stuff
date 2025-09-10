from pathlib import Path
import shutil

h = (Path.cwd() / 'this_path')


h.mkdir()

print(h.is_dir())


shutil.rmtree(h)

print(h.is_dir())






#os.unlink(path ) to remove single file at path
#os.rmdir(path). to delete the folder at path(it must be empty)
# must be careful about deleting files so first make a dry run with print()