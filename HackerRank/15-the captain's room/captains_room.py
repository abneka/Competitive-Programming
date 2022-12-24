# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
size = input()
data = input()
data = data.split(' ')
count = Counter(data)
count = {v: k for k, v in count.items()}

print(count[1])
