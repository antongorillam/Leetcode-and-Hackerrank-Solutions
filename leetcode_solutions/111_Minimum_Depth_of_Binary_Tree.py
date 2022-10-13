class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        # First handle the edge case
        if root==None:
            return 0
        
        queue = []
        # The 2nd element of the tuple note what height we are on
        queue.append((root, 1)) 
        
        while len(queue) > 0:
            (node, current_height) = queue.pop(0)
            
            # If both nodes are none, then we have found the lowest height
            if (not node.left) and (not node.right):
                return current_height
                
            if node.left:
                l_node = node.left
                queue.append((l_node, current_height+1))
            
            if node.right:
                r_node = node.right
                queue.append((r_node, current_height+1))

"""
Problem link: https://leetcode.com/problems/reverse-linked-list/

Idea: Since we want to find the shortest height, bfs (breath-first-search) makes most sense, since it will check each "level" at a time.

1. Create a queue and proceed with a normal bfs, with only difference is that we track which heigh each node is on.
2. As soon as booth we find a leaf node (both children are None) then we know we have found the lowest height.

Time complexity: O(|V|)

"""