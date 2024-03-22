def occurrences(char(target), search):
    count = 0
    for i in search:
        if i == target:
            count += 1 
    return count