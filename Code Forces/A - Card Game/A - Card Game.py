size = int(input())
 
left = 0
right = size - 1
 
wube = 0
henock = 0
 
wube_turn = True
 
data = list(map(int, input().split()))
 
while left <= right:
    if data[left] > data[right]:
        
        if wube_turn:
            wube += data[left]
            wube_turn = False
        
        else:
            henock += data[left]
            wube_turn = True
            
        left += 1
    
    else:
        
        if wube_turn:
            wube += data[right]
            wube_turn = False
        
        else:
            henock += data[right]
            wube_turn = True
            
        right -= 1
        
print(wube, henock)
