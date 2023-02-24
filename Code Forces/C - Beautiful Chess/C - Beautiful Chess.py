testcases = int(input())
 
 
for test in range(testcases):
    input()
    
    previous = [0, []]
    pre_previous = 0
    
    for row in range(8):
        
        line = input()
    
        count = [ 0, []]
        
        for index, char in enumerate(line):
            if char == '#':
                count = [ count[0] + 1, [str(row + 1), str(index +1)]]
        
        if count [0] == 2:
            if previous[0] == 1 and pre_previous == 2:
                print(' '.join(previous[1]))
                previous = [0, []]
                pre_previous = 0
        
        pre_previous = previous[0]
        previous = count
