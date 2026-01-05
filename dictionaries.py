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