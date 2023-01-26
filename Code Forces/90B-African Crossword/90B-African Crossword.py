from collections import defaultdict
n, m = map(int, input().split())

dic_row = defaultdict(int)
dic_column = defaultdict(int)

answer = ""
matrix = []

for row in range(n):
    matrix.append(list(input()))

for row in range(n):
    for column in range(m):
        dic_row[str(row) + matrix[row][column]] +=1
        dic_column[str(column) + matrix[row][column]] +=1

for row in range(n):
    for column  in range(m):
        if dic_row[str(row) + matrix[row][column]]<2 and dic_column[str(column) + matrix[row][column]]<2:
            answer += matrix[row][column]
print(answer)
