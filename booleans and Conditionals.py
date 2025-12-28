print(3>4)
print(3<4)
print(3!=4)

age=150
if age<=100:
    print('you are human')

grade=int(input('enter your grade:'))
if grade  >65:
    print('B')
elif grade >=30:
    print('C')
else:           
    print('F')

#multiplle conditions to be checked

is_citizen =bool(input("are you a citizen:"))
age=int(input("enter your age:"))
if is_citizen and age >=18: # tt=true
    print('eligible to vote')
else:
    print("no you are teenager person") 

#or condition
print(age or is_citizen)
