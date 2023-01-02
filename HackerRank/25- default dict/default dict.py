# Enter your code here. Read input from STDIN. Print output to STDOUT
# import collections

from collections import defaultdict

size = input()
size = size.split()

A = defaultdict(list)

for index in range(int(size[0])):
    A[input()].append(str(index+1))


for index in range(int(size[1])):
    b = input()
    if A[b]:
        print(' '.join(A[b]))
    else:
        print('-1')
