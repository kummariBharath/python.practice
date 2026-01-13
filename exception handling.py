# exception handling is the process of catching errors and managing the errrors
try:
    x=10/0
except ZeroDivisionError:
    print("you can't divide by zero!")
#try is block of code where error might come
# handles the  error raised from try block    

try:
    num=int('1230')
    result=10/num
except ValueError:
    print('that was not a valid number')
except ZeroDivisionError as e: #also alias e for zerodivisionerror
    print(f"error:{e}")           

#mutiple errors finding in the except block
try:
    num=int(input("enter a number :")) 
    result=10/num  
except (ValueError,ZeroDivisionError) as e:
    print(f"error :{e}")
