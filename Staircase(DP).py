# Recursive way without memorization takes O(2^n) time complexity and O(n) space complexity due to the call stack.
def climb_staircase_(n):
    if n<=2:
        return n 
    return climb_staircase_(n-1) + climb_staircase_(n-2)
print(climb_staircase_(5))

#Memorization way better than the recursive way takes O(n) time complexity and O(n) space complexity due to the call stack and the memoization dictionary.
def memorization(n,memo={}):
    if n in memo:
        return memo[n] #returns the value in the memoization dictionary if it exists
    if n<=2:
        return n
    
    memo[n] = memorization(n-1,memo) + memorization(n-2,memo) #stores the value in the memoization dictionary before returning it
    return memo[n]
print(memorization(5))