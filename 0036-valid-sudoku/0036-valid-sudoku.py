class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        col_test = defaultdict(set)
        col_size = collections.Counter()
        
        cube_test = defaultdict(set)
        cube_size = collections.Counter()
        
        change_cube_flag = 0
        
        
        for row_index, row in enumerate(board):
            
            row_size = 0
            row_test = set()
            
            
            if row_index//3 != change_cube_flag:
                
                for cube in range(3):
                    
                    if len(cube_test[str(cube)]) != cube_size[str(cube)]:
                        return False
                    
                cube_test = defaultdict(set)
                cube_size = collections.Counter()
                
            
            for index, elem in enumerate(row):
                
                if elem.isdigit():
                    row_test.add(elem)
                    row_size += 1
                    
                    col_test[str(index)].add(elem)
                    col_size[str(index)] += 1
                    
                    cube_test[str(index//3)].add(elem)
                    cube_size[str(index//3)] += 1
            
            if len(row_test) != row_size:
                return False
            
            change_cube_flag = row_index//3
            
            
        
        for index in range(9):
            if len(col_test[str(index)]) != col_size[str(index)]:
                return False
            
            if len(cube_test[str(index//3)]) != cube_size[str(index//3)]:
                return False
            
        return True
    