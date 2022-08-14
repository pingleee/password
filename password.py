password = 'a123456'
i = 3
while i > 0:
    i = i - 1
    enter = input('Please enter the password: ')
    if password == enter:
        print('Success')
        break
    else:
        print('Wrong!')
        if i > 0:
            print('You left', i, 'times.')
        else:
            print('Lock you account forever.')