a=[1,2,3,4,5]
b=[1,2,3]

def unionNintersection(a,b):
    u=dict()
    inter=dict()
    for i in a:
        u[i]=1
        inter[i]=1
    for i in b:
        if i in u.keys():
            inter[i]=2
        else:
            u[i]=1
            inter[i]=0
    union = [i for i in u.keys()]
    print(union)
    intersection=[i for i,j in inter.items() if j==2]
    print(intersection)

unionNintersection(a,b)