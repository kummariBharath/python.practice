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

#another method
n=25
def print_numbers(i):
    if i<=n:
        print(i,end=' ')
        print_numbers(i+1)
        
print_numbers(1)


# finding a num is prime using recursion
def prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        return True
    else:
        return False
print(prime(7))
print(prime(8))

#prime using recursion (corrected and more efficient)
def is_prime_recursive(n, i=2):
    # Base case: if n is less than 2, it's not prime
    if n < 2:
        return False
    # Base case: if i reaches n, n is prime 
    if i == n:
        return True
    # If n is divisible by i, it's not prime
    if n % i == 0:
        return False
    return is_prime_recursive(n, i + 1)

print(is_prime_recursive(7))
print(is_prime_recursive(8))

#slicing
num2=[23,44,55,66,77]
print(num2[0:2])
print(num2[0:4:2])


#sorting
num3=[23,77,15,45]
num3.sort()
print(num3)


#list comprehensions:
#writing the code in concise in single line
list1=[x*x for x in range(5)]
print(list1)

even=[x for x in range(10) if x%2==0]
print(even)

words=["goat","yak","rak"]
length=[len(word) for word in words]
print(length)

#Array/list:It is linear data structure that store multiple of the same type in continugous memory locations
#Python does not have a built in array data type
#syntax:
#array_name=[element1,element22...]

arr=["data","inter"]
print(arr)
print(arr[0])
arr[1]="happy"
print(arr)

#TRAVERSE
#It is visiting and accessing each element of an array/list one by one

arr=[1,23,44,55]
for a in arr:
    print(a)
    
arr=[23,33,445,55]
print(len(arr))

#insertion
arr=[23,44,55,66,77]
arr.append(99)
arr.insert(0,33)
print(arr)




#Deletion

#using remove
arr1=[44,44,55,8734,7474,798278,3483]
arr1.remove(44)
print(arr1)
#using pop
arr2=[123,445,66]
arr2.pop(0)
print(arr2)
#using del
arr3=[44,55,66]
del arr3[2]
print(arr3)

#Searching:it is process of finding whether an element in a array or not and location of podition
#syntax: value in list_name
#        list_name.index(value)

nums=[23,44,55,66]
a=44
if a in nums:
    print(nums.index(a))
else:
    print("NO")

###string methods###
a="bharath"
print(a.upper())
b="BHARATH"
print(b.lower())
c="infofsys"
print(c.capitalize())
d="placed into infofsys"
print(d.title())# title() converts each word's first char to capital
e=' I am into Infofsys '
print(e.strip())#strip() removes trailing spaces
f="I am notPlaced"
print(f.replace("notPlaced","Placed"))
p="bharath"
print(p.split(","))#split() converts into list
fruits=["grapes","apple"]
print("-".join(fruits))#join()
i="Aptitude"
print(i.find("A"))#find()
print(i.startswith("A"))#startswith()
print(i.endswith("e"))#endswith()
print(i.count("t"))#count()


#power of a number using recursion
def pow(N):
    return N**2
print(pow(9))
#using loops
def pow(c,d):
    r=1
    for i in range(d):
        r=r*c
    return r
print(pow(10,4))

#right approach for power of a number
def pow(n,e):
    if e==0:
        return 1
    return n*pow(n,e-1)
print(pow(10,2))

"""
s="the sky is blue"
a=s.split(" ")
a=a[::-1]
print(' '.join(a))
print(a)

s="lets get placed"
k=[]
s=s.split()
for i in s:
    k.append(i[::-1])
print(" ".join(k))      


arr = [1, 4, 3, 2, 6, 5]
a=arr[::-1]
print(a)