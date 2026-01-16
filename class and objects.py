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

#atttributes i.e aare that belong to the object to hold data
#instance attributes are used by the objects 
#class attributes are used by the class itself and shared by all the objects
class student:
    school="bharath public school" #class attribute
    def __init__(self,name,rollnumber):
        self.name=name
        self.rollnumber=rollnumber ##instance variables
    def admitted(self):
        print(f"{self.name.upper()} holding {self.rollnumber} is student of {student.school}")  
print(student.school)  
student_1=student("bharath","239PA16744")
student_2=student("H","239PA16755")
print(student_1.name)
print(student_1.rollnumber)
student_1.admitted()
print(student_2.name)
print(student_2.rollnumber)
student_2.admitted()



