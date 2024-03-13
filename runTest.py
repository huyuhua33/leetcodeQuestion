import sys
sys.path.append('/Q_2485_Find_the_Pivot_Integer_EAZY/Solution')  # Replace this with the actual path.

from Q_2485_Find_the_Pivot_Integer_EAZY.Solution import Ans

if __name__ == "__main__":
    
    testCase1 = 8
    
    testFunction = Ans.Solution()
    
    a = testFunction.pivotInteger(testCase1)
    
    print(a)