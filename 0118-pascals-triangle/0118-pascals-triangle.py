class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for line in range(1, numRows + 1):
            row = [1] * line
            for j in range(1,line - 1):
                row[j] = ans[line - 2][j] + ans[line - 2][j - 1]
            ans.append(row)
        return ans