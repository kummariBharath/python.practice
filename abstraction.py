#abstraction is a process of hiding the implementation details and showing only functionality to the user
#abstraction can be achieved by using abstract classes and interfaces
from abc import ABC,abstractmethod 
class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

# Concrete subclass that implements the abstract method
class ConcreteClassOne(AbstractClass):
    def abstract_method(self):
        print('Implementation in ConcreteClassOne')

# Another concrete subclass
class ConcreteClassTwo(AbstractClass):
    def abstract_method(self):
        print('Implementation in ConcreteClassTwo')
c=abstractmethod() #TypeError: Can't instantiate abstract class AbstractClass with abstract methods abstract_method
c1=ConcreteClassOne() #