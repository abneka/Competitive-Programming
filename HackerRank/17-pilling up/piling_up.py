# Enter your code here. Read input from STDIN. Print output to STDOUT
numberoftestcase=int(input())
for _ in range(numberoftestcase):
    cubenumber=int(input())
    cubesize=list(map(int, input().split(" ")))
    rightp=len(cubesize)-1
    leftp=0
    topstack=-1
    ans="Yes"
    while leftp<=rightp:
        if topstack==-1 and cubesize[leftp]>=cubesize[rightp]:
            topstack=cubesize[leftp]
            leftp+=1
        elif topstack==-1 and cubesize[leftp]<=cubesize[rightp]:
            topstack=cubesize[rightp]
            rightp-=1
        elif topstack!=-1:
            if cubesize[leftp]>=cubesize[rightp] and topstack>=cubesize[leftp]:
                topstack=cubesize[leftp]
                leftp+=1
            elif cubesize[leftp]>=cubesize[rightp] and topstack<=cubesize[leftp] and cubesize[rightp]<=topstack:
                topstack=cubesize[rightp]
                rightp-=1
            elif cubesize[leftp]<=cubesize[rightp] and topstack>=cubesize[rightp]:
                topstack=cubesize[rightp]
                rightp-=1
            elif cubesize[leftp]<=cubesize[rightp] and topstack<=cubesize[rightp] and cubesize[leftp]<=topstack:
                topstack=cubesize[leftp]
                leftp+=1
            else : 
                ans="No"
                break
    print(ans)
            
                
                
        
    
    
    
