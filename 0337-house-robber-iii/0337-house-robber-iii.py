# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        
        def rob(root, skip):
            if not root:
                return 0
            
            state = (root, skip)
            
            if state not in memo:
                if skip:
                    memo[state] = rob(root.left, not skip) + rob(root.right, not skip)
                else:
                    rob_later = memo[state] = rob(root.left, skip) + rob(root.right, skip)
                    rob_now = memo[state] = rob(root.left, not skip) + rob(root.right, not skip) + root.val
                    memo[state] = max(rob_later, rob_now)
            
            return memo[state]
        
        return max(rob(root, False), rob(root, True))