import math
testcases = int(input())

for _ in range(testcases):
    num = int(input())

    x = num & (-num)

    if num == 1:
        print(3)
    elif num % 2 != 0:
        print(1)
    elif x == num:
        print(x + 1)
    else:
        print(x)
