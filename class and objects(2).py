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

   def __getattribute__(self, key):
        dict_obj = object.__getattribute__(self, 'dict')
        if key in dict_obj:
            return dict_obj[key]
        return object.__getattribute__(self, key)


   def delete(self,key):
        if key in self.dict:
             del self.dict[key]    

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
print(cart.__getattribute__("grape"))
print(cart.__getattribute__("apple"))