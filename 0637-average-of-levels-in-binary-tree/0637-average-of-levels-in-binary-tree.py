# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque()
        queue.append(root)
        
        result = []
        
        while queue:
            new = []
            total = 0
            length = 0
            
            while queue:
                node = queue.popleft()
                total += node.val
                length += 1
                if node.left:
                    new.append(node.left)
                if node.right:
                    new.append(node.right)
            
            result.append(total/length)
            queue.extend(new)
            
        return result
    