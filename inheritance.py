class Developer:
    def __init__(self,name_1,name_2):
        self.name_1=name_1
        self.name_2=name_2
    def code(self):
        return f"{self.name_1} writes the logic for project"
    def test(self):
        return f"{self.name_2} tests the code"
class Manager(Developer):
    def __init__(self,name_1,name_2,name_3):
        super().__init__(name_1,name_2) #super() is used to call the parent class constructor
        self.name_3=name_3    
    
    