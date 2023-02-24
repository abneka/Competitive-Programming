n = int(input())
data = list(map(int, input().split()))
pair = []


for index in range(len(data)):
    mini = index
    for left in range(index + 1, len(data)):
        
        if data[mini] > data[left]:
            mini = left
            
            
    if mini != index:
        pair.append((index, mini))
        data[mini], data[index] = data[index], data[mini]

print(len(pair))
for ans in pair:
    print(*ans)
