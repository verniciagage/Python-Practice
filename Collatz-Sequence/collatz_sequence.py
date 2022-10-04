is_number = False

def collatz(number):
    if number % 2 == 0:
        number = number // 2
        print(number)
        collatz(number)
    elif number == 1:
        print(number)    
    else:
        number = 3 * number + 1
        print(number)
        collatz(number)

number = input('Please input a number: ')
while is_number == False:
    try:
        int(number)
    except:
        number = input('You must enter an integer Please input a number: ')
    else:
        is_number = True
        number = int(number)
collatz(number)
