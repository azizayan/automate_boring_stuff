import pyperclip


message = 'Hi Alex\'s dog'
# \t = tab
# \n = newline
# \\ = backslash


print(message)


print(r'The file is in C:\Aziz\Desktop')



print('''
      THIS
      IS
      A'
      MULTI-LINE
      STRING

''')


#below is a multiline comment
"""ADADADADA
ADADSASDADASD
ADS
ADS
AS
D
AD
A
SD
ASD
A
SDADASDA
DA"""


print("""
However this 
is also printed.
""")


print('Hello' in 'Hello, world!')
print('Hello' not in  'Hello, world!')


name = 'emre'
age = 20
print(f'My name is {name} and I am {age} years old')


print('ABC'.join(['Cats','bats','rats','dads']))

print('My name is Simon'.split('m'))


print('hello'.rjust(20))
print('hello'.ljust(20) + 'aaaa')

print('hello'.center(20,'*'))



hello_message = '     Hello     '

print(hello_message.rstrip())

"""
Passing strip() the argument 'ampS'
 will tell it to strip occurrences 
 of a, m, p, and S from the ends of 
 the string stored in spam. The order 
 of the characters in the string passed 
 to strip() doesn't matter: strip('ampS') 
 will do the same thing as strip('mapS') 
 or strip('Spam').
"""

print(ord('A'))


pyperclip.copy('aaaaa')

text = pyperclip.paste()

print(text.rjust(10))
