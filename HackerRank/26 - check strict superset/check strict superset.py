# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(input().split())
b = set()

for i in range(int(input())):
    temp = set(input().split())
    b = b.union(temp)
    
A = b.difference(A)

if A:
    print(False)
else:
    print(True)
