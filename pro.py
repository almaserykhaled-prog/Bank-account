from abc import ABC, abstractmethod

class check(ABC):
    def __init__(self,balance,payment_processing):
        self.balance=balance
        self.payment_processing=payment_processing

    @abstractmethod
    def check_balance(self):
        pass

    @abstractmethod   
    def payment_is_processing(self):
        pass

    @abstractmethod
    def with_draw(self):
        pass

    @abstractmethod
    def Depostion(self):
        pass

class voda_cash(check):
    def check_balance(self):
        print(f"this balance is : {self.balance} use voda")
    def payment_is_processing(self):
        print(f"the payment processing is : {self.payment_processing} use voda is succfully")

    def with_draw(balance,amount):
        balance -= amount
        return f"this balance is : {balance} , this balance before with with_draw : {balance}"  

    def Depostion(balance,amount):
        balance += amount
        return f"this balance is : {balance} , this balance before with Depositon : {balance}"       

class instapay(check):
    def check_balance(self):
        print(f"this balance is : {self.balance} use instapay")
    def payment_is_processing(self):
        print(f"the payment processing is : {self.payment_processing} use instapay is succfully")

    def with_draw(balance,amount):
        balance -= amount
        return f"this balance is : {balance} , this balance before with with_draw : {balance}"  

    def Depostion(balance,amount):
        balance += amount
        return f"this balance is : {balance} , this balance before with Depositon : {balance}" 


check=voda_cash(5000,50)
check.check_balance()
check.payment_is_processing()
