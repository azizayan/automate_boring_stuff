import re
phone_re = re.compile(r'(\d\d\d) (\d\d\d-\d\d\d\d)')
mo = phone_re.search('My number is 415 555-4242.')

area_code, main_number = mo.groups()
print(area_code)

print(mo.group(2))


pattern = re.compile(r'Cat(erpilar|astrophe|ch|egory)')
print(pattern.findall('Catch Caterpilar to prevent a Catastrophe of Category.'))


pattern2 = re.compile(r'[a-yA-Z09]')
result_list = pattern2.findall('You think the ** devil has horns__ So did I, But %% I was wrong..')
result_string = "".join(result_list)
print(result_string)


pattern3 = re.compile(r'\w+')
print(pattern3.findall('Sinéad OConnor'))

pattern4 = re.compile(r'42!?')
print(pattern4.search('42!'))
print(pattern4.search('42'))
print(pattern4.search('4!'))


pattern5 = re.compile('Eggs( and spam)*')
print(pattern5.search('Eggs'))
print(pattern5.search('Eggs and spam'))
print(pattern5.search('Eggs and spam and spam'))


name_pattern = re.compile(r'First Name: (.*) Last Name: (.*)')
name_match = (name_pattern.search('First Name: Aziz Last Name: Ayan'))
print(name_match.group(1))
print(name_match.group(2))


newline_pattern = re.compile('.*', re.DOTALL)
newline_match = newline_pattern.search('Serve the public trust.\nProtect the innocent. \nUphold the law.')
print(newline_match.group())

agent_pattern = re.compile(r'Agent \w+')
print(agent_pattern.sub('CENSORED', 'Agent Alice contacted Agent Bob'))

agent_pattern = re.compile(r'Agent (\w)\w*')
print(agent_pattern.sub(r'\1****', 'Agent Alice contacted Agent Bob.'))