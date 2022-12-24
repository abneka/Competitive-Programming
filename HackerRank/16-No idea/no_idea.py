ans = 0
input()
points = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

for i in points:
    if i in A:
        ans += 1
    if i in B:
        ans -= 1
print(ans)   
