class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        
        memo = Counter()

        def count_ones(num):
            if not num:
                return 0
            
            if num == 1:
                return 1
            
            if memo[num]:
                return memo[num] - 1
            
            count = num & 1
            memo[num] = count_ones(num // 2) + count + 1
            return memo[num] - 1

        for num in range(0, n + 1):
            ans.append(count_ones(num))

        return ans