import logging
logging.basicConfig(filename= 'mylogfile.txt',level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
logging.disable()# disable all levels of Logs
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(' + str(n) + ')')
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(' + str(n) + ')')
    return total

print(factorial(5))
logging.debug('End of program')