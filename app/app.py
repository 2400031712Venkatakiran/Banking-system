from fastapi import FastAPI
from app.schema import RegisterCustomer, Transaction, ShowDetails, AccountType, TransferMoney
from app.main import bank_manager
app=FastAPI()
@app.post('/register_customer')
def register_customer(customer:RegisterCustomer):
    return bank_manager.register_customer(customer.customer_id,customer.name,customer.phone_number)
@app.post('/create_savings_account')
def create_savings_account(account:AccountType):
    return bank_manager.create_savings_account(account.account,account.customer)
@app.post('/create_current_account')
def create_current_account(account:AccountType):
    return bank_manager.create_current_account(account.account,account.customer)
@app.post('/deposit')
def deposit_money(account:Transaction):
    return bank_manager.deposit(account.amount,account.account)
@app.post('/withdraw')
def withdraw_money(account:Transaction):
    return bank_manager.withdraw(account.amount,account.account)
@app.get('/Show_Account')
def show_account(account:int):
    return bank_manager.show_account(account)
@app.get('/Show_Transactions')
def show_transactions(account:int):
    return bank_manager.show_transaction(account)
@app.post('/TransferMoney')
def transfer_money(account:TransferMoney):
    return bank_manager.transfer_money(account.from_acc,account.to_acc,account.amount)

