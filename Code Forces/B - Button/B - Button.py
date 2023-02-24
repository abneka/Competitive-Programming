testcases = int(input())
 
 
for testcase in range(testcases):
    data = input()
 
    result = ''
    size = len(data)
    
    prev = data[0]
    count = 0
    
    for index in range(1, size):
        # print(prev, count, data[index])
        if prev == data[index]:
            count += 1
        
        else:
            if not count:
                result += prev
            prev = data[index]
            count = 0
    
    if not count:
        result += data[size -1]
    
    result = ''.join(sorted(result))
    print(result)
