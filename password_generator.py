import random, string

def generate_password(length):
    char_list=[]
    password_list = []
    
    print('there will be lowercase letters in your password, lets pick what you want additionally')
    upper_case_check = input('Do you want uppercase chars(enter y for yes and n for no): ')
    digit_check = input('Do you want digits(enter y for yes and n for no): ')
    special_char_check = input('Do you want special characters (enter y for yes and n for no): ')

    lowercase_letters = string.ascii_lowercase # 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = string.ascii_uppercase # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = string.digits                   # '0123456789'
    symbols = string.punctuation             # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    try:
        if length > 0:
            char_list = lowercase_letters

            password_list.append(random.choice(lowercase_letters))

            
            if upper_case_check =='y':
                        if len(password_list) == length:
                            random.shuffle(password_list)
                            password = "".join(password_list)
                            return password
                        char_list += uppercase_letters
                        password_list.append(random.choice(uppercase_letters))
            if digit_check =='y':
                        if len(password_list) == length:
                            random.shuffle(password_list)
                            password = "".join(password_list)
                            return password
                        char_list += digits
                        password_list.append(random.choice(digits))
            if special_char_check =='y':
                        if len(password_list) == length:
                            random.shuffle(password_list)
                            password = "".join(password_list)
                            return password
                        char_list += symbols
                        password_list.append(random.choice(symbols))
                

            remaining_length = length - len(password_list)-1
            for i in range(remaining_length):
                password_list.append(random.choice(char_list))
                
            random.shuffle(password_list)

            password = "".join(password_list)

        return password
    except  IndexError:
          print('Your password length is not sufficient for your requests. Program will autogenerate yopu password ')
          
    

    
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

    



