class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        heap = []
        
        for num in nums:
            while heap:
                val, leng = heap[0]
                if val + 1 == num:
                    heapreplace(heap,(num,leng+1))
                    break
                elif val == num:
                    heappush(heap,(num,1))
                    break
                else:
                    if leng < 3:
                        return False
                    heappop(heap)
            else:
                heappush(heap,(num,1))
                
        for i in range(len(heap)):
            num,leng = heap[i]
            if leng < 3:
                return False
        return True