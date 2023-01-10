class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        
        even_sum = sum([even for even in nums if even % 2 == 0])
        
        for val, index in queries:
            num = nums[index]
            
            if num % 2 == 0:
                even_sum -= num
            
            num += val
            
            if num % 2 == 0:
                even_sum += num
            
            nums[index] = num
            result.append(even_sum)
        
        return result