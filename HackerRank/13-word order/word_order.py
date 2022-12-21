n = int(input())
arr = []
Dic = {}

for i in range(n):
    arr.append(input())

for j in arr:
    if j in Dic:
        Dic[j] +=1
    else:
        Dic[j] = 1
print(len(Dic)) 
for i in Dic:
    print(Dic[i], end=" ")
