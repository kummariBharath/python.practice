class Cart:
   def __init__(self):
       self.dict = {} #dictionary to store items

   def add(self, item):
       self.dict[item] = True

   def remove(self, item, quantity=1):
         if item in self.dict:
              del self.dict[item]
    
   def display(self):
        for item in self.dict:
             print(item)  
   def __len__(self):
        return len(self.dict)

   def __contains__(self,item):
        return f'{item} is in the cart' if item in self.dict else f'{item} is not in the cart'
         
   def insert(self,key,value):
        self.dict[key]=value

   def  delete(self,key):
        if key in self.dict:
             del self.dict[key]    
   def display(self):
        for key, value in self.dict.items():
             print(f"{key}: {value}")

cart=Cart() ##creating object of Cart class
cart.insert("apple",3)
cart.insert("banana",5)
cart.insert("orange",2)
cart.insert("grape",4)
cart.display()
print(cart.__contains__("banana"))
cart.delete("orange")
cart.insert("pineapple",5)
print(cart.__len__())