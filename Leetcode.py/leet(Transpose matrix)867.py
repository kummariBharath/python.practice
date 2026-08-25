class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows=len(matrix)
        col=len(matrix[0])
        result=[[0]*rows for _ in range(col)]
        for i in range(rows):
            for j in range(col):
                result[j][i]=matrix[i][j]
        return result 

#Approaches and techniques used in above code:
# 1. Create a new matrix with dimensions swapped (rows become columns and vice versa).
# 2. Iterate through the original matrix and assign values to the new matrix in transposed positions.
# 3. Time complexity is O(m*n) where m is the number of rows and n is the number of columns in the original matrix.
# 4. The space complexity is O(m*n) because we are creating a new matrix to store the transposed values.    
    