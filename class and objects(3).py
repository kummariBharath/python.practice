#### Handling the object attributes dynamically
class book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
book_1=book("python","Bharath")
book_2=book("java","Alex") 
print(getattr(book_1,"price","not avaliable")) #prints the default value if attribute not found
print(getattr(book_2,"author","not avaliable")) #prints the attribute value if found

#using the dir() function to list all attributes of an object
class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 

person = Person('John Doe', 30)

# Loop through all attributes of the person object with dir() function
for attr in dir(person):
    # Ignore dunder methods like __init__ or __str__ and regular methods
    if not attr.startswith('__') and not callable(getattr(person, attr)):  #callable checks if the attribute is a method and ignores it
        value = getattr(person, attr)
        print(f'{attr}: {value}')

# Output
# age: 30
# name: John Doe

#set attribute using setattr() function
class laptop:
    pass
#giving info from outside
settings = {
    'brand': 'vivobook',
    'model': '16x',
    'year': 2024
}
laptop_1=laptop()
#setting attributes dynamically
for attr,value in settings.items():
    setattr(laptop_1,attr,value)

print(laptop_1.__getattribute__('brand'))  # Output: vivobook