n = int(input())
arr = list(map(int, input().split()))
pairs = []


for i in range(len(arr)):
    min_idx = i
    for j in range(i + 1, len(arr)):
        
        if arr[min_idx] > arr[j]:
            min_idx = j
            
            
    if min_idx != i:
        pairs.append((i, min_idx))
        arr[min_idx], arr[i] = arr[i], arr[min_idx]

print(len(pairs))
for res in pairs:
    print(*res)
