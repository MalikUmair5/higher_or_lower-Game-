# Non-OOP
# Bank 3
# Two accounts 

account_0_name = ''
account_0_password = ''
account_0_balance = ''
account_1_name = ''
account_1_password = ''
account_1_balance = ''
n_accounts = 0

def new_account(account_Number, name, balance, password):
    global account_0_name, account_0_balance, account_0_password
    global account_1_balance, account_1_name, account_1_password
    
    if account_Number == 0:
        account_0_name = name
        account_0_password = password
        account_0_balance = balance
    
    if account_Number == 1:
        account_1_name = name
        account_1_password = password
        account_1_balance = balance
        
def show():
    global account_0_name, account_0_balance, account_0_password
    global account_1_balance, account_1_name, account_1_password

    if account_0_name != '':
        print('Account 0')
        print('       Name', account_0_name) 
        print('       Balance:', account_0_balance) 
        print('       Password:', account_0_password) 
        print()     
        
        
    if account_1_name != '': 
        print('Account 1') 
        print('       Name', account_1_name) 
        print('       Balance:', account_1_balance) 
        print('       Password:', account_1_password) 
        print()
        

        
while True:
    print() 
    print('Press n create new Account') 
    print('Press s to show the account') 
    print('Press q to quit') 
    print() 
    
    action = input("please press your option: ")
    action = action.lower()
    print(action)
    if action == 'n':
        name = input("Enter User Name: ")
        password = input("Enter account Password: ")
        balance = input("Enter bank account Balance: ")
        
        new_account(1, name, password, balance)
        
    if action == 's':
        show()
    if action == 'q':
        break
    
print('done')
    
    
    
    
    
    
    
        

# Even with just two accounts, you can see that this approach gets out of
#  hand quickly. First, we set three global variables for each account at 1, 2,
#  and 3. Also, every function now has an if statement to choose which set of
#  global variables to access or change. Any time we want to add another
#  account, we’ll need to add another set of global variables and more if
#  statements in every function. This is simply not a feasible approach. We
#  need a different way to handle an arbitrary number of accounts.
