# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0
        
        def checkPath(root, prefix, total):
            nonlocal ans
            if not root:
                return
            
            total += root.val
            ans += prefix[total - targetSum]
                
            prefix[total] += 1
            
            checkPath(root.right, prefix, total)
            checkPath(root.left, prefix, total)
            
            prefix[total] -= 1
            
        prefix = Counter([0])
        
        checkPath(root, prefix, 0)
        
        return ans