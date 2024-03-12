import sys
sys.path.append('/Q_791_Custom_Sort_String_MEDIUM')  # Replace this with the actual path.

from Q_791_Custom_Sort_String_MEDIUM.Solution import Ans

if __name__ == "__main__":
    
    testCase1 = "kqep"
    testCase2 = "pekeq"
    
    testFunction = Ans.Solution()
    
    a = testFunction.customSortString(testCase1,testCase2)
    
    print(a)