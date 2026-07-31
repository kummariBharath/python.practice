"""
#fib using recursion
n=int(input("enter your num"))
def fibonacci(n): 
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
for i in range(n):
    print(fibonacci(i),end=" ")

#Two sum
num1=list(map(int,input("enter").split(',')))
target=5643
for i in range(len(num1)):
    for j in range(i+1,len(num1)):
        if num1[i] + num1[j] == target:
            print([i,j])

#palidrome using loop
a=input("enter a string:")
b=a[::-1]
if a==b:
    print("String is palindrome")
else:
    print("String is not palindrome")
    

for i in range(1,6):
    print(i)
    if i==3:
        break   

#Functions
def college(a,b):
    return a,b
print(college("sree dattha group of instiutions","Bharath"))


def add(a,b):
    return a+b,a//b,a%b,a**b,a*b
print(add(23,45))


a=10
def add():
    d=100
    return a,d
print(add())


a=lambda x:x**2
print(a(44))

def factorial(n):
    fact=1
    if n==1:
        return 1
    return n*factorial(n-1)
print(factorial(5))

#first N numbers sum
def sum(n):
    if n==1:
        return n
    return n+sum(n-1)
print(sum(5))
#Print numbers from 1 to N using recursion
n=25
def printnum(n):
    if n==0:
        return
    printnum(n-1)
    print(n,end=' ')
printnum(n)
"""
#another method
n=25
def print_numbers(i):
    if i<=n:
        print(i,end=' ')
        print_numbers(i+1)
        
print_numbers(1)






