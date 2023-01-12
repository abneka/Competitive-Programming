import collections

testcases = int(input())

for testcase in range(testcases):
    
    diagonal_sum = collections.Counter()
    diagonal_sum1 = collections.Counter()
    
    rows, cols = map(int, input().split())
    
    maximum = 0
    
    matrix = []
    
    for row in range(rows):
        row_data = list(map(int, input().split()))
        matrix.append(row_data)
        
        for col in range(cols):
            
            diagonal_sum[str(col - row)] += row_data[col]
            diagonal_sum1[str(col + row)] += row_data[col]
        
    # print(matrix, rows, cols)
    for row in range(rows):
        
        for col in range(cols):
            
            sum_of_diagonals = diagonal_sum[str(col - row)] + diagonal_sum1[str(col + row)]
            
            
            maximum = max(maximum, (sum_of_diagonals - matrix[row][col]))
    
    print(maximum)
            
            
            
            
            
