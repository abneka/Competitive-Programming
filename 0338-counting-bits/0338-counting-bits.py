class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []

        def count_ones(num):
            if not num:
                return 0
            
            if num == 1:
                return 1
            
            count = num & 1
            
            return count_ones(num // 2) + count

        for num in range(0, n + 1):
            ans.append(count_ones(num))

        return ans