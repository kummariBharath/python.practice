mylist=["banana","cherry","apple"]
print(mylist)
item=mylist[2]
print(item)

if "cherry" in mylist:
    print("yes")
else:                 #indentation is immportant#
    print("no")
len(mylist)
mylist.append("lemon")
print(mylist)
mylist.insert(1,"blueberry")
print(mylist)
#pop() removes last item in list
item=mylist.pop()
print(item)
print(mylist)
#remove specific element by value
item=mylist.remove("banana")
print(mylist)
item=mylist.clear()
print(mylist)

list2=[468,787,333,330]
new_list=sorted(list2)
print(list2)
print(new_list)

list3=[1,2,3,4,5,6,7,8,9]
a1=list3[1:]
a2=list3[::1]
a22=list3[::3]      # :: is useful for gap between numbers
a3=list3[::2]
print(a1)
print(a2)
print(a3)
print(a22)

mylist4=[1,2,3,4,5,6]
b=[i*4 for i in mylist4]  #multiplying each element by 4
print(b)

developer_names=["sachin","rahul","anil","sunil"]
developer_names[0]="bharath"  #modifying list element
print(developer_names)
sorted_list=sorted(developer_names)
print(sorted_list)
names_list=["bharath","shivani","navya",["vineeth","mabusubhan","sumit"]]
print(names_list[3][2]) #acccessing the nested _list
phislophers=["plato","aristotle","socrates","descartes"]
great,superior,good,bad=phislophers
print(great)
print(superior)
print(good)
print(bad)
