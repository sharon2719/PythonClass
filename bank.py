class Bank:
    customer="Rita Dominic"

    def __init__(self,deposit,balance):
        self.deposit=deposit
        self.balance=balance

    def get_balance(self):
        return f"Dear {self.customer},you have  balance of kshs.{self.balance}."

    def borrow(self):
        return f"Dear {self.customer},you have a deficit of {self.balance-self.deposit}to get a loan."

    def save(self):
        return f"Dear {self.customer} your current savings is Kshs.{self.balance}"
        