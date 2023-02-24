from collections import Counter
 
testcases = int(input())
 
data = list(map(int, input().split()))
 
maxi = 0
count = 0
 
prev = 0
 
for num in data:
    
    if num >= prev:
        count += 1
        maxi = max(maxi, count)
    
    else:
        maxi = max(maxi, count)
        count = 1
        
    prev = num
    
print(maxi)
