from collections import Counter
size = int(input())

for nod in range(size):

    data = map(int, input().split())
    adjecent = []
    for index, node in enumerate(data):
        if node:
            adjecent.append(index + 1)
    print(len(adjecent), *adjecent)
