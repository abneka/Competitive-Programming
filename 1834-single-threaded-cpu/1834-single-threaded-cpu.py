class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [task + [index] for index, task in enumerate(tasks)]
        tasks = sorted(tasks, key = lambda x:x[0])
        time = tasks[0][0]
        curr = 0
        heap = []
        ans = []
        length = len(tasks)
        
        while heap or curr < length:
            while curr < length and tasks[curr][0] <= time:
                heappush(heap, [tasks[curr][1], tasks[curr][2]])
                curr += 1
            
            if not heap:
                time = tasks[curr][0]
            
            else:
                process, task = heappop(heap)
                time += process
                ans.append(task)
                
        return ans
