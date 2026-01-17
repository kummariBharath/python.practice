#### Handling the object attributes dynamically
class book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
book_1=book("python","Bharath")
book_2=book("java","Alex") 
print(getattr(book_1,"price","not avaliable")) #prints the default value if attribute not found
print(getattr(book_2,"author","not avaliable")) #prints the attribute value if found