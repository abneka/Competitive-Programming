class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # approach number one 
        
        # k = k % len(nums)
        # stack = nums[-k:]+nums[:-k]
        # nums.clear()
        # nums.extend(stack)
        
        # approach number two: using two pointers
        
        length = len(nums)
        k = k % length
        rotation_index = length - k
        cache = []
        apply_cache = False
        
        for step in range(length):
            
            if rotation_index == length:
                rotation_index = 0
                apply_cache = True
                
            if apply_cache:
                cache.append(nums[step])
                nums[step] = cache[rotation_index]
                rotation_index += 1
                continue
            
            cache.append(nums[step])
            nums[step] = nums[rotation_index]
            rotation_index += 1
            