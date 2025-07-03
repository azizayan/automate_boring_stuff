# functions can be considered as black boxes, so only knowing input and outputs will be enough, it is not necessary to understand
#every fucntions code, and because writing functions without global variables is encouraged, you usually don’t have to worry about the function’s code interacting with the rest of your program.
def spam():
    global eggs 
    eggs = 'spam'

def ham():
    eggs ='ham'

eggs = 'global'
spam()
print(eggs)