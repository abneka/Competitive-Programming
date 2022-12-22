if __name__ == '__main__':
    N = int(input())
    data = []
    for i in range(N):
        comm = input().split(' ')
        if comm[0] == 'insert':
            data.insert(int(comm[1]), int(comm[2]))
        elif comm[0] == 'print':
            print(data)
        elif comm[0] == 'remove':
            data.remove(int(comm[1]))
        elif comm[0] == 'append':
            data.append(int(comm[1]))
        elif comm[0] == 'sort':
            data.sort()
        elif comm[0] == 'pop':
            data.pop()
        elif comm[0] == 'reverse':
            data.reverse()            
