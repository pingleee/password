password = 'a123456'
t = 0
while True:
    enter = input('Please enter the password: ')
    if password == enter:
        print('Success')
    else:
        while t < 3:
            print('Wrong! You left', 2 - t, 'times.')
            t = t + 1
            break