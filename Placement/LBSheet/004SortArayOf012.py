def sort012(a):
    if len(a)==1:
        return a
    x=0
    y=0
    z=len(a)-1
    while(y<=z):
        if a[y]==0:
            a[x],a[y]=a[y],a[x]
            x+=1
            y+=1
        elif a[y]==1:
            y+=1
        else:
            a[z],a[y]=a[y],a[z]
            z-=1
    return a