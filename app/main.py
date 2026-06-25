from abc import ABC, abstractmethod


class Customer:
    def __init__(self, customer_id, name, phone_number):
        self.customer_id = customer_id
        self.name = name
        self.phone_number = phone_number

    def display(self):
        return{
            "Customer id" : {self.customer_id},
            "Name" : {self.name},
            "Phone number" : {self.phone_number}
        }


class Transaction:
    def __init__(self, transaction_id, transaction_type, amount):
        self._transaction_id = transaction_id
        self._transaction_type = transaction_type
        self._amount = amount

    def display(self):
        return{
            "Transaction id" : {self._transaction_id},
            "Transaction type" : {self._transaction_type},
            "Amount" : {self._amount}
    }


class Account(ABC):
    def __init__(self, account_number, customer):
        self._account_number = account_number
        self._customer = customer
        self._balance = 0
        self._transactions = []

    def deposit(self, amount):
        self._balance += amount

        # CHANGE: Automatically add transaction when deposit happens
        self.add_transaction(0, "Deposit", amount)

        return f"Amount {amount} deposited successfully"

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self._balance

    def add_transaction(self, transaction_id, transaction_type, amount):
        self._transactions.append(
            Transaction(transaction_id, transaction_type, amount)
        )
        return "Transaction added successfully"

    def show_transaction(self):
        # CHANGE: Handle empty transaction list
        if not self._transactions:
            print("No transactions found.")
            return

        return(transaction.display() for transaction in self._transactions)

    @abstractmethod
    def calculate_interest(self):
        pass

    def display(self):
        self._customer.display()

        # CHANGE: Show account number and balance also
        return{
            "customer":self._customer.display(),
            "Account Number" : {self._account_number},
            "Balance" : {self._balance}
        }


class Savings(Account):
    def __init__(self, account_number, customer, interest_rate, minimum_balance):
        super().__init__(account_number, customer)
        self._minimum_balance = minimum_balance
        self._interest_rate = interest_rate

    def withdraw(self, amount):
        if self._balance - amount >= self._minimum_balance:
            self._balance -= amount

            # CHANGE: Automatically add withdraw transaction
            self.add_transaction(0, "Withdraw", amount)

            return "Withdraw successful"

        return "Amount exceeds minimum balance"

    def calculate_interest(self):
        # CHANGE: Use interest_rate variable instead of fixed 5%
        return (self._balance * self._interest_rate) / 100


class Current(Account):
    def __init__(self, account_number, customer, interest_rate, overdraft_limit):
        super().__init__(account_number, customer)
        self._overdraft_limit = overdraft_limit
        self._interest_rate = interest_rate

    def withdraw(self, amount):
        if -(self._balance - amount) <= self._overdraft_limit:
            self._balance -= amount

            # CHANGE: Automatically add withdraw transaction
            self.add_transaction(0, "Withdraw", amount)

            return "Withdraw successful"

        return "Amount exceeds overdraft limit"

    def calculate_interest(self):
        # CHANGE: Use interest_rate variable
        return (self._balance * self._interest_rate) / 100


class Bank:
    def __init__(self):
        self.customers = {}
        self.accounts = {}

    def register_customer(self, customer_id, name, phone_number):

        # CHANGE: Prevent duplicate customers
        if customer_id in self.customers:
            return "Customer already exists"

        self.customers[customer_id] = Customer(
            customer_id,
            name,
            phone_number
        )
        return "Customer added successfully"

    def create_savings_account(self, account_number, customer_id):

        # CHANGE: Prevent duplicate account numbers
        if account_number in self.accounts:
            return "Account already exists"

        if customer_id in self.customers:
            customer = self.customers[customer_id]

            self.accounts[account_number] = Savings(
                account_number,
                customer,
                9,
                200
            )

            return "Savings account created successfully"

        return "Customer id doesn't exist"

    def create_current_account(self, account_number, customer_id):

        # CHANGE: Prevent duplicate account numbers
        if account_number in self.accounts:
            return "Account already exists"

        if customer_id in self.customers:
            customer = self.customers[customer_id]

            self.accounts[account_number] = Current(
                account_number,
                customer,
                9,
                200
            )

            return "Current account created successfully"

        return "Customer id doesn't exist"

    def deposit(self, account_number, money):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            return account.deposit(money)

        return "Account number doesn't exist"

    def withdraw(self, account_number, money):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            return account.withdraw(money)

        return "Account number doesn't exist"

    def transfer_money(
        self,
        from_account,
        to_account,
        amount
    ):

        # CHANGE: Real transfer instead of only adding transaction

        if from_account not in self.accounts:
            return "Sender account doesn't exist"

        if to_account not in self.accounts:
            return "Receiver account doesn't exist"

        sender = self.accounts[from_account]
        receiver = self.accounts[to_account]

        result = sender.withdraw(amount)

        if result == "Withdraw successful":
            receiver.deposit(amount)
            return "Money transferred successfully"

        return result

    def show_account(self, account_number):

        if account_number in self.accounts:
            account = self.accounts[account_number]

            # CHANGE: display() already prints everything.
            # No need to return f"{display()} {balance}"

            return account.display()


        return "Account doesn't exist"

    def show_transaction(self, account_number):

        if account_number in self.accounts:
            account = self.accounts[account_number]

            # CHANGE: show_transaction() already prints transactions.
            return account.show_transaction()


        return f"Account doesn't exist"

bank_manager = Bank()


