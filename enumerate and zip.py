#enumerate function is used to add a counter to an iterable and returns it as an enumerate object
infacturators=["Alice", "Bob", "Charlie"]
for index,name in enumerate(infacturators, start=1):
    print(f"{index}: {name}")

 #zip function is used to combine two or more iterables (like lists or tuples) into a single iterable of tuples   
languages=["Python","Java","C++"] 
levels=["Beginner","Intermediate","Advanced"]
for lang,level in zip(languages,levels):
    print(f"{lang} is for {level} level")
