class Solution:
    def __init__(self):
        self.roman_2_int_hash =  {
                "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000,
            }

    def romanToInt(self, s: str) -> int:
        
        # Total sum
        output_num = 0
        
        # Corner case, only one element in the string
        if len(s) == 1:
            return self.roman_2_int_hash[s[0]] 
        
        for i in range(len(s)-1):
            # Compare a element with the next one
            this_s = self.roman_2_int_hash[s[i]]
            next_s = self.roman_2_int_hash[s[i+1]]
            
            if this_s >= next_s:
                output_num += this_s
            else:
                output_num -= this_s
        
        # Add the last element which was ignored in the loop
        output_num += next_s 
        
        return output_num

"""
Problem: https://leetcode.com/problems/roman-to-integer/

Idea: Important to understand that, if the next character is  

1. Loop over nums and save the results in a hashtable with value as key (I choosed to save the residual from the target, but does not matter)
2. Loop over nums once again, but this time we use to hashtable to check if the corresponding answer exist, which is O(1).

"""