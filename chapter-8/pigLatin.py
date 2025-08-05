"""
Pig latin is a silly made-up language that alters English words.
If a word begins with a vowel, the word yay is added to the end
of it. If a word begins with a consonant or consonant cluster
(like ch or gr), that consonant or consonant cluster is
moved to the end of the word and followed by ay.
"""


print('Enter a message to translate into pig latin: ')
message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

translated_text=[]

for word in message.split():
    prefix_non_letters = ''
    
    while(len(word) > 0 and not word[0].isalpha):
        prefix_non_letters += word[0]
        word = word[1:]
    
    if len(word) == 0:
        translated_text.append(prefix_non_letters)
        continue

    suffix_non_letters = ''
    while not word[-1].isalpha():
        suffix_non_letters = word[-1] +  suffix_non_letters
        word = word[:-1]
    
    was_upper = word.isupper()
    was_title = word.istitle()

    word = word.lower()

    prefix_consonants =''
    while len(word) > 0 and not word[0] in VOWELS:
        prefix_consonants += word[0]
        word = word[1:]


    if prefix_consonants != '':
        word += prefix_consonants +'ay'
    else:
        word += 'yay'
    

    if was_upper:
        word = word.upper()
    if was_title:
        word = word.title()
    
    translated_text.append(prefix_non_letters + word + suffix_non_letters)

print(' '.join(translated_text))




        


    

