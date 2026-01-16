class Cart:
   def __init__(self):
       self.items = {}

   def add(self, item):
       self.items[item] = True

   def remove(self, item, quantity=1):
         if item in self.items:
              del self.items[item]
    
   def display(self):
        for item in self.items:
             print(item)  

                     