#with open("bharath.txt","r") as f:
 #   data=f.read()

#new_data=data.replace("python","java") #replacing python with java
#print(new_data)

#with open("bharath.txt","w") as f:
#    f.write(new_data)

#finding the word "learning"
word="learning"
with open("bharath.txt","r") as f:
    data=f.read()
    if(data.find(word)): #word in data 
        print("found")
    else:
        print("not found")   

def check_for_line():
    word="learning"
    data=True
    line_no=1
    with open("bharath.txt","r") as f:
        while data:
            data = f.readline()
            if (word in data):
                print(line_no)
                return
            line_no+=1        
    return -1
check_for_line()

tuple(data)
print(data)