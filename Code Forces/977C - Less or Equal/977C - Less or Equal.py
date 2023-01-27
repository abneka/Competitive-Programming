from collections import Counter

n, k = map(int, input().split())
result = 0

data = list(map(int, input().split()))

data.sort()

if k == 0:
    if data[0] <= 1:
        print(-1)
    else:
        print(data[0] - 1)
else:
    
    if k == n:
        print(data[k - 1])
    else:
        if data[k] == data[k-1]:
            print(-1)
        else:
            print(data[k-1])
