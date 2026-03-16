# Recursive way without memorization takes O(2^n) time complexity and O(n) space complexity due to the call stack.
from typing import Final


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

# trace through the execution of climb_stairs(5) with the top-down approach to see how memoization eliminates redundant work:

#Call: climb_stairs_memo(5)
 # memo = {} (empty)
  
  #Call: climb_stairs_memo(4) 
   # memo = {} (empty)
    
    #Call: climb_stairs_memo(3)
     # memo = {} (empty)
      
      #Call: climb_stairs_memo(2) → returns 2 (base case)
      #Call: climb_stairs_memo(1) → returns 1 (base case)
      
      #Result: 2 + 1 = 3
      #memo = {3: 3} (stored!)
    
    #Call: climb_stairs_memo(2) → returns 2 (base case)
    
    #Result: 3 + 2 = 5
   # memo = {3: 3, 4: 5} (stored!)
  
 # Call: climb_stairs_memo(3) → returns 3 (FROM MEMO - no recursion!)
  
 # Result: 5 + 3 = 8
 # memo = {3: 3, 4: 5, 5: 8}



#Tabulation (Bottom-Up Approach)
#Tabulation builds the solution from the ground up, filling a table with solutions to subproblems

def climb_stairs_tabulation(n):
    if n<=2:
        return n
    #create a array for storing the elements from 0 to n
    dp = [0]*(n+1)
    dp[1]=1 # as climbing 1 step take 1 way
    dp[2]=2 # as climmbing 2 steps takes 2 ways i..e 1+1 ,2

    for i in range(3,n+1):# staring from 3
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
print(climb_stairs_tabulation(5))   
print(climb_stairs_tabulation(6)) 
#tracing through the execution of climb_stairs_tabulation(5):
# Initial state:
#dp = [0, 1, 2, 0, 0, 0]
 #    [0, 1, 2, 3, 4, 5] ← indices (step numbers)

#Step by step construction:
#
#i = 3:
 # dp[3] = dp[2] + dp[1] = 2 + 1 = 3
 # dp = [0, 1, 2, 3, 0, 0]
  
#i = 4:
 # dp[4] = dp[3] + dp[2] = 3 + 2 = 5
  #dp = [0, 1, 2, 3, 5, 0]
  
#i = 5:
  #dp[5] = dp[4] + dp[3] = 5 + 3 = 8
 # dp = [0, 1, 2, 3, 5, 8]

#Final result: dp[5] = 8     
