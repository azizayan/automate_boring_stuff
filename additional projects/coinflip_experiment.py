import random
number_of_streaks = 0
for experiment_number in range(10000): 

    pass

print('Chance of streak: %s%%' % (number_of_streaks / 100))


def hundred_flips():
    str = " "
    for i in range(100):
        number = random.choice([0,1])
        if number == 0:
            str+= 'H'
        else:
            str += 'T'
    
    