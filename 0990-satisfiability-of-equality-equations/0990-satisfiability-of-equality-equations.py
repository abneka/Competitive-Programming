class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {chr(char):chr(char) for char in range(ord('a'), ord('z') + 1)}
        rank = [1 for char in range(ord('a'), ord('z') + 1)]
        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]
        def union(node1, node2):
            parent1 = find(node1)
            parent2 = find(node2)
            
            if parent1 == parent2: return
            
            if rank[ord(parent1) - 97] > rank[ord(parent2) - 97]:
                parent[parent2] = parent1
                rank[ord(parent1) - 97] += rank[ord(parent2) - 97]
            
            else:
                parent[parent1] = parent2
                rank[ord(parent2) - 97] += rank[ord(parent1) - 97]
        
        inequal = []
        
        for equation in equations:
            if equation[1] == '!':
                inequal.append((equation[0], equation[3]))
                continue
            
            union(equation[0], equation[3])
        
        return all(find(a) != find(b) for a, b in inequal)