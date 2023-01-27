testcases = int(input())

for testcase in range(testcases):
    
    size = int(input())
    
    data = list(set(map(int, input().split())))
    size = len(data)
    result = size
    
    data.sort()
    
    for index in range((size - 1)):
        absolute = abs(data[index] - data[index + 1])
        
        if absolute <= 1:
            result -= 1
        
    
    if result == 1:
        print('YES')
    else:
        print('NO')
