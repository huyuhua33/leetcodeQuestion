import sys
sys.path.append('/Q_349_Intersection_of_Two_Arrays')  # Replace this with the actual path.

from Q_349_Intersection_of_Two_Arrays.Solution import Ans

if __name__ == "__main__":
    
    testCase1 = [4,7,9,7,6,7] 
    testCase2 = [5,0,0,6,1,6,2,2,4]
    
    testFunction = Ans.Solution()
    
    a = testFunction.intersection(testCase1,testCase2)
    
    print(a)