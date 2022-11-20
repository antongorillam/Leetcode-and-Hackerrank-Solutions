# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Count how long the linked list is
        counter = head
        cnt = 0
        while counter:
            cnt += 1
            counter = counter.next
        
        # Get middle
        mid = (cnt // 2)
        
        # Traverse to middle and return it
        for _ in range(mid):
            head = head.next
            
        return head