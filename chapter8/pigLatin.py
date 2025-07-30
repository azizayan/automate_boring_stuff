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
    prefix_non_letters += word[0]
    
    while(len(word) > 0 and not word[0].isalpha):
        prefix_non_letters += word[0]
        word = word[1:]
    
    if len(word) == 0:
        translated_text.append(prefix_non_letters)
        


    

