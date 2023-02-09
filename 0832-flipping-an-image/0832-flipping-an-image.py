class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        newMatrix = []
        for row in image:
            reversedRow = reversed(row)
            newRow = []
            for item in reversedRow:
                if item == 1: newRow.append(0)
                else: newRow.append(1)
            newMatrix.append(newRow)
        return newMatrix