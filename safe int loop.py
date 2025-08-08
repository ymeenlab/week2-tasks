#safe int input loop

while True:
    try:
        num = int(6)
        val = int(input('enter a number: '))
        if val == num:
            print('you entered valid number:', val)
            break
        else:
            print('you entered invalid number:', val)
            
    except ValueError:
        print('invalid format')