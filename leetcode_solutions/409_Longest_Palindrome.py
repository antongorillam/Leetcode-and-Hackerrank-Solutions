class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        freq = {}
        
        # Create a dictonary that maps: letter -> frequency
        for char in s:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1
        
        # Count the number of characters that have odd frequency number
        odd_freq = 0
        for _, value in freq.items():
            if value % 2 == 1:
                odd_freq += 1
        
        if odd_freq < 2:
            # If the amount of oddly numbered character are less than 2, 
            # no characters need to be removed
            return len(s)
        else:
            # Remove the number of oddly numbered but one to make a palidrome  
            return len(s) - odd_freq + 1

"""
Problem link: https://leetcode.com/problems/longest-palindrome/

Idea: 

Understand a couple of things:
    - If a character occurs an even number of time -> we can always build a palidrome
    - There can only be one oddly numbered characters in a palidrome. If there's more we have to remove a character to make it even.
    - The length of longest palidrome is the length of the string, subtracting the number of characters from the oddly numbered characters to make a palidrome, eg. len(s) - oddly_numbered_char + 1

Time-complexity: O(n)
Space-complexity: O(n)
"""