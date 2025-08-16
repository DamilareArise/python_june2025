# 1.  runtime error
# 2. compile type error


# number = int(input('Enter Number: '))
# print(number)

# recipe = ['apple', 'flour', 'sugar']
# recipe[10]


# print(name)

# try, except, else, and finally 
def calc():
    try:
        number1 = int(input('Enter Number: '))
        number2 = int(input('Enter Number: '))
        res = number1 / number2
        # name
    except ValueError as v:
        print('Invalid Input')
        
    except ZeroDivisionError as z:
        print('Cannot divide by zero')

    except Exception as e:
        print('Error: ', e)

    else:
        print('Your answer is', res)
        
    finally:
        # print('I am always executed if error occurs or not')
        user = input('Press 1 to exit or enter to continue operation: ')
        if user == '1':
            print('Exiting')
            exit()
        else:
            calc()

calc()

# number1 = int(input('Enter Number: '))
# number2 = int(input('Enter Number: '))
# res = number1 / number2