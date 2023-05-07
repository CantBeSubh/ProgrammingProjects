t=int(input())
a=[int(x) for x in input().split()]
mini=1e9
maxi=-1
mini_pos=0
maxi_pos=0
for i in range(t):
    if a[i]<=mini:
        mini=a[i]
        mini_pos=i
    if a[i]>maxi:
        maxi=a[i]
        maxi_pos=i

if mini_pos<maxi_pos:
    print(t-mini_pos+maxi_pos-2)
else:
    print(t-mini_pos+maxi_pos-1)