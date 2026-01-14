#class is blueprint that is used to create the classes using class keyword
class Bharath:
    def __init__(self, name, days):
        self.name = name
        self.days = days
    def learn(self):
        print(f"{self.name} and learns python in {self.days}")
#objects creation and calling from classes
skill_1=Bharath("learns sql",30)
skill_2=Bharath("learns DSA",25)   

#calling the methods
skill_1.learn()
skill_2.learn()
