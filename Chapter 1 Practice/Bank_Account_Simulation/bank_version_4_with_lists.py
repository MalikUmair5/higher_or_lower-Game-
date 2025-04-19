# Non-OOP Bank
# Version 4
# Any number of accounts - with lists 

account_names_list = []
account_balance_list = []
account_password_list = []


def new_account(name, balance, password):
     global account_names_list, account_balance_list, account_password_list
     account_names_list.append(name)
     account_balance_list.append(balance)
     account_password_list.append(password)
     
def show(account_number):
    global account_names_list, account_balance_list, account_password_list
    try:
        print(f'Account {account_number}')
        print(f'     Name: {account_names_list[account_number]}')
        print(f'     Balance: {account_balance_list[account_number]}')
        print(f'     Password: {account_password_list[account_number]}')

    except IndexError:
        print('Invalid Account number')
    
#similar way more functions to add such as withdraw, deposit etc

while True:
    print() 
    print('Press n create new Account') 
    print('Press s to show the account') 
    print('Press q to quit') 
    print() 

    action = input("please press your option: ")
    action = action.lower()
    
    if action == 'n':
        name = input("Enter User Name: ")
        password = input("Enter account Password: ")
        balance = input("Enter bank account Balance: ")
        
        new_account(name, balance, password)
        
    if action == 's':
        account_number = int(input("Enter account Number to show the details: "))
        show(account_number)
        
    if action == 'q':
        break
    
print('done')
    