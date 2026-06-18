from abc import ABC, abstractmethod
class Customer:
    def __init__(self,customer_id,name,phone_number):
        self.customer_id=customer_id
        self.name=name
        self.phone_number=phone_number
    def display(self):
        print(f"Customer id :{self.customer_id}\nName :{self.name}\nPhone number :{self.phone_number}")
class Transaction:
    def __init__(self,transaction_id,transaction_type,amount):
        self.__transaction_id=transaction_id
        self.__transaction_type=transaction_type
        self.__amount=amount
    def display(self):
        print(f"Transaction id:{self.__transaction_id}\nTransaction type:{self.__transaction_type}\n Amount:{self.__amount}")

class Account(ABC):
    def __init__(self,account_number,customer):
        self.__account_number=account_number
        self.__customer=customer
        self.__balance=0
        self.__transactions=[]
    def deposit(self,amount):
        self.__balance+=amount
        return f"amount {amount} has deposited successfully"
    @abstractmethod
    def withdraw(self,amount):
        pass
    def get_balance(self):
        return self.__balance
    def add_transaction(self,transaction_id,transaction_type,amount):
        self.__transactions.append(Transaction(transaction_id,transaction_type,amount))
        return f"Transaction added successfully"
    def show_transaction(self):
        for transaction in self.__transactions:
            transaction.display()
    @abstractmethod
    def calculate_interest(self):
        pass
class Savings(Account):
    def __init__(self,account_number,customer,interest_rate,minimum_balance):
        super().__init__(account_number,customer)
        self.__minimum_balance=minimum_balance
        self.__interest_rate=interest_rate
    def withdraw(self,amount):
        if self.__balance-amount>=self.__minimum_balance:
            self.__balance-=amount
            return f"Withdrawn successfull"
        return f"amount exceeds minimum balance"

    def calculate_interest(self):
        interest=(self.__balance*5)/100
        return interest

class Current(Account):
    def __init__(self, account_number, customer, interest_rate, overdraft_limit):
        super().__init__(account_number, customer)
        self.__overdraft_limit = overdraft_limit
        self.__interest_rate = interest_rate

    def withdraw(self, amount):
        if -(self.__balance - amount) <= self.__overdraft_limit:
            self.__balance -= amount
            return f"Withdrawn successfull"
        return f"amount exceeds overdraftlimit"

    def calculate_interest(self):
        interest = (self.__balance * 9) / 100
        return interest
class Bank:
    def __init__(self):
        self.customers={}
        self.accounts={}
    def register_customer(self,customer_id,name,phone_number):
        self.customers[customer_id]=Customer(customer_id,name,phone_number)
        return f"Customer added successfully"
    def create_savings_account(self,account_number,customer_id):
        if self.customers[customer_id]:
            customer=self.customers[customer_id]
            self.accounts[account_number]=Savings(account_number,customer_id,9,200)
            return f"Account has created successfully"
        return f"customer id doesnt exist"

    def create_current_account(self,account_number,customer_id):
        if self.customers[customer_id]:
            customer=self.customers[customer_id]
            self.accounts[account_number]=Current(account_number,customer_id,9,200)
            return f"Account has created successfully"
        return f"customer id doesnt exist"
    def deposit(self,account_number,money):
        if self.accounts[account_number]:
            account=self.accounts[account_number]
            return account.deposit(money)
        return f"Account number doesnt exist"
    def withdraw(self,account_number,money):
        if self.accounts[account_number]:
            account=self.accounts[account_number]
            return account.withdraw(money)
        return f"Account number doesnt exist"
    def transfer_money(self,money,account_number,transaction_id,transaction_type):
        if self.accounts[account_number]:
            account=self.accounts[account_number]
            return account.add_transaction(transaction_id,transaction_type,money)
        return f"Account doesnt exist"
    def show_account(self,account_number):
        if self.accounts[account_number]:
            account=self.accounts[account_number]
            return f"{account.customer.display()} {account.get_balance()}"
        return f'account doesnt exist'
    def show_transaction(self,account_number):
        if self.accounts[account_number]:
            account=self.accounts[account_number]
            return account.show_transaction()
        return f"Account doesn't exist"

def main():
    bank_manager=Bank()
    while True:
        print(f"1. Register Customer\n2. Create Savings Account\n3. Create Current Account"
              f"\n4. Deposit Money\n5. Withdraw Money\n6. Transfer Money\n"
              f"7. Show Account Details\n8. Show Transactions\n9. Exit")
        choice=input("Enter your choice: ")
        if choice==1:
            customer_id=int(input("enter the customer id: "))
            name=input("enter the customer name")
            phone_number=input("enter the customer phone number")
            print(bank_manager.register_customer(customer_id,name,phone_number))
        elif choice==2:
            account_number=int(input("enter the account number :"))
            customer_id=int(input("enter the customer id :"))
            print(bank_manager.create_savings_account(account_number,customer_id))
        elif choice==3:
            account_number=int(input('enter the account number :'))
            customer_id=int(input("enter the customer id :"))
            print(bank_manager.create_current_account(account_number,customer_id))
        elif choice==4:
            money=int(input("enter the amount you want to deposit :"))
            account_number=int(input("enter the account number :"))
            print(bank_manager.deposit(account_number,money))
        elif choice==5:
            money = int(input("enter the amount you want to deposit :"))
            account_number = int(input("enter the account number :"))
            print(bank_manager.withdraw(account_number,money))
        elif choice==6:
            money=int(input("enter the money you want to transfer :"))
            account_number=int(input("enter the account number :"))
            transaction_id=int(input("enter the transaction id :"))
            transaction_type=input("enter the transaction type :")
            print(bank_manager.transfer_money(money,account_number,transaction_id,transaction_type))
        elif choice==7:
            account_number=int(input("enter the account number"))
            print(bank_manager.show_account(account_number))
        elif choice==8:
            account_number=int(input("enter the account number"))
            print(bank_manager.show_transaction(account_number))
        elif choice==9:
            break

