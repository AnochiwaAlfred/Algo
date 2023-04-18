from random import randint
from datetime import date

# Write a program that simulates a bank account. The program should allow users to open a new account, deposit and 
# withdraw funds, and check their balance.

class User():
    all = []
    
    def __init__(self):
        self.first_name = input('Enter Firstname: ')
        self.last_name = input('Enter Lastname: ')
        self.username = input('Enter preferred username: ')
        self.email=input('Enter email: ')
        self.password = self.set_password()
        self.account=Account(self.first_name, self.last_name)
        
        print('\nAccount Created Sucessfully')
        print(f"\nFIRSTNAME: {self.first_name}")
        print(f"LASTNAME: {self.last_name}")
        print(f"USERNAME: {self.username}")
        print(f"EMAIL: {self.email}")
        print(f"ACCOUNT NAME: {self.account.account_name}")
        print(f"ACCOUNT NUMBER: {self.account.account_number} \n")
        User.all.append(self)    
        
    def set_password(self):
        password1 = input('Enter Preferred Password: ')
        password2 = input('Enter Password Again: ')
        if password1==password2:
            return password1
        else:
            print('Password mismatch')
            self.set_password()
            
    def check_balance(self):
        self.account.check_balance()
    
    def deposit(self, amount:int):
        self.account.deposit()
        
    def withdraw(self):
        self.account.withdraw()
    
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'.title() 
    

class Account():
    all = {}
    acct_numbers = []
    
    def __init__(self, first_name, last_name):
        self.account_name = f"{first_name} {last_name}".upper()
        self.account_number = self.generate_account_number()
        self.__pin = self.set_pin()
        self.opening_date = date.today()
        self.__account_balance = 0
        
        Account.acct_numbers.append(self.account_number)
        Account.all.update({self.account_number:self})
        
    def generate_account_number(self):        
        account_number = randint(1000000000, 9999999999)
        if str(account_number) in Account.acct_numbers:
            self.generate_account_number()
        else:
            return str(account_number)
                
    def set_pin(self):
        pin1:int = input('Enter preferred 4-digit pin for transactions: ')
        pin2:int = input('Enter pin again: ')
        
        if len(str(pin1))!=4:
            self.set_pin()
            print(f'Enter a 4 digit pin')
        if pin1==pin2:
            return str(pin1)
        else:
            print('Password mismatch')
            self.set_pin()
            
    def deposit(self, amount:int):
        self.__account_balance = self.__account_balance + amount
    
    def check_balance(self):
        pin = input('Enter pin: ')
        if pin == self.__pin:
            print(self.__account_balance)
        else:
            print('Wrong Pin')
    
    def withdraw(self):
        amount:int = int(input('Enter withdrawal amount: '))
        pin = input('Enter pin: ')
        if pin != self.__pin:
            print('Wrong Pin')
        else:
            if self.__account_balance >= amount:
                self.__account_balance = self.__account_balance - amount
                print('Withdrawal Successful')  
            else:
                print('Insufficient Balance')              
    
    def __str__(self):
        return self.account_name
    
    def get(self, account_number):
        if account_number==self.account_number:
            return self
            
class Deposit():
    all = []
    def __init__(self):
        self.depositors_name = input('Enter Depositors Name: ')
        self.depositors_number = input('Enter Depositors Number: ')
        self.account_name = input('Enter Account Name: ')
        self.account_number = input('Enter Account Number: ')
        self.amount = int(input('Enter amount: '))
        self.account = self.check_account(self.account_number, self.account_name)
        self.deposit(self.account, self.amount)
        
        Deposit.all.append(self)
        print(f'Deposit of {self.amount} to {self.account} was successful')    
    
    def check_account(self, account_number, account_name):
        try:
            account = Account.all.get(account_number)
        except:
            Exception(f'Wrong account details. Account with {account_number} and {self.account_name} does not exist')
        if account.account_name == self.account_name:
            return account
                

    def deposit(self, account, amount):
        account.deposit(amount)
