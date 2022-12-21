def split_and_join(line):
    # write your code here
    splitted = line.split(' ')
    joined = '-'.join(splitted)
    
    return joined

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
