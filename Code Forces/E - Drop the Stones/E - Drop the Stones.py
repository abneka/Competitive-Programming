cases = int(input())

for _ in range(cases):
    ROWS, COLS = map(int , input().split())
    
    grid = []
    
    for _ in range(ROWS):
        temp = list(input())
        grid.append(temp)
    
    for cur_col in range(COLS):
        cur = ROWS
        for cur_row in range(ROWS - 1, -1, -1):
            
            if grid[cur_row][cur_col] == '*':
                cur -= 1
                
                if cur_row != cur:
                    grid[cur][cur_col] = '*'
                    grid[cur_row][cur_col] = '.'
                    
            elif grid[cur_row][cur_col] == 'o':
                cur = cur_row
                   
    
    for cur_row in range(ROWS):
        for cur_col in range(COLS):
            print(grid[cur_row][cur_col],end='')
        print()
    print()
