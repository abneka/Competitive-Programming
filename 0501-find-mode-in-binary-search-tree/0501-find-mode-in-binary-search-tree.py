# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def Traverse(self, root):
        if root == None:
            return []
        array = [root.val]
        array += self.Traverse(root.left)
        array += self.Traverse(root.right)
        
        return array
    
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq = Counter(self.Traverse(root))
        maxi = max(freq.values())
        
        answer = []
        for key, value in freq.items():
            if value == maxi:
                answer.append(key)
        
        return answer
        