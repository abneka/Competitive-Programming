class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [task + [index] for index, task in enumerate(tasks)]
        tasks = sorted(tasks, key = lambda x:x[0])
        time = tasks[0][0]
        curr = 0
        heap = []
        ans = []
        length = len(tasks)
        print(tasks)
        while curr < length:
            enq, process, index = tasks[curr]
            if enq <= time:
                heappush(heap, [process, index])
                curr += 1
                continue
                
            if not heap:
                time = tasks[curr][0]
                continue
            
            process, task = heappop(heap)
            time += process
            ans.append(task)
            
            
        while heap:
            process, task = heappop(heap)
            ans.append(task)
        
        return ans
