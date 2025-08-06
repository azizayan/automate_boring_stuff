import pyperclip, re

phone_re = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  
    (\s|-|\.)?  
    (\d{3})  
    (\s|-|\.)  
    (\d{4})  
    (\s*(ext|x|ext\.)\s*(\d{2,5}))?  
    )''', re.VERBOSE)

email_re = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}')

text = pyperclip.paste()

phone_matches = [match[0] for match in phone_re.findall(text)]
email_matches = email_re.findall(text)


result = '\n'.join(phone_matches + email_matches)

pyperclip.copy(result)


print(result)

