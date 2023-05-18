from typing import List


from typing import List

from collections import defaultdict
from collections import deque


class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        # code here
        graph = defaultdict(list)
        indeg = defaultdict(int)
        
        for indep, dep in edges:
            graph[indep].append(dep)
            indeg[dep] += 1
        
        queue = deque()
        visited = set()
        time = [0] * n
        
        for node in range(n):
            if not indeg[node + 1]:
                queue.append(node + 1)
        
        count = 1
        # print(queue)
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                visited.add(node)
                # print(node + 1, count)
                time[node - 1] = count
                
                for job in graph[node]:
                    indeg[job] -= 1
                    if not indeg[job]  and job not in visited:
                        queue.append(job)
            
            count += 1
        
        return ' '.join(map(str, time[:]))



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        edges=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.minimumTime(a[0],a[1], edges)
        
        print(res)
        

# } Driver Code Ends
