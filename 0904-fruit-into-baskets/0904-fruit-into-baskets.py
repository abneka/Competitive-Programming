class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        basket = Counter()
        length = 0
        
        ans = 0
        
        for index, fruit in enumerate(fruits):
            
            if not basket[fruit]:
                length += 1
            
            basket[fruit] += 1
            
            while length > 2:
                basket[fruits[left]] -= 1
                if not basket[fruits[left]]:
                    length -= 1
                    del basket[fruits[left]]
                left += 1
            
            ans = max(index - left + 1, ans)
        
        return ans