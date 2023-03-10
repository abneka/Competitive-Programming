# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        count = 0

        def countNodes(root):
            nonlocal count

            if not root:
                return (0,0)

            left = countNodes(root.left)
            right = countNodes(root.right)

            total = root.val + left[0] + right[0]
            nodes = left[1] + right[1] + 1

            avarage = total // nodes

            if avarage == root.val:
                count += 1
            
            return (total, nodes)
        
        countNodes(root)

        return count