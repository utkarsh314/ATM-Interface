class user:
    def __init__(self, username, PIN, balance=0):
        self.username = username
        self.PIN = PIN
        self.balance = balance

class ATM(user):
    def __init__(self, username, PIN, balance=0):
        super().__init__(username, PIN, balance)

    def ViewBalance(self):
        print('Your current balance is: ', self.balance)

    def update(self):
        login = open('login.txt', 'r') 
        accounts = login.readlines()
        login.close()

        accountsnew = []

        for account in accounts:
            details = account.split(' ')
            if details[0] == self.username:
                account = account.replace(details[2], f'{self.balance}\n')
            accountsnew.append(account)
        
        newdata = "".join(accountsnew)
        login = open('login.txt', 'w')
        login.write(newdata)
        login.close()

    def Deposit(self):
        amount = float(input('Please enter amount to be deposited:'))
        balance = float(self.balance)
        balance += amount
        self.balance = balance
        print("ammount deposited succesfully!")

    def Withdraw(self):
        amount = float(input('Please enter amount to be withdrawn:'))
        balance = float(self.balance)
        if amount <= balance:
            balance -= amount
            self.balance = balance
            print("ammount withdrawn succesfully!")
        else:
            print('Not enough balance in account')

print("""Welcome to the ATM, please insert card to continue:
1: Log In
2: Create New Account
""")

i = int(input('Enter here:'))

if i == 1:
    while(True):
        Username = input('Enter Username: ')
        PIN = input('Enter PIN: ')
    
        login = open('login.txt', 'r') 
    
        data = login.read()
    
        if f'{Username} {PIN}' in data:
            print('Login Successful!')
            break
        else:
            print('incorrect Username or PIN')
    
elif i == 2:
    while(True):
        Username = input('Set a new username: ')
        PIN = input('Set a 4-digit PIN: ')
        
        if PIN.isdigit() and len(PIN) == 4:
            
            PIN2 = input('confirm PIN: ')

            login = open('login.txt', 'r') 
            data = login.read()
    
            if Username not in data and PIN == PIN2:
                balance = 0
                login = open('login.txt', 'a')
                login.write(f'\n{Username} {PIN} {balance}')
                print('Account created successfully! You have been logged in!')
                break
            
            elif Username in data:
                print('This username already exists, try another')
    
            else:
                print('Please enter correct PIN')
        else:
            print('Please enter a 4-digit PIN')

CurrentUser = ATM(Username, PIN)

login = open('login.txt', 'r') 
accounts = login.readlines()

for account in accounts:
    details = account.split(' ')
    if details[0] == Username:
        CurrentUser.balance = details[2]

while(True):
    print()
    print("""What would you like to do today?
1: Display Balance
2: Deposit
3: Withdraw
4: Log out
""")

    option = int(input('Enter Here: '))

    if option == 1:
        CurrentUser.ViewBalance()

    elif option == 2:
        CurrentUser.Deposit()
        CurrentUser.update()

    elif option == 3:
        CurrentUser.Withdraw()
        CurrentUser.update()

    elif option == 4:
        print('Please remove card')
        exit()