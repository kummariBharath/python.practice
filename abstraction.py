#abstraction is a process of hiding the implementation details and showing only functionality to the user
#abstraction can be achieved by using abstract classes and interfaces
from abc import ABC,abstractmethod 
class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self): #@this method is abstract method and it must be implemented by the subclass
        pass

# Concrete subclass that implements the abstract method
class ConcreteClassOne(AbstractClass):
    def abstract_method(self):
        print('Implementation in ConcreteClassOne')

# Another concrete subclass
class ConcreteClassTwo(AbstractClass):
    def abstract_method(self):
        print('Implementation in ConcreteClassTwo')
#c=abstractmethod() #TypeError: Can't instantiate abstract class AbstractClass with abstract methods abstract_method
c1=ConcreteClassOne() 
c1.abstract_method()

from abc import ABC,abstractmethod
class Assignment(ABC):
    def __init__(self,name):
        self.name=name
    @abstractmethod    
    def submit(self):
        pass
class submit_assignment(Assignment):
    def submit(self):
        print(f"{self.name} submitted the assignment")
class submit_project(Assignment):
    def submit(self):
        print(f"{self.name} submitted the project")        
s=submit_assignment("bharath")
print(s.name)
print(s.submit())           