"""
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

#Array insertion using shift elements  to right(*Beginning)
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


#deletion of specific element using shift elements to left
arr=[10,20,30,40]
n=4
pos=2
for i in range(pos,n-1):
    arr[i]=arr[i+1]
n-=1
for i in range(n):
    print(arr[i],end=' ')

 #deletion of first occurrence of specific element using remove()
arr=list(map(int,input().split()))
ele=int(input("enter ele to deleted"))
n=len(arr)
if ele in arr:
    arr.remove(ele)
print(" arr after deletion") 
for i in range(len(arr)):
    print(arr[i],end=' ')

#removing all occurances of the element using remove and copy of the arr(updating arr ,itertating over index of copy)



arr=list(map(int,input().split()))
ele=int(input('enter element to be deleted')) 
for x in arr[:]:
    if x==ele:
        arr.remove(ele)  
print(arr)  
"""

def findMaxConsecutiveOnes(nums): #
        count=0
        maximum=0
        for num in nums:
            if num==1:
                count+=1
                maximum=max(maximum,count)
            else:
                count=0 #reset the count to 0 when arr[i]==0    
        return maximum
print(findMaxConsecutiveOnes([1,1,0,1,1,1])) #output:3






 


   













