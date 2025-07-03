def get_valid_number():
    while True:
        try:
            number = int(input('Enter a number: '))
            return number
        except ValueError:
            print('Error, you must enter a number')
number = get_valid_number()
def collatz(number):
    if number % 2 == 0:
        number = number // 2
    else:
        number = number*3 + 1
    print(number,end= ' ')
    return number
    
print(number, end = ' ')
while number != 1:
     number = collatz(number)

