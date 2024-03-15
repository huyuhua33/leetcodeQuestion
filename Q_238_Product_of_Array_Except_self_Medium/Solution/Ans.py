class Solution:
    def __init__(self):
        pass

    def productExceptSelf(self, nums: list[int]) -> list[int]:
    # require O(n)
        # [1,1,1,1,1]
        ans = [1] * len(nums)

        # 存左到右 p = 已經乘過的數
        p = 1
        for i in range(len(nums)):
            ans[i] = p
            p *=  nums[i]
            print(f"ans[{i}] = {ans[i]} , p = {p}")

        # 存右到左 p = 已經乘過的數並與左翼相乘
        p = 1
        for i in reversed(range(len(nums))):
            ans[i] *= p
            p *=  nums[i]
            
            
            print(f"r : ans[{i}] = {ans[i]} , p = {p}")


        return ans