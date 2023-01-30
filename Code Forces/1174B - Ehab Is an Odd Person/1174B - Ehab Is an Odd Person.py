size = int(input())
data = list(map(int, input().split()))
 
odd = []
even = []
for num in data:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
        
        
if not len(even) or not len(odd):
    print(*data)
else:
    print(*sorted(data))
