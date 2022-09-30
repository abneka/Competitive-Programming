def gradingStudents(grades):
    # Write your code here
    for i in range(len(grades)):
        if grades[i] < 38:
            continue
        elif grades[i] % 5 > 2:
            grades[i] += 5 - (grades[i] % 5)
    return grades 
