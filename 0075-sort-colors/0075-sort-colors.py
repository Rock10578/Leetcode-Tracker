class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        for x in range(n-1):
            for y in range(x+1,n):
                if nums[x]>nums[y]:
                    nums[x],nums[y] = nums[y],nums[x]