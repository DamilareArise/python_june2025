# print(45 + 23)
# print("Hello Everyone")  # print is an out command

'''
asldas ksdasdnla
jdasdlsad]
dakdasdasld
naksdsdasas
 
'''

# print(
#     '''
#         1. Create account
#         2. Sign in
#     '''
# )


# Python Variables

# name = "Temi"
# # print(name)

# print('Welcome to python class', name)

# firstName = "Joy" # camel case
# # print(firstName)
# first_name_of_the_student = "Joy" # snake case
# FirstName = "joy" # Pascal case

# I&you = 'Tolu and yemi'
# print(I&you)


"""
3major component for variable declaration
1. Variable name
2. Assignment operator
3. Value/content

Rules guiding variable name declaration
1. variable must be descriptive enough.
2. Variable name contains only aphalbet, numbers and underscore.
3. A variable doesn't start with a number
"""
# Types of variable declaration

# 1. single variable single value
name = 'joy'
# print(name)

# 2. single variable multiple Value
names = "Dami", "joy", "kenny"
# print(names)

# 3. multiple variable single value
x = y = z = 20
temi = dami = joy = 'student'
# print(temi, dami, joy)
temi = 'staff'
# print(temi, dami, joy)

x = x + 10
# print(x, y, z)

# print(y)
# 4. multiple variable multiple value
x, y, z = 10, 20, 30
# print(z)
# print(x)


# Python Datatypes

# 1. text type: string str()
# 2. number type:
    # i. Integer int() e.g 34, 6, 655
    # ii. Float float() e.g 3.4, 6.7, 0.9
    # iii. Complex complex() e.g 3+4j, 6+7j, 0+9j
# 3. Sequence type:
    # i. List list() e.g [1, 2, 3], ['a', 'b', 'c']
    # ii. Tuple tuple() e.g (1, 2, 3), ('a', 'b', 'c')
    # iii. Range range() e.g range(1, 10), range(1, 10, 2)
# 4. Boolean bool() e.g True, False
# 5. Set set() e.g {1, 2, 3}, {'a' , 'b', 'c'}
# 6. Mapping Type
#   Dictionary dict() e.g {'name': 'joy', 'age': 20}





name = "joy"
# print(type(name))
balance = 1999.9
num = 3 + 4j
# print(type(num))

# Concatenation -> joining two or more strings together

# print('Welcome to class ' + name)
# print('Your balance is #' + balance)
# print(type(balance))

names_of_student = ['joy', 'dami', 'kenny']
# print(names_of_student[-1])


# print(names_of_student)
# print(type(name_of_students))

numbers = range(1, 11, 3)
# print(type(numbers))
# print(list(numbers))

isMarried = bool(1)
# print(isMarried)

setA = {5,4,1,2,6,8,7,3}
setB = {'temi', 'dami', 'joy', 'femi', 'bolu', 'emmanuel'}
# print(setB)

students = [ 'Ade', 'Femi', 'lola' ]
# print(students[-1])

person = {
    "fullname": 'Adebayo Femi',
    "age": 25,
    "city": 'Lagos',
}

# print(person['fullname'])


# student1 = {
#     'name': 'kenny',
#     'course': 'Data analysis',
#     'state': 'Lagos State',
#     'subjects': ['excel', 'python', 'powerbi']
# }
# print(type(student))

students = [
    {
        'name': 'joy',
        'course': 'Data analysis'
    },
    
    {
        'name': 'dami',
        'course': 'Data Science'
    },
    
    {
        'name': 'kenny',
        'course': 'Data analysis'
    }
]
# print(students[0]['name'])

# print(students[0]['course'])
# print(students[1]['course'])
# print(students[2]['course'])

# for student in students:
#     print(student['course'])
  

# Python operators
# 1. Arithmetic Operator: +, -, *, /,
#  % -> Modulus, // -> Floor division, ** -> Raise to power
# 2. Assignment Operator: =, +=, -=, *=, /=, %=, //=, **=
# 3. comaparison operator: ==,!=, >, <, >=, <=
# 4. Logical Operator: and, or, not
# 5. Membership Operator: in, not in
# 6. Identity Operator: is, is not


fruits = ['mango', 'cashew', 'orange']
# print('Mango' in fruits)
# print('Mango' not in fruits)


numA = 5
numB = 5

# print(numA is not numB)


# val1 = 5
# val2 = 2

# val2 *= 2
# print(val1 % val2)
# print(val1 == val2)



# conditional statements
# if val1 == 5:  
#     print("I'm val1")

# else:
#     print("I'm not val1")

# old or even number checker
# value = int(input('Input your number: '))

# if value % 2 > 0:
#     print('Odd number')
# else:
#     print('Even Number')
    
# print(type(value))

# AND 
# A ____ B ____ Result
# T ____ T ____ T
# T ____ F ____ F
# F ____ T ____ F
# F ____ F ____ F

# OR
# A ____ B ____ Result
# T ____ T ____ T
# T ____ F ____ T
# F ____ T ____ T
# F ____ F ____ F

rice = True
beans = False
# print(rice and beans)

# if rice and beans:
#     print('Buy both rice and beans')
# elif rice:
#     print('Buy rice')
# elif beans:
#     print('Buy beans')
# else:
#     print("come back home")

# if rice or beans:
#     print('Buy rice or beans') 
# else:
#     print('come back home')

# value = int(input('Input your number: '))

# if value % 3 == 0 and value % 5 == 0:
#     print("FizzBuzz")
# elif value % 3 == 0:
#     print("Fizz")
# elif value % 5 == 0:
#     print("Buzz")
# else:
#     print(f"{value} is not a fizzbuzz")


# calculator 

# print("Alata calculator")
# val1 = float(input('Value 1: '))
# operator = input('choose operator ( *, /, +, - ): ')
# val2 = float(input('Value 2: '))

# if operator == '+':
#     print(val1 + val2)
# elif operator == '-':
#     print(val1 - val2)
# elif operator == '*':
#     print(val1 * val2)
# elif operator == '/':
#     print(val1 / val2)
    
# else:
#     print("Invalid operator")
    
# print('I dey ooo')


# nested if statement...
# rice = True
# beans = True
# bread = True
# chicken = True

# if rice and beans:
#     print('buy rice and beans')
# elif beans:
#     print('There is beans')
#     if bread:
#         print('buy beans and bread')
#     else:
#         print('I know you have beans but I need it with bread')
        
# elif rice:
#     print('There is rice')
#     if chicken:
#         print('buy rice and chicken')
#     else:
#         print('I can not eat rice without chicken')
    
# else:
#     print('Come back home')


# Ussd App

# print('Print Welcome to MyMTN')
# code = input('ussd code: ')
# if code == '*312#':
#     print("""
#     1. Buy Data
#     2. Check Balance
#     #. Exit
#     """)
#     choice = input('Choice: ')
#     if choice == "1":
#         print('You have successfully bought data')
        
#     elif choice == "2":
#         print('You have successfully checked your balance')
#     elif choice == "#":
#         print('Goodbye')
#         exit()
#     else:
#         print('Invalid choice')
    
# else:
#     print('Invalid code')

    



# Assignments
# Study python operators and conditional statements
# Build a simple calculator
# Design a grading system.
# Design a fizzbuzz app.
    # if the in divisible by 3 -> fizz
    # if the number is divisible by 5 -> buzz
    # if the number is divisible by both 3 and 5 -> fizzbuzz
# A simple ussd application 



# Python strings
# name = 'Boluwatife' # ['k', 'e', 'n', 'n', 'y', '', '']
# print(name[-1])
# fruits = ['Mango', 'Apple', 'Cashew'] # [ ['M', 'a', 'n', 'g', 'o'],  ['A', 'p', 'p', 'l', 'e']]
# print(fruits[0][0])

# cars = [['toyota', ['Ford']], ['Benz', ['Honda', 'Nissan']]]

# print(cars[1][1][3])
# print(cars[1][1][0])

# slicing
# print(name[0:3])

# print(fruits[:2])
# print(fruits[1:])
# print(fruits[-2: ])

# students = ['ayo', 'ade', 'lola', 'kemi', 'shola', 'bunmi']
# students

# print(len(students))
# print(students[2:4])

expression = 'Hello everyone, I am glad to be part of this family'
# print(len(expression))
# print(type(expression))
# print(expression.upper())
# print(expression.lower())
# print(len(expression.strip()))


# new_exp = expression.strip('&?/$')
# print(new_exp)

# print(expression.find('everyone'))
# print(expression.split())



# name = input('Your name: ')
# # print(name)
# ans = input('Are you a student? yes or no: ')
# if ans.lower() == 'yes': 
#     print(f'{name} is a student')
# else:
#     print(f'{name} is not a student')


# word counter
# text = input('Enter a text: ')
# print(len(text.strip().split()))


# 1. len 
# 2. strip
# 3. split


# Assigment
# 1. build a CBT application. a simple question and answer flow and after the test, display the result.