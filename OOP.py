class Wallet:
    def __init__(self,balance):
         self._balance=balance 
    def deposit(self,amount):
         if amount>0:
              self._balance+=amount
    def withdraw(self,amount):
         if amount<=self._balance:
              raise ValueError("insuffient funds")
    def get_balance(self):
         return self._balance     
acc_1=Wallet(500)
print(acc_1.self._balance)    # Accessing the balance directly (not recommended)          

         
         