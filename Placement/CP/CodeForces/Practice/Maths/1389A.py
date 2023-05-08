t=int(input())
def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

def lcm(x, y):
    lcm = (x*y)//gcd(x,y)
    return lcm

while(t):
    t-=1
    l,r=map(int,input())
