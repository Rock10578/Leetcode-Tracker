class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n,flag = len(nums),True
        for i in range(n-2,-1,-1):
            print(nums[i])
            if nums[i]<nums[i+1]:
                flag = False
                idx = min((j for j in range(i+1, len(nums)) if nums[j] > nums[i]), key=lambda j: nums[j], default=-1)
                nums[i],nums[idx] = nums[idx],nums[i]
                # SORTING
                for x in range(i+1,n-1):
                    minV = x
                    for y in range(x+1,n):
                        if nums[minV]>nums[y]:
                            minV = y
                    if x!=y:
                        nums[minV],nums[x] = nums[x],nums[minV]
                break
        if flag:
            for x in range(n-1):
                minV = x
                for y in range(x+1,n):
                    if nums[minV]>nums[y]:
                        minV = y
                if x!=y:
                    nums[minV],nums[x] = nums[x],nums[minV]