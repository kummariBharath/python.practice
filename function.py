#functions are reusable blocks of code that perform a specific task
def greet(name):
     #f is fstring for formatting
    return f"Hello, {name}!"
#use function
print(greet("Bharath"))

def multiply(a,b):
    return a * b
print(multiply(177,199))

def factorial(n):
    if n ==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(100))
