from collections import Counter
 
testcases = int(input())
 
 
for testcase in range(testcases):
    matimatician, programmers = map(int, input().split())
    
    print(min(matimatician, programmers, (matimatician + programmers)//4))
