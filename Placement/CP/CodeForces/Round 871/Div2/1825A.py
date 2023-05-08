t=int(input())
for i in range(t):
    s=input()
    if s==s[0]*len(s): print(-1)
    else:print(len(s)-1)