#Array
arr=[] #dynamic array
#array traversal
arr=[1,34,55,99]
for i in arr:
    print(i,end=" ")
print()

#linear search  using traversal
arr=[1,34,55,99]
i=0
target=55
found=False
for i in range(len(arr)):
    if arr[i]==target:
        found=True
        break
if found:
    print("found")
else:
    print("not found")     

#MOdify using traversal 
arr=[100,200,20003,40000]
for i in range(len(arr)):
    arr[i]+=10000
print("modified array:",arr)

#Array insertion using shift elements  to right
arr=[10,20,30,40,0]
n=4
for i in range(n-1,-1,-1): #start at i=4 ,i values are 3,2,1,0
    arr[i+1]=arr[i]
arr[0]=50
for i in range(n+1):
    print(arr[i],end=' ')

#array insertion of specific element using shift elemnets to right (custom )
arr = [10,20,30,40,0] #array size is "5"
n=4
pos=2
ele=5
for i in range(n-1,pos-2,-1): # i range from 3 to 0 ,i values are 3,2,1 
    arr[i+1]=arr[i]
arr[pos-1]=ele
print(arr)













