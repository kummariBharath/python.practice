class Company: #polymorphism
    def __init__(self,name):
        self.name=name
    def hire(self):
        return f"{self.name} started to hire freshers"
class organization:
    def hire(self):
        return "organization started hiring"
class industry:
    def hire(self):
        return "industry started to hire" 
def job_search(job):
    print(job.hire())  

job_search(Company("google"))
job_search(organization())
job_search(industry())   
job_search(Company("TCS"))

#Name Mangling in Inheritance
#class parent:
#    def __init__(self):
#        self.__name="bharath" #private variable
#        def get_name(self):
 #           return self.__name
#class child(parent):
#    def diplay(self):
#        return self.__name    
#c=child()
#print(c.diplay()) #AttributeError: 'child' object has no attribute '__name'            
 #correct way below
class parent:
    def __init__(self):
        self.__name="bharath" #private variable
    def get_name(self):
        return self.__name
class child(parent):
    def display(self):
        return self._parent__name  ###Inside class parent, you defined self.__name. Python stored this as self._parent__name.
                                      # Inside class child, you wanted to access that specific variable.
                                      # Since child inherits from parent, it has access to the data, but only under the "mangled" name.
                                       #Therefore, you explicitly wrote self._parent__name to retrieve it.
                                       #_parent__name is how to access private variable in child class
c=child()
print(c.display())


class Example:
    def __init__(self, internal, private):
        self._internal = internal
        self.__private = private

example1 = Example(
    'I can be accessed from outside the class, but should not',
    'I cannot be accessed directly from outside the class'
)
print(example1.__dict__) #{'_Example__private': 'I cannot be accessed directly from outside the class'}
print(example1._internal) #I can be accessed from outside the class, but should
