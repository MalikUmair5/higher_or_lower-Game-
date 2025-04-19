# Non-OOP Bank
# Version 5
# Any number of accounts - with a list of dictionaries 

account_list = []

def newAccount(a_name, a_balance, a_password): 
    global account_list 
    newAccountDict = {'name':a_name, 'balance':a_balance, 'password':a_password} 
    account_list.append(newAccountDict) 
    
def show(account_number): 
    global account_list 
    print('Account', account_number) 
    this_account = account_list[account_number] 
    print('       Name', this_account['name']) 
    print('       Balance:', this_account['balance']) 
    print('       Password:', this_account['password']) 
    print()
    
def getBalance(account_number, password): 
    global account_list 
    this_account = account_list[account_number] 
    if password != this_account['password']: 
        print('Incorrect password') 
        return None 
    return this_account['balance'] 


# Create two sample accounts 
print("Fahad account is account number:", len(account_list)) 
newAccount("Fahad", 100, 'Madarsa') 
print("Mary's account is account number:", len(account_list)) 
newAccount("Saif", 2000, 'Shop')

while True:
    print() 
    print('Press s to show the account') 
    print('Press b to get balance')
    print('Press q to quit') 
    print() 

    action = input("please press your option: ")
    action = action.lower()
    
    if action == 'b':
        account_number = int(input("Enter account Number to show the Balance: "))
        user_password = input("Enter account Password: ")
        balance = getBalance(account_number, user_password)
        print(balance)

     
    if action == 's':
        account_number = int(input("Enter account Number to show the details: "))
        show(account_number)
        
    if action == 'q':
        break
    
print('done')