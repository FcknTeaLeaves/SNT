def enumere(tab):
    result = {}
    for i,j in enumere(tab):
        if j in result:
            result[j] = [i]
        else:
            result[j].append([i])
    return result
    
    


print(enumere([]))
print(enumere([1,2,3]))
print(enumere([1,1,2,3,2,1,3]))
