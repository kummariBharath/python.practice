#Array
arr=[] #dynamic array
#array traversal
arr=[1,34,55,99]
for i in arr:
    print(i,end=" ")
print()

#searching using traversal
arr=[1,34,55,99]
i=0
target=55
found=False
for i in arr:
    if arr[i]==target:
        found=True
        break
if found:
    print("found")
else:
    print("not found")        



