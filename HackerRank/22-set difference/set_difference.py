# Enter your code here. Read input from STDIN. Print output to STDOUT
english_size = int(input())
english = input()
english = english.split()
english = set(english)

french_size = int(input())
french = input()
french = french.split()
french = set(french)

difference = english.difference(french)

print(len(difference))
