# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        if root:
            queue.append(root)
        
        result = []
        
        while queue:
            queue_size = len(queue)
            level = []
            
            while queue_size:
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                    
                queue_size -= 1
            result.append(level)
            
        return result