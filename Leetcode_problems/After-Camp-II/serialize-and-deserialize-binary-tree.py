# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        ans = []
        queue = deque([root])
        
        while queue:
            curr = queue.popleft()
            if curr:
                ans.append(str(curr.val))
                queue.append(curr.left)
                queue.append(curr.right)
            else:
                ans.append('null')
        
        return ' '.join(ans)
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        

    def deserialize(self, data):
        print(data)
        arr = list(data.split())
        if not arr or arr[0] == 'null':
            return None
        root = curr = TreeNode(arr[0])
        index = 1
        queue = deque([curr])
        def makeTree(index):
            if index >= len(arr) or arr[index] == 'null':
                return None
            
            return TreeNode(arr[index])
        while queue:
            curr = queue.popleft()
            print(curr.val, arr[index], arr[index + 1])
            curr.left = makeTree(index)
            curr.right = makeTree(index + 1)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            index += 2

        return root
        """Decodes your encoded arr to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))