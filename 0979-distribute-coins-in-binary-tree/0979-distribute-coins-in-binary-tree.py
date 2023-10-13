# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dp(node):
            if not node:
                return (0,0)
            nonlocal ans
            
            coin_req_l, total_l = dp(node.left)
            coin_req_r, total_r = dp(node.right)
            
            ans += (abs(coin_req_l - total_l) + abs(coin_req_r - total_r))
            
            return (coin_req_l + coin_req_r + 1, total_l + total_r + node.val)
        dp(root)
        print(ans)
        return ans
