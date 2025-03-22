def appends(x):
    a=[]
    for i in x:
        for j in i:
            a.append(j)
    return a


print(appends([[1,4,5,7],[2,6],[6,9,8]]))
