def spam(divide_by):
    try:
        return 42/ divide_by
    except ZeroDivisionError:
        print('Error: division by zero is not possible.')
print(spam(2))
print(spam(1))
print(spam(0))
print(spam(3))


print(" ")
def spam_2(divide_by):
    return 42/ divide_by

try:
    print(spam_2(2))
    print(spam_2(12))
    print(spam_2(0))
    print(spam_2(1))
except  ZeroDivisionError:
    print('error')
except  ZeroDivisionError:
    print('aaaaa')
    


print(type(None))