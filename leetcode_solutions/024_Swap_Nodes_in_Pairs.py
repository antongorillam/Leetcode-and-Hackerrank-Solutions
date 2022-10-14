# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Save the first head to return
        first_head = head
        
        # Look at 2 nodes at a time
        while head and head.next:
            # Swapping values
            temp_val = head.val
            head.val = head.next.val
            head.next.val = temp_val
            # "skips" over a node
            head = head.next.next
        
        return first_head

"""
Problem link: https://leetcode.com/problems/swap-nodes-in-pairs/

Idea: Always look at 2 node at a time.
"""