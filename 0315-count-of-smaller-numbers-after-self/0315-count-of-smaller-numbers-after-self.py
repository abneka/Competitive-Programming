class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        
        def merge(new_nums): 
            if len(new_nums) == 1:
                return new_nums
            
            left = merge(new_nums[:len(new_nums)//2])
            right = merge(new_nums[len(new_nums)//2:])
            
            ans = []
            l = r = 0
            while r < len(right) or l < len(left):
                
                if r >= len(right) or ((l < len(left)) and (nums[left[l]] <= nums[right[r]])):
                    result[left[l]] += len(ans) - l                   
                    ans.append(left[l])
                    l += 1
                else:
                    ans.append(right[r])
                    r += 1
            return ans

        merge([i for i in range(len(nums))])
        return result