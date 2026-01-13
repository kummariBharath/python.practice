# exception handling is the process of catching errors and managing the errrors
try:
    x=10/0
except ZeroDivisionError:
    print("you can't divide by zero!")
#try is block of code where error might come
# handles the  error raised from try block        