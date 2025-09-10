import zipfile 


with open('file1.1.txt','w',encoding ='utf-8') as file_obj:
    file_obj.write('HELLO' * 1000)


with zipfile.ZipFile('example.zip','w') as example_zip:
    example_zip.write('file1.1.txt',compress_type=zipfile.ZIP_DEFLATED,compresslevel = 9)



example_zip = zipfile.ZipFile('example.zip')
print(example_zip.namelist())

example_zip.extract('file1.1.txt','Users/azizemreayan/Desktop/automate_boring_stuff/ziphere')



example_zip.close()