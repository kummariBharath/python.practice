with open("bharath.txt","r") as f:
    data=f.read()

new_data=data.replace("python","java") #replacing python with java
print(new_data)

with open("bharath.txt","w") as f:
    f.write(new_data)


    