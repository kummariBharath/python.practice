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
    def __add_internal(self,a,b):
         return a+b
cal_1=calcy()
print(cal_1.add(5,200))         
         