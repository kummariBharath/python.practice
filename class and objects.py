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

class car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year

    def car_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")  
    def car_age(self,current_year):
        age=current_year - self.year
        print(f"the car is {age} years old")
    def service_recommendation(self,current_year):
        age=current_year-self.year
        if age<3:
            print(f"Car {self.brand} {self.model} requires service.")
        elif 3<=age<7:
            print(f"Car {self.brand} {self.model} requires major service.")
        else:
            print(f"Car {self.brand} {self.model} requires comprehensive service.")
    def car_restriction(self,current_year,pollution):
        age=current_year - self.year
        if age>10 and pollution=="high":
            print(f"Car {self.brand} {self.model} is resticated on the roads")
        else:
            print(f"Car {self.brand} {self.model} is allowed on every roads")

car_1=car("alto","maruti",2018)
car_2=car("polo","volkswagen",2022)
car_3=car("swift","maruti",2015)
car_4=car("creta","hyundai",2020)
car_1.car_info()
car_1.car_age(2026)
car_2.car_info()
car_2.car_age(2026)
#apply methods
car_3.service_recommendation(2026)
car_4.service_recommendation(2026)
car_3.car_restriction(2026,"high")
car_4.car_restriction(2026,"low")
car_2.car_restriction(2026,"high")