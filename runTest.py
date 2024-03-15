import sys
sys.path.append('/Q_238_Product_of_Array_Except_self_Medium/Solution')  # Replace this with the actual path.

from Q_238_Product_of_Array_Except_self_Medium.Solution import Ans

if __name__ == "__main__":
    
    # testCase1 = [-1,1,0,-3,3]
    testCase2 = [1,2,3,4]
    testFunction = Ans.Solution()
    
    a = testFunction.productExceptSelf(testCase2)
    # a = testFunction.meargeSort(testCase2,3)
    print(a)


    # 1 2 3 / 4 5 6 7 len = 6
    # index = 3
    # dataR = 4,5,6,7
    #     index = 2
    #     dataR = 7
    #     dataL = 4 5
    #         index



    # dataL = nums[0:3]

