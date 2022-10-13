# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        while head:
            temp = head.next # Save the next node
            head.next = prev # Point to previous node
            prev = head # Previous node to current node 
            head = temp # Move current node to next node
            
        return prev

"""
Problem link: https://leetcode.com/problems/reverse-linked-list/

Idea: Loop through LL and direct pointer to the previous node

Hardest part is the order:
    1. Save the coming node
    2. Redirect the current node pointer to the previous node
    3. Move previous node to the current node
    4. Move current node to the next node
"""