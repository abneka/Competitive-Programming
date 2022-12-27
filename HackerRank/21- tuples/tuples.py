# Enter your code here. Read input from STDIN. Print output to STDOUT
size = int(input())
data = input()
data = list(data.split(' '))
data = [int(num) for num in data]
data = tuple(data)
# print(data)
hashed = hash(data)
print(hashed)
