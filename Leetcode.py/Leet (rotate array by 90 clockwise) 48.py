class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

        for i in range(n):
            for j in range(n//2):
                matrix[i][j],matrix[i][n-j-1]=matrix[i][n-j-1],matrix[i][j]
 
#Approach for above
#1. Transpose the matrix (swap rows with columns)

#2. Reverse each row of the transposed matrix(first row becomes last row and so on)

#3. Time complexity is O(n^2) because we are iterating through the matrix twice, once for transposing and once for reversing the rows.
#(how O(n^2) is derived: The first loop runs n times and the second loop runs n/2 times for each row,
#  resulting in a total of n * (n/2) = n^2/2 operations, which simplifies to O(n^2).)
#4. The space complexity is O(1) because we are modifying the matrix in place without using any additional data structures.
   