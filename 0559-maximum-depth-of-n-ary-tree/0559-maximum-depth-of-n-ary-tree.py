"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        def maxDepth(root, depth):
            if not root:
                return depth
            
            maxi = depth
            for child in root.children:
                maxi = max(maxDepth(child, depth + 1), maxi)
            
            return maxi
        
        return maxDepth(root, 1)