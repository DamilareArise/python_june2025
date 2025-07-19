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


# Escape characters
# \n,  -> next line
# \r, -> return
# \t -> tab
# r -> raw string

# print("C:\\django_works\\june_django")
# print('It\'s mine')
# print(r"C:\django_works\june_django")


# PYTHON Collections / Array 
# 1. list
# 2. tuple
# 3. set 
# 4. dictionary

# list [] or list() -> ordered, allows duplicate values, It can indexed, it's changeable/mutable

myList = ["Apple", 'Mango', 'Tomato', 'Orange', 'Tomato']
numbers = [2, 4, 7, 5, 4, 1, 3, 6]
# print(myList[3])
# myList[3] = ""

# myList.reverse()
# myList.append("Cherry")
# myList.extend(("Cherry", 'Watermelon'))
# myList.pop(5)
# myList.remove('Mango')
# myList.sort()
# numbers.sort(reverse=False)
# print(myList.index('Tomato', 3, 4))
# print(numbers)
# print(myList)

# robust = myList + ("Cherry", 'Watermelon')
# print(robust)

# filter out item that ends with 'o' and pop them or put in a seperate list

item_with_o = []
item_without_o = []

for item in myList:
    result = item.endswith('o')
    if result:
        item_with_o.append(item)
    else:
        item_without_o.append(item)
        
# print(item_with_o)
# print(item_without_o)
        




# Python loops => for loop and while loop

# print(f"{myList[0]} is a fruit")
# print(f"{myList[1]} is a fruit")
# print(f"{myList[2]} is a fruit")
# print(f"{myList[3]} is a fruit")
# print(f"{myList[4]} is a fruit")

# x=1
# for fruit in myList:
#     print(f"{x}. {fruit} is a fruit")
    
#     if x == 3:
#         break
    
#     x+=1

# x=1
# for fruit in myList:
#     print(f"{x}. {fruit} is a fruit")

#     if x == 3:
#         break
    
#     x+=1
    
#     # else:
#     #     x+=1
#     #     continue
    

# name = "Damilare"
# print('my name is ' + str(name))
# print(f'my name is {name}')

# class-work 
#1. sort items into a list of fruits and vegies

# items = [
#     "apple-fruit",
#     "carrot-veg",
#     "banana-fruit",
#     "spinach-veg",
#     "grape-fruit",
#     "broccoli-veg",
#     "mango-fruit",
#     "lettuce-veg",
#     "orange-fruit",
#     "cucumber-veg",
#     "pineapple-fruit",
#     "pepper-veg",
#     "watermelon-fruit",
#     "tomato-veg",
#     "strawberry-fruit",
#     "onion-veg",
#     "blueberry-fruit",
#     "cabbage-veg",
#     "papaya-fruit",
#     "zucchini-veg"
# ]


# Assignment.
# Upgrade your cbt app to do the following;
# 1. ask a user how many students are about to take the test/quiz.
# 2. collect the name of each student into a list.
# 3. call each student one after the other to take their test.
# 4. print out all the students name and their score respectively


# items = ['Bag', 'Shoe']
# prices = [2000, 30000]

# for item, price in zip(items, prices):
#     print(f"{item} - #{price}")

# print(sum(prices))
# print(min(prices))
# print(max(prices))
# print(sum(prices)/len(prices))

# print("Welcome to ourQuiz App")

# no_students = int(input("How many students are taking the test: "))

# students = []
# scores = []
# print("Kindly register each student")
# for x in range(no_students):
#     student = input(f"Student name {x+1}: ").strip()
#     students.append(student)

# # print(students)

# for student in students:
#     print(f"\n{student} it's for your test")
    
#     questions = [
#         "1. What is the capital of Ghana a.) Togo  b.) Accra c.) Lagos",
#         "2. What is the capital of Nigeria a.) Accra b.) Lagos c.) Abuja"
#     ]
#     answers = [
#         'b',
#         'c'
#     ]
#     score = 0
#     for ques, ans in zip(questions, answers):
#         print(ques)
        
#         user = input('Answer: ').strip().lower()
#         if user == ans:
#             score += 5
            
#     scores.append(score)
    
# # print(students)
# # print(scores)

# print(f"""
# ==============================    
#         FINAL RESULT
 
# """)
# for student, score in zip(students, scores):
#     print(f"{student} --- {score}")
    
# # Student with the highest score
# ind = scores.index(max(scores))  
# print(f"{students[ind]} got the highiest score")

# ind = scores.index(min(scores))  
# print(f"{students[ind]} got the lowest score")

# print("\n==============================")




# TUPLE -> ordered, allows duplicate, immutable/unchangeable, indexed
myTP = ('ope', 'ola', 'femi', 'oyin', 'femi')

# A = ("Ope")
# B = ("ope",)
# print(type(B))

# print(myTP[0:3])

# myTP[0] = "Damilare"


# x = list(myTP)
# # print(x)
# x[0] = "Damilare"
# myTp = tuple(x)
# print(myTp)

# unpacking
# v, w, x, y, z= myTP
# *x,= myTP

# z, *y, x= myTP
# print(z)

# print(myTP.count('femi'))
# print(myTP.index("femi", 3))


items = ['Bag', 'Shoe']
prices = [2000, 30000]
# print(list(zip(items, prices)))

# for item in zip(items, prices):
#     print(item)


item_price = [
    ('Bag', 2000, 'Gucci'),
    ('Shoe', 3000, 'LV')
]



# for *x, in item_price:
#     print(x[2])