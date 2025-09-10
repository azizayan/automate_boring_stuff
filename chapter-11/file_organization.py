from pathlib import Path
import shutil


h = Path.cwd()
print(h)
(h / 'spam').mkdir(exist_ok=True)
with open(h/'spam/file1.txt', 'w',encoding = 'utf-8') as file:
    file.write('hello')


print(shutil.copy(h / 'spam/file1.txt', h))

print(shutil.copy(h / 'spam/file1.txt', h/ 'spam/file2.txt'))


#print(shutil.copytree(h  / 'spam' , h /'spam_backup' )) 

( h/ 'spam2').mkdir()


print(shutil.move(h / 'spam/file1.txt', h / 'spam2/new_name.txt'))




