# def solve(s):
#     res=0
#     for i in range(len(s)):
#         if s[i]!=' ':
#             res+=1
#         else:
#             if i!=len(s)-1:
#                 res=0
#     return res

def solve(s):
    res=0
    l=len(s)-1
    while(l>-1 and s[l]==' '):
        l-=1
    while(l>-1 and s[l]!=' '):
        res+=1
        l-=1
    
    return res

print(solve('Hello World   '))