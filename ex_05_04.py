largest = None
smallest = None
while True :
    try :
        num = raw_input('Enter a number: ')
        if num == 'done' :
            break
        num = int(num)
        if largest is None or largest < num :
            largest = num
        elif smallest is None or  smallest > num:
            smallest = num
    except ValueError:
        print('invalid input')

print('Maximum is', largest)
print('Minimum is', smallest)
