# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Edge case if one linked list is empty
        if not list1: return list2
        if not list2: return list1
        
        # Create Dummy node
        cur_node = head = ListNode()
        
        while list1 and list2:
    
            if list2.val >= list1.val:
                cur_node.next = list1
                list1 = list1.next
            else:
                cur_node.next = list2
                list2 = list2.next
            cur_node = cur_node.next
        
        # One element will always be left, handle if
        if list1:
            cur_node.next = list1
            cur_node = cur_node.next
        if list2:
            cur_node.next = list2
            cur_node = cur_node.next
        
        return head.next
                
"""
Problem link: https://leetcode.com/problems/merge-two-sorted-lists/

Idea: Had quite a hard time with this one, but when I got the idea to create a dummy node, then its quite straight forward.

Quite many edge cases if porly designed

Improvements: Perhaps rewrite loop so that last if statements would not be needed.
"""