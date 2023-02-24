size = int(input())
 
for i in range(size):
    word = input()
    word = word + '?'
 
    print(word[0:2] + '... ' + word)
