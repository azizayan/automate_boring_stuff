birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    birthday_key = input('Enter a name(blank to quit): ')
    if birthday_key =='':
        break

    if birthday_key in birthdays:
        print(birthdays[birthday_key] + ' is the birthday of ' + birthday_key)
    else:
        print('There is no birthday info for this friend. That means new friend!')
        new_bday = input('What is their birthday? ')
        birthdays[birthday_key] = new_bday
        print('Birthday added.')
# add database to here, very basic app idea, key senesivity etc should be added


