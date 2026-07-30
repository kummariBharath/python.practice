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
