testcases = int(input())
 
for testcase in range(testcases):
    
    size = int(input())
    nums = list(map(int, input().split()))
    
    maxi = 0
    total = 0
    
    for num in nums:
        
        if num > 0:
            if maxi < 0:
                total += maxi
            maxi = max(maxi, num)
        
        else:
            if maxi > 0:
                total += maxi
                maxi = num
            if not maxi:
                maxi = num
            maxi = max(maxi, num)
        
    total += maxi
    print(total)
