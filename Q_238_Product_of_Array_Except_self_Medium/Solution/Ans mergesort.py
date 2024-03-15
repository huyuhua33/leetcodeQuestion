class Solution:
    def __init__(self):
        pass
    def meargeSort(self,numsSub:list[int],setindex:int = -1) -> int:
        if setindex == -1:
            index = int(len(numsSub) /2)
            if index == 0:
                
                if numsSub == []:
                    return 1
                return numsSub[0]
        else:
            index = setindex
        # only have one for each err (left right) return that arr
        
        # get right
        if setindex == -1:
            ccc = numsSub[index:]
        else :
            ccc = numsSub[index +1:]

        dataL = self.meargeSort(ccc)

        # get left 
        bbb = numsSub[:index]

        dataR = self.meargeSort(bbb)
        combineed = dataR * dataL
        return combineed
     
    def productExceptSelf(self, nums: list[int]) -> list[int]:
    # require O(n)
        output = []
        count = 1

        for i in range(len(nums)):
            count = self.meargeSort(nums,i)
            output.append(count)
        print(output)
            
        return output