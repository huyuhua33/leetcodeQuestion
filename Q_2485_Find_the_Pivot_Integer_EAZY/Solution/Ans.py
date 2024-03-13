class Solution:
    def __init__(self):
        pass
    
    def pivotInteger(self, n: int) -> int:
        sum1 = 0
        
        for i in range(1,n+1):
            sum2 = 0
            sum1 += i
            for j in range(i,n+1):
                sum2 += j
            if sum2 == sum1:
                return i
        return -1