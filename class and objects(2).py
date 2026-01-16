class Cart:
   def __init__(self):
       self.items = {} #dictionary to store items

   def add(self, item):
       self.items[item] = True

   def remove(self, item, quantity=1):
         if item in self.items:
              del self.items[item]
    
   def display(self):
        for item in self.items:
             print(item)  
   def __len__(self):
        return len(self.items)
   
   def __contains__(self,item):
        return item in self.items
         
   def insert(self,key,value):
        self.items[key]=value

   def  delete(self,key):
        if key in self.items:
             del self.items[key]    

                     