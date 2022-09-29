# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        # Handles 3 edge cases
        if root== None:
            return True
        
        q = [(root.left, root.right)]
        
        while len(q) > 0:
        
            (l_child, r_child) = q.pop(0)

            # If both are None, it its valid
            if (l_child==None) and (r_child==None):
                continue
            # All cases when it is false
            elif (l_child==None) ^ (r_child==None):
                # False case: Only one is None
                return False
            elif (l_child.val!=r_child.val):
                return False
            else:
                # Valid leaf, no None so add to queue
                q.append((l_child.left, r_child.right))
                q.append((l_child.right, r_child.left))
                                
        return True

            
