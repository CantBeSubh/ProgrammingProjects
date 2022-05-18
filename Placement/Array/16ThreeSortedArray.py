a=[1,2,3,4]
b=[1,2,3,4]
c=[2,3,4,6]

def match(a,b,c):
    x,y,z=0,0,0
    res=[]
    while(x<len(a) and y<len(b) and z<len(c)):
        m=max(a[x],b[y],c[z])
        while(x<len(a) and a[x]<m):
            x+=1
        while(y<len(b) and b[y]<m):
            y+=1
        while(z<len(c) and c[z]<m):
            z+=1
        if(x<len(a) and y<len(b) and z<len(c)):
            if a[x]==b[y]==c[z]:
                res.append(a[x])
                x+=1
                y+=1
                z+=1
    
    return res

print(match(a,b,c))

[1,2,4]