things_to_change=["attitude","behaviour","approach","perception"]
for thing in things_to_change:
    print(f'this are things to change:{thing}')
#simple iteration of string
for char in "bharath":
    print(char)    
#nested loop()
beauty=['hair','skin','nails']
health=['diet','excerise','sleep']
for b in beauty:
    for h in health:
        print(f'the secret of {b} is {h}')
#also use print(beauty,health)

#while loop
max=10
count=1
while count<=max:
    print(f'the count is :{count}')
    count+=1
guess_number=7
guess=1
print("guess the number between 1 to 10")
while guess!=guess_number:
    guess=int(input())
    if guess<guess_number:
        print("too low")
    elif guess>guess_number:
        print("too high")
    else:
        print("your guessed it right") 

deveolpers=["bharath","shivani","navya","sumit"]
for dev in deveolpers:
     if dev=="bharath":
         print(f'{dev} is selected')
         break