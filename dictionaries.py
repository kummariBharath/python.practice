#creation 
#using{}
my_dict={'name':'bharath','age':20,'city':'hyderabad'}
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

#get() method to access value
print(my_dict.get('name'))
print(my_dict.get('country','India')) #if key not found return default value
my_dict.pop('age')  #removes key value pair
print(my_dict)
my_dict['age']=21  #modifying 
my_dict.update({'city':'bangalore'},domain='analyst')
print(my_dict)
#deletion
del my_dict['city']
print(my_dict)

#looping through a dictionary
products={'laptop':100000,'phone':20000,'tablet':15000,'headphones':5000}
for product,price in products.items():
    print(f'The price of {product} is {price}')
 #applying discount using loop
for product,price in products.items():
    discounted_price=price*0.9
    print(f'The discounted price of {product} is {discounted_price}')
   
#enumerte function
for product in enumerate(products):
    print(product)
for index,product,price in enumerate(products.items()):
    print(index,product,price)    