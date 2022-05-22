#Kadane's Algorithm
import sys

def Kadene(a):
    s=0
    M=-sys.maxsize
    for i in a:
        s+=i
        M=max(s,M)
        s=0 if s<0 else s
    return M

print(Kadene([-9,-2,-3,-4]))
