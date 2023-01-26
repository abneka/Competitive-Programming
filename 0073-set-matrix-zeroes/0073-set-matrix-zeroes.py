class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        R = len(matrix)
        C = len(matrix[0])
        rows, cols = [], []

        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)

        for i in range(R):
            for j in range(C):
                if i in rows or j in cols:
                    matrix[i][j] = 0