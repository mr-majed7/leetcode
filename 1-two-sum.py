class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = []
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j]==target-nums[i]:
                    return[i,j]       