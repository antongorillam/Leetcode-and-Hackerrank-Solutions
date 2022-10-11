class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # Leaf node
        if root == None:
            return 0
        
        return max(
            self.maxDepth(root.left) + 1, 
            self.maxDepth(root.right) + 1
        )

"""
Problem: https://leetcode.com/problems/maximum-depth-of-binary-tree/

Idea: Regular DFS. Call the function recusively for each child, 
and return the max height. 

"""