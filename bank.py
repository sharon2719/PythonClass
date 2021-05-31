from datetime import datetime
class Account:

    def __init__(self,name,phoneNumber,loan):
        self.name=name
        self.phoneNumber=phoneNumber
        self.balance=0
        self.loan=loan
        self.statement=[]

    def showBalance(self):
        return f"Hello {self.name},your balance is kshs.{self.balance}."

    def deposit(self,amount):
        if(amount<0):
            return f"You cannot deposit less than 0"
        else:
            self.balance+=amount
            now=datetime.now()
            transaction={"amount":amount,"time":now,"narration":"You deposited"}
            self.statement.append(transaction)
           
            
            return self.showBalance()
           
    
    def show_statement(self):
        for transaction in self.statement:
            amount=transaction["amount"]
            narration=transaction["narration"]
            time=transaction["time"]
            date=time.strftime("%d/ %m / %y")
            print(f"{date}:{narration}:{amount}")
       

    def withdraw(self,amount):
        if(amount>self.balance):
            return f"Your balance is {self.balance}.You cannot withdraw {amount}"
        else:
            self.balance-=amount
            now=datetime.now()
            transaction={"amount":amount,"time":now,"narration":"You have withdrawn"}
            self.statement.append(transaction)
           
            return self.showBalance()
    
    def borrow(self,amount):
        self.amount=amount
        if (amount>0):
            return f"You can borrow{amount}"
        else:
            return f"You cannot borrow less than zero"
    
    def repay_loan(self,amount):
        self.amount=amount
        if(amount>0):
            return f"Please repay your outstanding loan of{amount}"
        else:
            return f"You have cleared your loan!"
