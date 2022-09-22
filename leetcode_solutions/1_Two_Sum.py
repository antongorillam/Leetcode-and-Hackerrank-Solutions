class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_2_idx = {}
        for i in range(len(nums)):
            res = target - nums[i]
            nums_2_idx[res] = i
        
        for i in range(len(nums)):
            if nums[i] in nums_2_idx and i != nums_2_idx[nums[i]]:
                # We have found our answer
                return [i, nums_2_idx[nums[i]]]
