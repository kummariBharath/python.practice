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

#Raise statement used to explicitly throe an exception at any point
def process_data(data):
    try:
        result=int(data)
        return result*2
    except ValueError:
        print('logging:invalid data received')
        raise

print(process_data(88))

def file_config(filename):
    try:
        with open(filename,'r') as file:
            data=file.read()
            return int(data)
    except FileNotFoundError:
        raise ValueError('configuration file is missing')
    except ValueError as e:
        raise ValueError('invalid format') 
print(file_config('bharath.txt'))   

#asseration error
def calculate_square_root(number):
    assert number >=0
    return number**0.5
try:
    result=calculate_square_root(-5)
except AssertionError as e:
    print(f"Asseration failed:{e}")    