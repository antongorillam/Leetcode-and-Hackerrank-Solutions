class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening_brackets = "([{"
        closing_brackets = ")]}"           
        
        for curr_s in s:
            if curr_s in opening_brackets:
                # If its an opening bracket, put in into the stack
                stack.append(curr_s)
            elif (curr_s in closing_brackets) and stack!=[]:
                # If its an closing bracket, check it with the last element from the stack
                last_s = stack.pop()
                if not (last_s=="(" and curr_s==")" or \
                        last_s=="[" and curr_s=="]" or \
                        last_s=="{" and curr_s=="}"):
                    return False
            else:
                return False 
        
        if stack==[]:
            return True
        else:
            return False

"""
Problem link: https://leetcode.com/problems/valid-parentheses/

Idea: Beacause we need to preserve the order, a stack should be used. As soon as I realized that, the task becomes easy.

There are x cases where it should fail:
- The closing bracket and the last element does not match.
- The stack is empty when encountering a opening bracket.
- The stack is not empty when we reach the end of the string
"""