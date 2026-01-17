#truty values are 0,[1],(9),{1;2},True,"hello"
#falsy values are 0.0,[],(),{},False,""

from ast import In


num1=10
num2=20
if num1 % 2:     #here 10%2==0 so 0 means false --else block will execute
    print("num1 is truthy")
else:
    print("num1 is falsy")
if num2 % 3:      #here 20%3==2 so 2 means true --if block will execute
    print("num2 is truthy")
else:
    print("num2 is falsy")    

#bool() function is used to check whether the value is truthy or falsy   
print(bool([])) #falsy
print(bool([1,23,45])) #truthy
print(bool(0)) #falsy

a = 10  # binary: 1010
b = 4   # binary: 0100

# BITWISE OPERATORS:

# & (AND) - Returns 1 if both bits are 1
# a & b = 1010 & 0100 = 0000 = 0
print(a & b)  # Output: 0
# Use: Checking if specific bits are set, masking bits

# | (OR) - Returns 1 if at least one bit is 1
# a | b = 1010 | 0100 = 1110 = 14
print(a | b)  # Output: 14
# Use: Setting specific bits, combining flags

# ~ (NOT) - Inverts all bits (0→1, 1→0)
# ~a = ~1010 = ...0101 = -11 (two's complement)
print(~a)  # Output: -11
# Use: Inverting all bits

# ^ (XOR) - Returns 1 if bits are different
# a ^ b = 1010 ^ 0100 = 1110 = 14
print(a ^ b)  # Output: 14
# Use: Toggling bits, detecting differences

# >> (Right Shift) - Shifts bits right by n positions (divides by 2^n)
# a >> 2 = 1010 >> 2 = 0010 = 2 (10 / 4) 
#Before:  1 0 1 0
#Shift 1:   1 0 1
#Shift 2:     1 0

print(a >> 2)  # Output: 2
# Use: Efficient division by powers of 2

# << (Left Shift) - Shifts bits left by n positions (multiplies by 2^n)
# a << 2 = 1010 << 2 = 101000 = 40 (10 * 4)
print(a << 2)  # Output: 40
# Use: Efficient multiplication by powers of 2


#precedence
#Precedence and Associativity of Operators
#Python, Operator precedence and associativity determine the priorities of the operator
expr = 10 + 20 * 30
print(expr)      # * has higher precedence than +, so multiplication is performed first.
name = "Alex"
age = 0

if name == "Alex" or name == "John" and age >= 2:
    print("Hello! Welcome.")  #and has higher precedence than or, so the age check is performed first.
else:
    print("Good Bye!!")



def prob(a,b,flag):
    if (a>=0 and a<0) or (a<0 and b>=0) and flag ==True:
        return "True"
    else:
        return "false"
print(prob(-1,2,True))        