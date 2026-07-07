class Solution:
    def pattern(self,N):
        for i in range(N):
            for j in range(N):
                print("*",end=' ')
            print()  
sol=Solution()
N=4              
sol.pattern(N)


class Solution:
    def pattern6(self, n):
        for i in range(n):
            for j in range(n,i,-1):
                print(n-j+1,end='')
            print()    
dal=Solution()
n=4
dal.pattern6(n)


class Solution:
    def pattern7(self, n):
        for i in range(n):
            for j in range(n-i-1):
                print(' ',end='')
            for j in range(2*i+1):
                print('*',end='')
            for j in range(n-i-1):
                print(' ',end='')    
            print()
        print()   
cal=Solution()
n=10
cal.pattern7(n)

class Solution

                 