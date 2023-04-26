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
            level_size = len(queue)
            total = 0
            length = 0
            
            while level_size:
                node = queue.popleft()
                total += node.val
                length += 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level_size -= 1
            
            result.append(total/length)
            
        return result
    