#identity  with diagonnal as 2
n=4
for i in range(n):
    for j in range(n):
        if i==j:
            print("2",end="")
        else:
            print("0",end="")
    print()