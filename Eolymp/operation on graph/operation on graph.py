from collections import defaultdict
graph = defaultdict(list)

size = int(input())
op = int(input())

for operation in range(op):
    command, *data = map(int, input().split())
    if command - 1:
        print(*graph[data[0]])
        continue

    graph[data[0]].append(data[1])
    graph[data[1]].append(data[0])
