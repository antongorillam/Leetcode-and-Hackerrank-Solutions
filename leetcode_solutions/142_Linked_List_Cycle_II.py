Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        node_map = {}
        
        if head == None:
            return None
        
        while head.next:
            node_map[hash(head)] = True
            head = head.next
            if node_map.get(hash(head)):
                return head
            
        return None