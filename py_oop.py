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


# OOP - Object oriented programming
# object -> anything that has a property and can perform a function
# class  -> a blueprint of an object, we define the properties and functions that the object will have here

# name = str()
# name2 = str()
# basket = ['z', 'y']

class USSD:
    # brandname = 'MTN' # public property
    
    __brandname = None
    __balance = 0 # private property

    
    def __init__(self, brand):  # class constructor
        self.__brandname = brand
        print(f'Hello! welcome to {self.__brandname}')
        

    
    def get_balance(self):
       print(f"Your balance is {self.__balance}")
       self.dashboard()
    
    def get_brandname(self):
        return self.__brandname
    
    
    def home(self):
        ussd = input('USSD: ')
        while ussd != '*312#':
            user = input('Invalid ussd code! \nPress enter to Try again or 1 to exit: ').strip()
            if user == '1':
                exit()
                
            ussd = input('USSD: ')
            
        else:
  
            self.dashboard() 
            
    def dashboard(self):
        print("""
        1. Data plan
        2. Check balance
        3. Recharge
        #. exit   
        """)
        
        user = input('Choice: ').strip()
        if user == '1':
            self.dataPlan()
        elif user == '2':
            self.get_balance()
        elif user == '3':
            self.recharge()
        elif user == '#':
            exit()
        else: 
            print('Invalid input\n')
            self.dashboard()
    
    def recharge(self):
        amount = float(input('Amount: '))
        if amount > 0:
            self.__balance += amount
            print(f'Your recharge of {amount} is successfull. Your balance is {self.__balance}')
        else:
            print('Invalid amount.')
            
        self.dashboard()
            
    def dataPlan(self):
        print('''
            1. #200 for 500mb
            2. #1000 for 5gb
            #. go to dashboard
            ''')
        
        user = input('Choice: ')
        if user == '1':
            if self.__balance >= 200:
                self.__balance -= 200
                print('You have successfully purchase 500mb')
            else:
                print('Insufficient fund')
                
            self.dashboard()
            
        elif user == '2':
            if self.__balance >= 1000:
                self.__balance -= 1000
                print('You have successfully purchase 5gb')
            else:
                print('Insufficient fund')
                
            self.dashboard()
            
        elif user == '#':
            self.dashboard()
            
        else:
            print('Invalid choice..')
            self.dataPlan()

# mtn = USSD(brand='MTN')
# mtn.home()

# mtn.__balance = 1000
# # print(mtn.__balance)
# print(mtn.get_balance())



# glo = USSD('GLO')

# glo.brandname = 'GLO'
# print(glo.get_brandname())



# Inheritance

class Parent:
    __surname = 'Adedeji'
    
    def get_surname(self):
        return self.__surname

par = Parent()
# par.__surname = 'Olawale'
# print(par.__surname)
# print(par.get_surname())
    
    
class Child(Parent):
    __firstname = 'Ayomide'
    
    
    def get_firstname(self):
        return self.__firstname
    
    def get_fullname(self):
        return self.__firstname + " " + self.get_surname()



# chd = Child()
# print(chd.get_firstname())

# print(chd.get_fullname())

