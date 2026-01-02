#enumerate function is used to add a counter to an iterable and returns it as an enumerate object
infacturators=["Alice", "Bob", "Charlie"]
for index,name in enumerate(infacturators, start=1):
    print(f"{index}: {name}")

