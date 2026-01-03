#list comprehensions
even_numbers=[x for x in range(1,88) if x%3==0]
print(even_numbers)
#creating tuples using list comprehension
numbers=input("enter numbers sepparted by comma:")
result=[(x,int(x)**2,int(x)**3) for x in numbers.split(",")]
print(result)
#creating a dictionary using list comprehension
squares={x:x**2 for x in range(1,10)}
print(squares)

#creating a set using list comprehension
odd_numbers=[x for x in range(1,20) if x%2!=0]
print(odd_numbers)

#nested list comprehension
matrix=[[1,2,3],[4,5,6],[7,8,9]]
transposed=[[row[i] for row in matrix] for i in range(3)]
print(transposed)

#filter() is used to filter the items in an input list
avengers=["ironman","thor","hulk","captain america","black widow","hawkeye"]
doomsday_avengers=list(filter(lambda x: "m" in x,avengers))
print(doomsday_avengers)
def is_long_word(word):
    return len(word)>6
long_words=list(filter(is_long_word,avengers))
print(long_words)

#map() is used to apply a function to all the items in an input list
celius_temperatures=[36.6,37.0,38.2,39.5,40.0]
def is_fahrenheit(celius):
    return (celius*9/5)+32
fahrenheit_temperatures=list(map(is_fahrenheit,celius_temperatures))
print(fahrenheit_temperatures)

#sum() function
numbers=[100,200,3000,467,384]
total=sum(numbers)
print(total)
