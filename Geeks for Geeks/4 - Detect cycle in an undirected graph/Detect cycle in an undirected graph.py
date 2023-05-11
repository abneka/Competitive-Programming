from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		memo = [True] * V
		def dfs(vertex,prev):
		    memo[vertex] = False
		    
		    for neigh in adj[vertex]:
		        if neigh != prev:
		            if not memo[neigh] or not dfs(neigh,vertex):
    		            return False
    		            
		    memo[vertex] = True
		    return True
	    
	    for i in range(V):
            if not dfs(i,-1):
                return 1
	    return 0
		#Code here


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends
