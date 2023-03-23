# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        count = defaultdict(list)
        count[0].append(root.val)
        
        def findPosition(root, depth, position):     
            if not root.left and not root.right:
                return
            
            if root.left:
                count[depth].append((root.left.val, 2 * position))
                findPosition(root.left, depth + 1, 2 * position)
                
            if root.right:
                count[depth].append((root.right.val, 2 * position+ 1))
                findPosition(root.right, depth + 1, 2 * position + 1) 
        
        findPosition(root,1, 1)
        return count.values()
    
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int: 
        num_with_position = self.levelOrder(root)
        ans = 1
        
        for index, level in enumerate(num_with_position):
            if not index:
                continue
            
            left = level[0][1]
            right = level[0][1]
            
            for pos in level:
                left = min(left, pos[1])
                right = max(right, pos[1])
                
                ans = max(right - left + 1, ans)
        return ans