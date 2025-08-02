from config.ussd import USSD

class USSD_PRO(USSD):
    
    __reg_no = ''
    
    def __init__(self, brand, reg_number):
        super().__init__(brand)
        self.__reg_no = reg_number
        print(f"REG: {self.__reg_no}\n")
    

myussd = USSD_PRO('MTN', 1234)
myussd.home()