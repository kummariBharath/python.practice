#enumerate function is used to add a counter to an iterable and returns it as an enumerate object
infacturators=["Alice", "Bob", "Charlie"]
for index,name in enumerate(infacturators, start=1):
    print(f"{index}: {name}")

 #zip function is used to combine two or more iterables (like lists or tuples) into a single iterable of tuples   
languages=["Python","Java","C++"] 
levels=["Beginner","Intermediate","Advanced"]
for lang,level in zip(languages,levels):
    print(f"{lang} is for {level} level")

students=["John","Emma","Sophia"]
scores=[85,92,78]
rankings=[1,2,3] 
for student,score,rank in zip(students,scores,rankings):
    print(f"{student} scored {score} and is ranked with {rank}")  
