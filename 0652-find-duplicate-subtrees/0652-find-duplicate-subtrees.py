# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtree = defaultdict(int)
        result = []
        
        def dp(node):
            if not node:
                return ' '
            
            substr = str(node.val) +'-'+ dp(node.left) +'-'+ dp(node.right)
            subtree[substr] += 1
            
            if subtree[substr] == 2:
                print(substr)
                result.append(node)
            
            return substr
        print(subtree)
        dp(root)
        return result