m, n = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
 
result = []

small = 0
counter = 0

for num in b:
    
    while small < m and a[small] < num:
        counter += 1
        small += 1
    
    result.append(counter)
    
print(*result)
