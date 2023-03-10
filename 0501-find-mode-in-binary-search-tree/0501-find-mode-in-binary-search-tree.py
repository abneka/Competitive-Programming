# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = Counter()

        def countOccurence(root):
            if not root:
                return 

            count[root.val] += 1

            countOccurence(root.left)
            countOccurence(root.right)
        
        countOccurence(root)
        
        maxi = max(count.values())
        
        answer = []
        for key, value in count.items():
            if value == maxi:
                answer.append(key)
        
        return answer