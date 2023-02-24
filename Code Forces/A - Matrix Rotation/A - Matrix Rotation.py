from collections import Counter
 
testcases = int(input())
 
for testcase in range(testcases):
 
    rowa, rowb = map(int, input().split())
    rowc, rowd = map(int, input().split())
    
    is_found = False
    
    
    for tries in range(4):
        if rowa < rowb and rowc < rowd:
            if rowa < rowc and rowb < rowd:
                print('YES')
                is_found = True
                break
            
        temp = rowa
        rowa = rowc
        rowc = rowd
        rowd = rowb
        rowb = temp
    
    if not is_found:
        print('NO')
