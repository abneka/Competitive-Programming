def countSwaps(a):
    # Write your code here
    counter = 0
    for i in range(len(a)):
        for j in range(len(a) - (1+i)):
            if a[j+1] < a[j]:
                a[j+1], a[j] = a[j], a[j+1]
                counter += 1
    print ("Array is sorted in %d swaps." % (counter))
    print ("First Element: %d" % (a[0]))
    print ("Last Element: %d" % (a[len(a)-1]))
