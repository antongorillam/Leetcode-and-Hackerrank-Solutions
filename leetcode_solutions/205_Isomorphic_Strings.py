class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        s_map = {}
        t_map = {}
        
        for i in range(n):
            
            if (s[i] in s_map) ^ (t[i] in t_map): 
                return False
            
            if (s[i] in s_map) and (t[i] in t_map) and \
                (s_map[s[i]] != t_map[t[i]]): 
                return False
        
            if s[i] not in s_map:
                s_map[s[i]] = i
        
            if t[i] not in t_map:
                t_map[t[i]] = i
        
        return True

"""
Problem link: https://leetcode.com/problems/isomorphic-strings/

Idea: We can transform a string to a list, eg. f("egg") = [0,1,1]. The number in the string is arbitrary, 
as long as it preserves the its structure. The function can be implemented with a hashfunction and works basically like this:
    - Loop through the string.
    - If the character haven't been seen previously (eg. not in hashmap), add it, with a arbitrary number.
    - If the character exist, assign the number its corresponding to it.

With this algorithm, f("egg") = f("add") = "011"
"""