def climb_staircase_(n):
    if n<=2:
        return n 
    return climb_staircase_(n-1) + climb_staircase_(n-2)
print(climb_staircase_(5))