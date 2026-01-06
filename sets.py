#Sets are one of Python's built-in data structures. One of the core characteristics of sets is that they don't store duplicate values. 
my_set={1,2,3,4,5}
my_set.add(66) #add() 
my_set.remove(3) #remove() to delete a element
my_set.discard(1) #dicard() to delete a element
print(my_set)

#.issubset() and issuperset()
my_set1={10,20,30,40,50}
my_set2={20,30,40}
print(my_set2.issubset(my_set1))
print(my_set1.issuperset(my_set2))
#checking comman elements in both sets using .isdisjoint()
print(my_set1.isdisjoint(my_set2))
