# OOP -> Object oriented programming
# Modularization


# class Human():
    
#     def __init__(self):
#         self.complexion = 'dark'
#         print('helloo')
    
#     def introduce(self, name):
#         print(f'My name is {name} I am {self.complexion} in complexion')
        
        

# ade = Human()
# print(ade.complexion)
# ade.introduce('Ade')

# tolu = Human()
# tolu.complexion = 'Light'
# print(tolu.complexion)


# print(type(ade))

# basket = list()
# basket.
# name = str()
# name.
# print(type(basket))




class Car():
    color = ''
    brand = ''   

    def __init__(self, color, brand):
        self.color = color
        self.brand = brand
        # print('Welcome..')
    
    
    def drive(self, speed):
        print(f'Driving a color {self.color} {self.brand} at {speed}km/hr')

    def reverse(self):
        print('Reverse mode activated')
        

# benz = Car('black', 'Benz')
# print(benz.color)
# benz.drive(100)
# benz.reverse()
# print(type(benz))


# CBT

class CBT():
    database = []
    school_name = ''
    
    def __init__(self, school):
        self.school_name = school
        
        
    def home(self):
        print(f''' 
        Welcome to {self.school_name}
        
        1. Register
        2. Student Portal
        3. Staff Portal
        4. exit 
        
        ''')
        user = input('Choice: ').strip()
        if user == '1':
            self.register()
        elif user == '2':
            self.studentPortal()
        elif user == '3':
            self.staffPortal()
        elif user == '4':
            exit()
        else:
            print('Invalid Option..')
            self.home()
        
    
    def register(self):
        student = {
            'name': input('Name: ').strip(),
            'email': input('Email: ').strip(),
            'password': input('Password: ').strip(),
            'score': 0
        }
        
        self.database.append(student) 
        print('Registration successful') 
        self.studentPortal()
        
        
    def studentPortal(self):
        # print(f"\n{self.database}")
        print('Student Portal') 
         
        email = input('Email: ').strip()
        password = input('Password: ')
        
        for student in self.database:
            if student['email'] == email and student['password'] == password:
                self.dashboard(student)
            
        print('Invalid credentials')
        
        self.home()
        
        
    def dashboard(self, student):
        print(f"welcome {student['name']} \n")
        
        print(f'''
            Welcome {student['name']}
            
            1. Take test
            2. Check result
            3. go back to home      
        ''')
        
        
    def staffPortal(self):
        pass     
        
        
# kennySch = CBT('Kenny\'s group of schools')
# dammieSch = CBT('Dammie\'s group of schools')
# dammieSch.home()


# kennySch.home()


# component of OOP
# 1. Inheritance
# 2. Encapsulation



