class hello:
    message = "hi"
print(hello.message)    

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
dog_1=Dog("buddy",3)
print(dog_1.name)

count = 4
while (count < 5):    
    count = count+1
    print(count)
    break
else:
    print("No Break")

sum=0
num=int(input("enter a number(0 to stop):"))
while num !=0:
    sum+=num
    num=int(input("enter a number(0 to stop):"))
print("The sum is:",sum) #output:enter a number(0 to stop):55
                                 #enter a number(0 to stop):6168
                                 #enter a number(0 to stop):28088888989899
                                #enter a number(0 to stop):0
                                #The sum is: 28088888996122

