def countingValleys(steps, path):
    valley = 0
    counter = []
    counter.append(path[0])
    for i in range(1, len(path)):
        if len(counter) == 0 :
            counter.append(path[i])
            continue
        if counter[len(counter)-1] != path[i]:
            if len(counter) == 1 and counter[0] == 'D':
                valley += 1
            counter.pop()
            continue
        counter.append(path[i])
    return valley
