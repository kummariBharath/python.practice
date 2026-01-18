class hello:
    message = "hi"
print(hello.message)    

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
dog_1=Dog("buddy",3)
print(dog_1.name)