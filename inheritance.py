class Developer:
    def __init__(self,name_1,name_2):
        self.name_1=name_1
        self.name_2=name_2
    def code(self):
        return f"{self.name} writes the logic for project"
    def test(self):
        return f"{self.name_2} tests teh code"