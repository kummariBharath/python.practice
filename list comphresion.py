#list comprehensions
even_numbers=[x for x in range(1,88) if x%3==0]
print(even_numbers)
#creating tuples using list comprehension
numbers=input("enter numbers sepparted by comma:")
result=[(x,x**2,x**3) for x in numbers.split(",")]
print(result)
#creating a dictionary using list comprehension
squares={x:x**2 for x in range(1,10)}
print(squares)