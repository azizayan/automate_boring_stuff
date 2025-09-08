from pathlib import Path

p = Path('spam.txt')
print(p.write_text('hello world 11231 times'))

print(p.read_text())

hello_file = open(Path.cwd() /'spam.txt', encoding='UTF-8')
hello_content = hello_file.read()
print(hello_content)



poem_file = open(Path.cwd()/'poem.txt','a', encoding='UTF-8')
poem_file.write('all poems are meaningless')
poem_file.close()
poem_file = open(Path.cwd()/'poem.txt', encoding='UTF-8')
print(poem_file.readlines())
poem_file.close




new_file = open(Path.cwd() / 'new_file.txt','w',encoding='UTF-8')
new_file.write('raining with thunders are best time to live')

new_file.close()
new_file = open(Path.cwd() / 'new_file.txt',encoding='UTF-8')
new_file_content = new_file.read()
new_file.close()
print(new_file_content)




with open('348thfile.txt','w', encoding='UTF-8') as file_obj:
    file_obj.write(' and also a coffee')
with open('348thfile.txt', encoding='UTF-8') as file_obj:
    content = file_obj.read()
print(content)





