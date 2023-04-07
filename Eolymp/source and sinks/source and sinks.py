from collections import Counter
graph = Counter()

size = int(input())
sinks = []
source = []

for nod in range(size):

    data = map(int, input().split())
    total = 0

    for index, node in enumerate(data):
        graph[index] += node
        total += node

    if not total:
        sinks.append(nod + 1)

for node in range(size):
    if not graph[node]:
        source.append(node + 1)

print(len(source), *source)
print(len(sinks), *sinks)
