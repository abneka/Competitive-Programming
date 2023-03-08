# Definition for a binary tree node.
# class TreeNode:
#     def init(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ans = []
        # ********************************************************
        def findSuccesor(root, depth):
            nonlocal ans
            if not root:
                return None
            if not depth:
                if ans and ans[-1] == root.val:
                    return None
                ans.append(root.val)
                return None
            
            if root and root.right:
                findSuccesor(root.right, depth - 1)

            if root and root.left:
                findSuccesor(root.left, depth - 1)
        
        # *******************************************************
        
        def findTarget(root, depth, target, k):
            nonlocal ans
            if not root:
                return 0
            
            if root.val == target.val:
                # print('found')
                findSuccesor(root, k)
                return 1
            
            left = findTarget(root.left, depth + 1, target, k)
            
            right = findTarget(root.right, depth + 1, target, k)
            
            if left:
                if k - (1  + left) > -1:
                    findSuccesor(root.right, k - (1  + left))
                if left == k:
                    ans.append(root.val)
                return left + 1
            
            if right:
                if k - (1 + right) > -1:
                    findSuccesor(root.left, k - (1 + right))
                if right == k:
                    ans.append(root.val)
                return right + 1
        findTarget(root, 0, target, k)
            
        return ans