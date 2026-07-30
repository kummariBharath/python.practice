
"""
class Solution:
    def pattern(self,N):
        for i in range(N):
            for j in range(N):
                print("*",end=' ')
            print()  
sol=Solution()
N=4              
sol.pattern(N)


class Solution:
    def pattern6(self, n):
        for i in range(n):
            for j in range(n,i,-1):
                print(n-j+1,end='')
            print()    
dal=Solution()
n=4
dal.pattern6(n)


class Solution:
    def pattern7(self, n):
        for i in range(n):
            for j in range(n-i-1):
                print(' ',end='')
            for j in range(2*i+1):
                print('*',end='')
            for j in range(n-i-1):
                print(' ',end='')    
            print()
        print()   
cal=Solution()
n=10
cal.pattern7(n)

class Solution:
    def pattern2(self,n):
        for i in range(n):
            for j in range(n-i-2):
                print(' ',end='')
            for j in range(3*i+1):
                print('$',end='')
            for j in range(n-i-2):
                print(' ',end='')
            print()
        print()
cale = Solution()
n=7
cale.pattern2(n)

#prime number 
count=0  
num=int(input("enter your number"))
for i in range(1,num):
    if num%i==0:
        count+=1
if count==1:
    print("prime number")
    
else:
    print("not a prime number")



#palidrome
a=input("enter a string")
b=a[:1]
print(b)

#Palindrome
a=input("enter a str:")
b=a[::-1]
if a==b:
    print("a is palindrome")
else:
    print("Not a palindrome")


#Sum of two number using loop
nums = [5,100]
sum=0
for num in nums:
    sum+=num
print(sum)

#Fibonacci number using simple logic loop(logic is Each number is the sum of the previous two numbers.) 
num=int(input("enter your num"))
a=0
b=1
for i in range(num):
    print(a,end=" ")
    c=a+b #addding the first two and assigning to 'c'
    a=b #the b value is shifted to 'a'
    b=c #c is assigned to 'b'

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

n=int(input("enter a three digit number:"))
a=n//100
b=(n//10)%10
c=n%10
print('Sum =',a+b+c)
"""
#prime number
n=5
count=0
for i in range(1,n):
    if n%2==0:
        count+=1
    else:
        print("prime number")



    


                 
