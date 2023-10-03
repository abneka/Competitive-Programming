class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = []
        heapq.heappush(heap, (k - 1, 0))
        cons = [[] for _ in range(n)]
        dis = [inf for _ in range(n)]
        dis[k - 1] = 0

        for u, v, t in times:
            cons[u - 1].append((v - 1, t)) 

        while heap:
            u, curDis = heapq.heappop(heap)
            for v, d in cons[u]:
                nextDis = curDis + d
                if nextDis < dis[v]:
                    dis[v] = nextDis
                    heapq.heappush(heap, (v, nextDis))
        
        if any(d == inf for d in dis):
            return -1

        return max(dis)