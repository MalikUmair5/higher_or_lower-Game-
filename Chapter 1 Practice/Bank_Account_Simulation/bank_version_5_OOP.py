 # Account class 
class Account():
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = balance
        self.password = password
        
    def deposit(self, amount_to_deposit, password):
        if password != self.password:
            print('Sorry, Incorrect Password')
            return None
        if amount_to_deposit <= 0:
            print('Print you can not deposit a negative amount')
            return None
        self.balance = self.balance + amount_to_deposit
        return self.balance
    
    def withdraw(self, amount_to_withdraw, password):
        if password != self.password:
            print('Sorry, Incorrect Password')
            return None
        if amount_to_withdraw <= 0:
            print('Print you can not deposit a negative amount')
            return None
        if amount_to_withdraw > self.balance:
            print('you can not withdraw more then your balance')
            
        self.balance = self.balance - amount_to_withdraw
        return self.balance
    
    def getBalance(self, password):
        if password != self.password:
            print('Sorry, Incorrect Password')
            return None
        return self.balance
    
    def show(self):
        print('       Name:', self.name) 
        print('       Balance:', self.balance) 
        print('       Password:', self.password) 
        print()
        
        
umairAccount = Account('Umair', 20000, 12345)

umairAccount.show()
