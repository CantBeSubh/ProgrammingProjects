def FirstRepeated(arr):
    n=len(arr)
    m=dict()
    repIndex=list()
    for i in range(n):
        if arr[i] not in m.keys():
            m[arr[i]]=[i,1]
        else:
            m[arr[i]][1]+=1
    for i in m:
        if(m[i][1]>1):
            repIndex.append(m[i][0])

    if len(repIndex)==0:
        return -1
    return min(repIndex)+1

print(FirstRepeated([7,4,0,9,4,8,8,2,4,5,5,1]))