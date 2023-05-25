class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        n = len(accounts)
        rank = [1] * n
        for i in range(n):
            parent[i] = i
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            parent_x = find(x)
            parent_y = find(y)
            if parent_x != parent_y:
                if rank[parent_x] >= rank[parent_y]:
                    rank[parent_x] += rank[parent_y]
                    parent[parent_y] = parent[parent_x]
                else:
                    rank[parent_y] += rank[parent_x]
                    parent[parent_x] = parent[parent_y]
           
        for i in range(n):
            email = set(accounts[i][1:])
            for j in range(i + 1, n):
                if email & set(accounts[j]):
                    union(i, j)
        
        visited = set()
        count = 0
        ans = [] 
        for i in range(n):
            common = set() 
            if i not in visited:
                ans.append([accounts[i][0]])
            for j in range(i, n):
                if find(i) == find(j) and j not in visited:
                    for email in accounts[j][1:]:
                        common.add(email)
                        visited.add(j)
            ans[-1].extend(sorted(common))
        return ans