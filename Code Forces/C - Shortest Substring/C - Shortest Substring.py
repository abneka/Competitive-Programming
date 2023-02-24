testcases = int(input())
 
for testcase in range(testcases):
    
    data = input()
    
    size = len(data)
    
    one = -1
    two = -1
    three = -1
    
    mini = size
    not_found = False
    
    for index, char in enumerate(data):
        
        if char == '1':
            one = max(one, index)
            
        elif char == '2':
            two = max(two, index)
            
        else:
            three = max(three, index)
            
        left = min(one, two, three)
        right = max(one, two, three)
        
        if left == -1:
            not_found = True
            continue
        
        not_found = False
        mini = min(mini, (right - left + 1))
    
    if not_found:
        print(0)
        continue
    
    print(mini)
