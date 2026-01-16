#truty values are 0,[1],(9),{1;2},True,"hello"
#falsy values are 0.0,[],(),{},False,""

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