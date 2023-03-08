# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def constructBST(index):
            if not index + 1:
                return None
            
            if index == length:
                return None
            
            node = TreeNode(nums[index])
            
            if index - 1 < mid:
                node.left = self.sortedArrayToBST(nums[:index])
            
            if index + 1 > mid:
                node.right = self.sortedArrayToBST(nums[index + 1:])
            
            return node
    
        length = len(nums)
        mid = length // 2
        return constructBST(mid)