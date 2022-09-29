class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_2_idx = {}
        for i in range(len(nums)):
            res = target - nums[i]
            nums_2_idx[res] = i
        
        for i in range(len(nums)):
            if nums[i] in nums_2_idx and i != nums_2_idx[nums[i]]:
                # If the number exist and is NOT iteslf,
                # then we have found our answer
                return [i, nums_2_idx[nums[i]]]

""" 
Problem: https://leetcode.com/problems/two-sum/

Idea: It is easy to bruteforce O(n^2), but using hashtables can reduce it to O(n), while it might increase memory complexity a bit.

1. Loop over nums and save the results in a hashtable with value as key (I choosed to save the residual from the target, but does not matter)
2. Loop over nums once again, but this time we use to hashtable to check if the corresponding answer exist, which is O(1).

"""