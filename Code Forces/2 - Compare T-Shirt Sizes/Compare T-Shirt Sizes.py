count = int(input())

shirt_size = {'S':-1, 'M':1, 'L':2}

for index in range(count):
    sizes = input().split()
    
    left = sizes[0].count('X') + 1
    right = sizes[1].count('X') + 1
    
    left = left * shirt_size[sizes[0][-1]]
    right = right * shirt_size[sizes[1][-1]]
    
    if left > right:
        print('>')
    elif left < right:
        print('<')
    else:
        print('=')
