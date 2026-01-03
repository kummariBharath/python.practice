#lamba function is used as anonymous function instead of defining a fun() using def keyword
#syntax: lamba arguments: expression
#example 1
triple=lambda x:x*3
print(triple(10))
developers=lambda name: "Hello "+name+", welcome to the world of Python!"
print(developers("Bharath"))
#example 2
expression=lambda a,b,c:(b**2-4*a*c+2*a)/(2*a)
print(expression(2,5,3))
#example 3
max_number=lambda x,y: x if x>y else y
print(max_number(30,50))