class Solution:
    def __init__(self):
        pass
                
    def pivotInteger(self, n: int) -> int:
        sum1 = 0
        
        for i in range(n):
            sum2 = 0
            sum1 += i
            for j in range(i,n):
                sum2 += j
                print(sum2)          
            if sum2 == sum1:
                return i
            else: 
                return -1