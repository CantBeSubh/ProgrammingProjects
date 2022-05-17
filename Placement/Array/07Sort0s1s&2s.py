# a=[0,2,1,2,0]

# def SortMe(a):
#     if len(a)==1:
#         return a
#     x=0
#     y=0
#     z=len(a)-1
#     while(a[x]==0):
#         x+=1
#         y+=1
#     y+=1
#     while(a[z]==2):
#         z-=1
#     while(y<z):
#         if a[y]==1:
#             y+=1
#         if a[y]==0:
#             a[x],a[y]=a[y],a[x]
#             x+=1
#             y+=1
#         if a[y]==2:
#             a[z],a[y]=a[y],a[z]
#             z-=1
#             y+=1
#     return a

# print(SortMe(a))

def sort012(self,a,n):
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