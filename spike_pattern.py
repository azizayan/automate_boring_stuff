import time, sys

try:
    while True:  # The main program loop
        # Draw lines with increasing length:
        for i in range(1, 9):# this means from 1 to 9, 9 not included
            print('-' * (i * i))
            time.sleep(0.1)

        # Draw lines with decreasing length:
        for i in range(7, 1, -1):# this means from 7 to 1, -1 dor decreasing
            print('-' * (i * i))
            time.sleep(0.1)
except KeyboardInterrupt:
    sys.exit()


#i confused that i am still seeing 1 line after the first 1 line but as loop ends starts that 1 is always the start of a new loop
#