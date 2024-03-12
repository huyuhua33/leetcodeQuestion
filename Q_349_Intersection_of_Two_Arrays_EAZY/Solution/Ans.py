class Solution:
    def __init__(self):
        pass
        
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans = []
        ans2 = []
        for i in nums1:
            # i in nums1
            if i not in ans:
                ans.append(i)
                
        for i in ans:
            if i in nums2:
                ans2.append(i)

        return ans2
    
    def intersection2(self, nums1: list[int], nums2: list[int]) -> list[int]:
        x = set(nums1)
        y = set(nums2)
        return list(y-(y-x))