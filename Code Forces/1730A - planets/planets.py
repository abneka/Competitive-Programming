from collections import Counter
n=int(input())

for i in range(n):
    p, m2 = map(int,input().split())
    planets=list(map(int,input().split()))
    orbit = Counter(planets)
    ans=0
    for planet in orbit:
        if orbit[planet] > 1 and orbit[planet] >= m2:
            ans+=m2
        elif orbit[planet] > 1:
            ans+=orbit[planet]
        else:
            ans+=1
    print(ans)
