import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

guess_number= 0
if guess=='heads':
    guess_number= 1

toss = random.randint(0, 1)  # 0 is tails, 1 is heads
if toss == guess_number:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess_number:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')