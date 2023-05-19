class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []

        for row in matrix:
            for val in row:
                heappush(heap, val)

        for _ in range(k-1):
            heapq.heappop(heap)

        return heapq.heappop(heap)