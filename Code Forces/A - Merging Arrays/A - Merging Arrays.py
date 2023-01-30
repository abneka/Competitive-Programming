m, n = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
 
c = []
i = 0
j = 0
while i < m and j < n:
    if a[i] < b[j]:
        c.append(a[i])
        i+=1
    else:
        c.append(b[j])
        j+=1
        
c.extend(a[i:])
c.extend(b[j:])
print(*c)
