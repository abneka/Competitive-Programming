# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        def traverse(root):
            if not root:
                return
            
            if root.left:
                graph[root.left.val].append(root.val)
                graph[root.val].append(root.left.val)
                traverse(root.left)
            if root.right:
                graph[root.right.val].append(root.val)
                graph[root.val].append(root.right.val)
                traverse(root.right)
        traverse(root)
        
        queue = deque([target.val])
        visited = set()
        visited.add(target.val)
        
        path = 0
        ans = []
        while queue:
            for i in range(len(queue)):
                temp = queue.popleft()
                
                if path == k:
                    ans.append(temp)
                
                for num in graph[temp]:
                    if num not in visited:
                        queue.append(num)
                        visited.add(num)
            path += 1
        return ans