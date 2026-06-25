from pydantic import BaseModel
class RegisterCustomer(BaseModel):
    customer_id:int
    name:str
    phone_number:str
class AccountType(BaseModel):
    account:int
    customer:int
class ShowDetails(BaseModel):
    account:int
class TransferMoney(BaseModel):
    from_acc:int
    to_acc:int
    amount:int
class Transaction(BaseModel):

    account:int

