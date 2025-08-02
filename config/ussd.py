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
