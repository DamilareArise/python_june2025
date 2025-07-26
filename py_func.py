# Python function stages 

# Declaration stage
# Definition stage
# Invokation satge


def drink():   #declaration
    # define
    print('Drinking')
    
# drink()  #invokation


# return statement
def get_water():
    return 'Water'

# result = get_water()
# print(result)


# Parametized function

def get_water(litres):
    return f'{litres}ltrs of water'

# result = get_water(20)
# print(result)


def get_water(litres=1):
    return f'{litres}ltr(s) of water'

# result = get_water(10)
# print(result)


def get_water(type, litres=1):
    return f'{litres}ltr(s) of {type} water'

# result = get_water('holy', 2)
# print(result)


# ussd code

def home():
    print('Welcome to USSD APP\n')
    ussd = input('USSD: ')
    while ussd != '*312#':
        user = input('Invalid ussd code! \nPress enter to Try again or 1 to exit: ').strip()
        if user == '1':
            exit()
            
        ussd = input('USSD: ')
        
    else:
        dashboard() 
        
def dashboard():
    print("""
       1. Data plan
       2. Check balance
       #. exit   
    """)
    
    user = input('Choice: ').strip()
    if user == '1':
        dataPlan()
    elif user == '2':
        checkBalance()
    elif user == '#':
        exit()
    else: 
        print('Invalid input\n')
        dashboard() #recursive function 

def dataPlan():
    print("""
        1. daily plan
        2. weekly plan
        3. monthly plan
        # exit
        0. go back
        
        """)
    dashboard()
    
def checkBalance():
    print('Your balance is 1000')
    dashboard()

# home()



# global and local variables

val1 = 10  # global variable

def add():
    global val3
    
    val2 = 5  # local variable
    val3 = 2 
    val4 = val3 + val1
    
    return val4 + val2

def subtract():
    val2 = 5
    return val1 - val2

def aggregate():
    # agg = add() * subtract() * val3
    # print(agg)
    print(add())
    print(subtract())

# aggregate()
# print(subtract())



balance = 10
 
def dammie():
    global balance 
    
    balance = balance - 2.5
    return balance

def kenny():
    global balance
    
    balance = balance - 2.5
    return balance
    
def temi():
    global balance
    
    balance = balance - 2.5
    return balance
    
def dami():
    global balance 
    
    balance = balance - 2.5
    return balance
    
def process_payment():
    dammie()
    kenny()
    temi()
    dami()
    
    print(balance)
# process_payment()



# Assignment
# Build a simple Banking app that does the following using python function alone
# 1. Deposit
# 2. withdraw
# 3. checkbalance

# convert your todoApp & contact App to function based





