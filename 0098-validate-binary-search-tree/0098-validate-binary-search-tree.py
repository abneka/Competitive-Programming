# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        array = self.traverse(root)
        return all(array[index] > array[index - 1] for index in range(1, len(array)))
    
    def traverse(self, root):
        if not root:
            return []
        
        array = []
        
        array.extend(self.traverse(root.left))
        array.append(root.val)
        array.extend(self.traverse(root.right))
        
        return array
    