from collections import defaultdict

n = int(input())
graph = defaultdict(int)
edges = 0


for start in range(n):
    data = list(map(int, input().split()))

    for index, city in enumerate(data):
        if city:
            graph[start] += 1

for key, value in graph.items():
    edges += value
print(edges//2)
