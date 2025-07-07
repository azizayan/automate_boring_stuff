import random, string

def generate_password(length):
    char_list=""
    
    print('there will be lowercase letters in your password, lets pick what you want additionally')
    upper_case_check = input('Do you want uppercase chars(enter y for yes and n for no): ')
    digit_check = input('Do you want digits(enter y for yes and n for no): ')
    special_char_check = input('Do you want special characters (enter y for yes and n for no): ')

    lowercase_letters = string.ascii_lowercase # 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = string.ascii_uppercase # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = string.digits                   # '0123456789'
    symbols = string.punctuation             # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    while len(char_list) != length:
        char_list += (lowercase_letters[random.randint(0,len(lowercase_letters)-1)])
        
        if upper_case_check =='y':
            char_list +=(uppercase_letters[random.randint(0,len(uppercase_letters)-1)])
        if digit_check =='y':
            char_list += (digits[random.randint(0,len(digits)-1)])
        if special_char_check =='y':
            char_list += (symbols[random.randint(0,len(symbols)-1)])
        
    temp_list = list(char_list)

    random.shuffle(temp_list)

    password = "".join(temp_list)
    


    return password
    

    
def main():
    print('welcome to password generator.')
    length = int(input('Enter a length for your password'))

    print('we came here')
    password = generate_password(length)

    print('job done')
    print(password)
    return password

if __name__ == '__main__':
    main()

    



