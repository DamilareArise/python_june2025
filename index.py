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

student1 = {
    'name': 'kenny',
    'course': 'Data analysis',
    'state': 'Lagos State',
    'subjects': ['excel', 'python', 'powerbi']
}
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

val1 = 0
val2 = 2
# print(val1 ** val2)
# val1 -= 10 # val1 = val1 + 10
# print(val1)

# print(val1 != val2)

# conditional statements
if val1 == 5:
    print('yes')
else:
    print('no')

# Assignments
# Study python operators and conditional statements
# Build a simple calculator
