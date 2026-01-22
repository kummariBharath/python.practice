class Wallet:
    def __init__(self,balance):
         self.__balance=balance 
    def deposit(self,amount):
         if amount>0:
              self.__balance+=amount
    def withdraw(self,amount):
         if amount<=self.__balance:
              raise ValueError("insuffient funds")
    def get_balance(self):
         return self.__balance     
acc_1=Wallet(500)
print(acc_1.get_balance())    # with double underscore balance is private and accesible with methods only        

#deining a private method which does the internal work
class calcy:
    def add(self,a,b):
         return self.__add_internal(a,b)
    def __add_internal(self,a,b): #internel private method
         return a+b
cal_1=calcy()
print(cal_1.add(5,200))    

#adding a private attribute __validate in the first example of class wallet
class Wallet:
    def __init__(self,balance):
         self.__balance=balance 
    
         
    def __validate_balance(self):
         if self.__balance<0:
              raise ValueError("Balance cannot be negative")
         
    def deposit(self,amount):
         self.__balance+=amount
              
    def withdraw(self,amount):
         self.__validate_balance(amount)
         if amount>self.__balance:
              raise ValueError("insuffient funds")
         self.__balance-=amount
         
    def get_balance(self):
         return self.__balance
    
acc_1=Wallet(500)
print(acc_1.get_balance())
print(acc_1.deposit(200))
print(acc_1.get_balance())
print(acc_1.deposit(-50))  # no change as amount is negative


         