    account_name = '' 
    account_balance = 0 
    account_password = '' 

    def newAccount(name, balance, password): 
        global account_name, account_balance, account_password 
        account_name = name 
        account_balance = balance 
        account_password = password 
        
    def show(): 
        global account_name, account_balance, account_password 
        print('       Name', account_name) 
        print('       Balance:', account_balance) 
        print('       Password:', account_password) 
        print() 
        
    def getBalance(password): 
        global account_name, account_balance, account_password 
        if password != account_password: 
            print('Incorrect password') 
            return None 
        return account_balance

    def deposit(ammount_to_deposit, password): 
        global account_name, account_balance, account_password 
        if ammount_to_deposit < 0: 
            print('You cannot deposit a negative amount!') 
            return None 
        if password != account_password: 
            print('Incorrect password') 
            return None 
        account_balance = account_balance + ammount_to_deposit 
        return account_balance 

    def withdraw (amount_to_withdraw, password):
        global account_name, account_balance, account_password 
        if amount_to_withdraw < 0: 
            print('You cannot withdraw a negative amount') 
            return None 
        if password != account_password: 
            print('Incorrect password for this account') 
            return None
        if amount_to_withdraw > account_balance: 
            print('You cannot withdraw more than you have in your account') 
            return None 
        account_balance = account_balance - amount_to_withdraw 
        return account_balance


    newAccount("Umair", 100, 'shop')  # create an account 

    while True: 
        print() 
        print('Press b to get the balance') 
        print('Press d to make a deposit') 
        print('Press w to make a withdrawal') 
        print('Press s to show the account') 
        print('Press q to quit') 
        print() 
        
        action = input('What do you want to do? ') 
        action = action.lower()  # force lowercase 
        action = action[0]  # just use first letter 
        print()
        
        if action == 'b': 
            print('Get Balance:') 
            user_password = input('Please enter the password: ') 
            the_balance = getBalance(user_password) 
            if the_balance is not None: 
                print('Your balance is:', the_balance)
                
        elif action == 'd': 
            print('Deposit:') 
            user_deposit_amount = input('Please enter amount to deposit: ') 
            user_deposit_amount = int(user_deposit_amount) 
            user_password = input('Please enter the password: ')
            new_balance = deposit(user_deposit_amount, user_password) 
            if new_balance is not None: 
                print('Your new balance is:', new_balance)
                
        elif action == 'w': 
            print('Widhdraw:') 
            user_withdraw_amount = input('Please enter amount to Withdraw: ') 
            user_withdraw_amount = int(user_withdraw_amount) 
            user_password = input('Please enter the password: ')
            new_balance = deposit(user_withdraw_amount, user_password) 
            if new_balance is not None: 
                print('Your new balance is:', new_balance)     
        elif action == 's':
            show()
            
        else:
            break
                
        print('Done')

