t=int(input())
ans=0
arr=[int(x) for x in input().split()]
for i in arr:
    ans|=i

if ans==1: print("HARD")
else: print("EASY")