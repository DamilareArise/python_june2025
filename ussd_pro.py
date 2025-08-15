from config.ussd import UssdConfig

class USSD(UssdConfig):
    __brand = None
    def __init__(self, brand):
        super().__init__()
        self.__brand = brand
        print(f'Hello! welcome to {self.__brand}')
        
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
        1. Buy 1gb
        2. Check balance
        3. Recharge
        4. get code
        #. exit   
        """)
        
        user = input('Choice: ').strip()
        if user == '1':
            res = self.data_1gb()
            print(res)
            
        elif user == '2':
            print(f'Your balance is {self.get_balance()}')
            
        elif user == '3':
            amount = float(input('amount: '))
            res = self.recharge(amount)
            print(res) 
        
        elif user == '4':
            print(self.get_code()) 
            
        elif user == '#':
            exit()
            
        else: 
            print('Invalid input\n')
        
        self.dashboard()

# ussd = USSD('MTN') 
# ussd.home()
# print(type(ussd))

# ussd = UssdConfig()
# print(type(ussd))

# if __name__ == '__main__':
#     ussd.home()


# scripts 
# Module # datetime, time, random
# Library # numpy, pandas
# frameworks # django, flask

import random, time, pwinput as pw

# print(random.randint(2000000000, 2099999999))
# print('Loading...')
# time.sleep(4)
# print('Done')
# from gtts import gTTS
# tts = gTTS('hello everyone')
# tts.save('hello.mp3')

password = pw.pwinput()
print(password)