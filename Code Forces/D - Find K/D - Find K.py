from collections import Counter
 
testcases = int(input())
 
for testcase in range(testcases):
    
    n, k = map(int, input().split())
    data = list(map(int, input().split()))
    
    count = Counter()
    
    for num in data:
        count[str(num)] = 1
        
    is_not_found = True
    
    for num in data:
        
        if count[str(num + k)]:
            print('YES')
            is_not_found = False
            break
    
    if is_not_found:
        print('NO')
