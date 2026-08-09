class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's ALgo
        MAX,SUM = float('-inf'),0
        for x in nums:
            SUM += x
            MAX = max(MAX,SUM)
            if SUM < 0: SUM = 0
        return MAX