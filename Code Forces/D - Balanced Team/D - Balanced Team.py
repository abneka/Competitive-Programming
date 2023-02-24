from collections import Counter
 
testcases = int(input())
 
data = list(map(int, input().split()))
 
prefix = []
 
data.sort()
prev = data[0]
 
for testcase in range(1, testcases):
    
    prefix.append(data[testcase] - prev)
    
    prev = data[testcase]
 
total = 0
left = 0
right = 0
students = 0
length = len(prefix)
 
while right < length:
    total += prefix[right]
    
    while total > 5 and left <= right:
        total -= prefix[left]
        left += 1
    
    students = max(students, (right - left + 2))
    right += 1
 
print(students)
