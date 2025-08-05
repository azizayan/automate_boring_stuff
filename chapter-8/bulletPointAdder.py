""" copy this text:
Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars
"""
import pyperclip
text = pyperclip.paste()

lines = text.split('\n')

for i in range(len(lines)):
    lines[i] = '* ' + lines[i]



text ='\n'.join(lines)
pyperclip.copy(text)
print(text)
