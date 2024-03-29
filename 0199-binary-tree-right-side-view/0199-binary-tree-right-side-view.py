# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        count = defaultdict(list)

        def groupLevel(root, depth):
            if not root:
                return 

            count[depth].append(root.val)

            groupLevel(root.left, depth + 1)
            groupLevel(root.right, depth + 1)
        
        groupLevel(root, 0)

        return [right_vals[-1] for right_vals in count.values()]