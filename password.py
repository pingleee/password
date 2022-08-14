password = 'a123456'
i = 3
while i > 0:
    enter = input('Please enter the password: ')
    if password == enter:
        print('Success')
        break
    else:
        i = i - 1
        print('Wrong! You left', i, 'times.')