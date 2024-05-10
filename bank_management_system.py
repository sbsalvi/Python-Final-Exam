import random
from datetime import datetime

class User:
    users=[]

    def __init__(self,name,email,address,account_type):
        self.name=name
        self.email=email
        self.address=address
        self.balance=0
        self.loan_limit=2
        User.account_number=random.randint(1000,5000)
        self.account_number=User.account_number
        self.transaction_history=[]
        self.account_type=account_type
        User.users.append(self)

    def deposit(self,amount):
        if(amount>0):
            self.balance+=amount
            print(f"amount {amount} is added to your account")
            self.transaction_history.append(f"transaction type: deposit, account number {self.account_number}, amount {amount}, time {datetime.now()}")
        else:
            print(f"amount {amount} is not valid. Try again")

    def withdraw(self,amount):
        if amount>0 and amount<=self.balance:
            self.balance-=amount
            print(f"your amount {amount} withdraw successfully")
            self.transaction_history.append(f"transaction type: withdraw, account number {self.account_number}, amount {amount}, time {datetime.now()}")
        else:
            print(f"withdrawal amount {amount} is exceeded")
    
    def check_available_balance(self):
        print(f"your available balance is {self.balance}")

    def check_transaction_history(self):
        print("transaction history:")
        for x in self.transaction_history:
            print(x)
    
    def take_loan(self,amount):
        if self.loan_limit>0:
            self.balance+=amount
            self.loan_limit-=1
            admin.total_loan+=amount
            print(f"loan amount {amount} is added to your account")
            self.transaction_history.append(f"transaction type: take loan, account number {self.account_number}, amount {amount}, time {datetime.now()}")
        else:
            print("your loan limit is over")
    def transfer_amount(self,transfer_account,amount):
        if transfer_account in User.users:
            if amount>0 and amount<=self.balance:
                transfer_account.deposit(amount)
                self.balance-=amount
                print(f"amount {amount} is transferd to account {transfer_account.account_number}")
                self.transaction_history.append(f"transaction type: transfer amount, from account {self.account_number} to account {transfer_account.account_number} amount {amount}, time {datetime.now()}")
            else:
                print(f"amount {amount} in not valid")
        else:
            print(f"account {account_number} does not exist")
    
    def check_account(account_number):
        flag=False
        for user in User.users:
            if user.account_number==account_number:
                flag=True
        return flag

class Bank:
    def __init__(self,name):
        self.name=name
        
class Admin:
    password="admin123"
    def __init__(self):
        self.total_loan=0
        self.is_loan_active=True
        self.bank_is_bankrupt=False

    def create_user_account(self,name,email,address,account_type):
        User(name,email,address,account_type)
        account_number=User.account_number
        print("account opend successfully")
        print(f"user name {name} account number {account_number}")
    
    def delete_user_account(self,account_number):
        for user in User.users:
            if user.account_number == account_number:
                User.users.remove(user)
                print(f"account {account_number} deleted successfully")
            
    def  accounts_list(self):
        if len(User.users)==0:
            print("accounts list is empty")
        else:
            print("\t accounts list \t")
            for user in User.users:
                print(f"user name: {user.name}")
                print(f"email: {user.email}")
                print(f"address: {user.address}")
                print(f"account number: {user.account_number}")
                print(f"account balance: {user.balance}")
                print(f"account type: {user.account_type}")
                print()

    def bank_balance(self):
        balance=0
        for user in User.users:
            balance+=user.balance
        print(f"total available balance of the bank is {balance}")
    
    def total_loan_amount(self):
        print(f"total loan amount of the bank is {self.total_loan}")

    def loan_status(self,status):
        if status==True:
            self.is_loan_active=True
            print("loan system on")
        else:
            self.is_loan_active=False
            print("loan system off")

    def bankrupt_status(self,status):
        if status==True:
            self.bank_is_bankrupt=True
            print("bank is bankrupt on")
        else:
            self.bank_is_bankrupt=False
            print("bank is bankrupt off")

abc_bank=Bank("ABC Bank")
admin=Admin()

while(True):
    print("\t Welcome to the ABC Bank \t")
    print("1.user")
    print("2.admin")
    print("3.exit")

    option=int(input("enter option: "))

    if option==1:
        print("\t user options \t")
        print("1.create account")
        print("2.log in account")
        print("3.exit")

        option2=int(input("enter option: "))

        if option2==1:
            name=input("enter name: ")
            email=input("enter email: ")
            address=input("enter address: ")
            account_type=input("enter account type: ")

            admin.create_user_account(name,email,address,account_type)
        elif option2==2:
            account_number=int(input("enter your account number: "))
            if User.check_account(account_number):
                user=None
                for x in User.users:
                    if x.account_number==account_number:
                        user=x
                    
                if user is not None:
                    while(True):
                        print("\t user options \t")
                        print("1.deposit amount")
                        print("2.withdraw amount")
                        print("3.check available balance")
                        print("4.check transaction history")
                        print("5.take loan")
                        print("6.transfer amount")
                        print("7.exit")

                        option3=int(input("enter option: "))

                        if option3==1:
                            amount=int(input("enter deposit amount: "))
                            user.deposit(amount)
                        elif option3==2:
                            amount=int(input("enter withdraw amount: "))
                            if admin.bank_is_bankrupt==False:
                                user.withdraw(amount)
                            else:
                                print("the bank is bankrupt")
                        elif option3==3:
                            user.check_available_balance()
                        elif option3==4:
                            user.check_transaction_history()
                        elif option3==5:
                            if admin.is_loan_active==True:
                                amount=int(input("enter loan amount: "))
                                user.take_loan(amount)
                            else:
                                print("loan section is off now")
                        elif option3==6:
                            account_number=int(input("enter transfer account number: "))
                            if User.check_account(account_number):
                                user2=None
                                for y in User.users:
                                    if y.account_number==account_number:
                                        user2=y
                                if user2 is not None:
                                    amount=int(input("enter transfer amount: "))
                                    if amount>0 and amount<=user.balance:
                                        user.transfer_amount(user2,amount)
                                    else:
                                        print(f"transfer amount {amount} is not valid")
                                else:
                                    print("account does not exist") 
                        elif option3==7:
                            break
                        else:
                            print(f"option {option3} is not valid")
        elif option2==3:
            break
        else:
            print(f"option {option2} is not valid")
    elif option==2:
        password=input("enter admin password: ")
        if password==admin.password:
            while(True):
                print("\t admin options \t")
                print("1.create user account")
                print("2.delete user account")
                print("3.see all user accounts")
                print("4.check available bank balance")
                print("5.check total loan amount")
                print("6.change loan feature")
                print("7.change bankrupt status")
                print("8.exit")

                option4=int(input("enter option: "))
                if option4==1:
                    name=input("enter name: ")
                    email=input("enter email: ")
                    address=input("enter address: ")
                    account_type=input("enter account type: ")

                    admin.create_user_account(name,email,address,account_type)
                elif option4==2:
                    account_number=int(input("enter delete account number: "))
                    admin.delete_user_account(account_number)
                elif option4==3:
                    admin.accounts_list()
                elif option4==4:
                    admin.bank_balance()

                elif option4==5:
                    admin.total_loan_amount()
                elif option4==6:
                    print("1.turn off loan feature")
                    print("2.turn on loan feature")
                    option5=int(input("enter option: "))
                    if option5==1:
                        admin.loan_status(False)
                    elif option5==2:
                        admin.loan_status(True)
                    else:
                        print(f"option {option5} is not valid")                       
                elif option4==7:
                    print("1.turn on bankrupt")
                    print("2.turn off bankrupt")
                    option6=int(input("enter option: "))
                    if option6==1:
                        admin.bankrupt_status(True)
                    elif option6==2:
                        admin.bankrupt_status(False)
                    else:
                        print(f"option {option6} is not valid")
                elif option4==8:
                    break
                else:
                    print(f"option {option4} is not valid")
        else:
            print("admin password is wrong")
    elif option==3:
        break
    else:
        print(f"option {option} is not valid")