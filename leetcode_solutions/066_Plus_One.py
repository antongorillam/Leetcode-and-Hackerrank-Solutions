class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        size = len(digits)
        for i in range(size-1, -1, -1):
            # Loop from the back to the front
            if digits[i]==9 and i==0:
                # If the we are on the largest digit and its a 9
                digits[i] = 0
                digits = [1] + digits

            elif digits[i]==9:
                digits[i] = 0
            
            else:
                digits[i] += 1
                break
            
        return digits

"""
Problem link: https://leetcode.com/problems/plus-one/

Idea: While looping throught the list from reverse, there are only 3 cases:

Case 1: We are on the "last" digit (eg. index=0) and its a 9. We therefore need to extend the list with 1 more position 

Case 2: The digit is a 9, thus we need a carry over (eg. the loops continues)

Case 3: If the number is not a 9, then just add 1 and break the loop.
"""