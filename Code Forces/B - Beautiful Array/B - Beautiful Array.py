size = int(input())
 
right = size - 1
left = 0
 
nums = list(map(int, input().split()))
nums.sort()
length = len(nums)
 
negative = []
positive = []
zeros = []
 
neg = 1
pos = 1
zero = 1
 
# while left < right:
 
pass_num = False
    
for index, num in enumerate(nums):
    if pass_num:
        positive.append(str(num))
        pass_num = False
        continue
    
    if pos * num > 0:
        positive.append(str(num))
        pos *= num
        continue
    
    elif neg * num < 0:
        negative.append(str(num))
        neg *= num
        continue
    
    elif num == 0:
        zeros.append(str(num))
        continue
        
    if index < length:
        if nums[index + 1] < 0:
            positive.append(str(num))
            pass_num = True
        else:
            zeros.append(str(num))
 
print(str(len(negative)) + ' ' +' '.join(negative))
print(str(len(positive)) + ' ' +' '.join(positive))
print(str(len(zeros)) + ' ' +' '.join(zeros))
