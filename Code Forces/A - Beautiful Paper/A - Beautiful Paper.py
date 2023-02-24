testcases = int(input())
 
for testcase in range(testcases):
    
    first = list(map(int, input().split()))
    second = list(map(int, input().split()))
    
    first.sort()
    second.sort()
    
    if first[1] == second[1]:
        if first[0] + second[0] == first[1]:
            print('Yes')
            continue
    
    print('No')
