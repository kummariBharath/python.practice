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
#filter()
avengers=["ironman","thor","hulk","captain america","black widow","hawkeye"]
doomsday_avengers=list(filter(lambda x: "a" in x,avengers))
print(doomsday_avengers)
def is_long_word(word):
    return len(word)>6
long_words=list(filter(is_long_word,avengers))
print(long_words)