class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        basket = Counter()
        
        ans = 0
        
        for index, fruit in enumerate(fruits):
            basket[fruit] += 1
            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if not basket[fruits[left]]:
                    del basket[fruits[left]]
                left += 1
            
            ans = max(index - left + 1, ans)
        
        return ans