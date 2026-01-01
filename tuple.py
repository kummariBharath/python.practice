#tuples are unmutable(not changeable by inseration)
mytuple = ("MAX",28,"BOSTON")
print(type(mytuple))

item=mytuple[-2]
print(mytuple)
if "MAX" in mytuple:
    print("yes")
else:
    print("no")

print(len(mytuple))
a=(1,2,3,4,5,6,7,78,9)
b=a[::-2]
print(b)

my_tuple=(0,1,2,3,4)
i1,*i2,i3 =my_tuple   #here observe the *i2 takes the 3 elements and put into together as tuple
print(i1)
print(i2)
print(i3)
k= mytuple.__sizeof__()
k=mytuple.__getattribute__("index")("BOSTON")
print(k)
#count()
imp_person_life=('bharath','navya','shivani','sumit','bharath')
k=imp_person_life.count('bharath')
print(k)
'navya'in imp_person_life
'sumit'in imp_person_life