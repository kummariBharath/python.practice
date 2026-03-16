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



#Bottom-up Approach
