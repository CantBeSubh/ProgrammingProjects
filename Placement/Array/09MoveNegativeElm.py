#https://practice.geeksforgeeks.org/problems/move-all-negative-elements-to-end1813/1
#obsidian://open?vault=HolyCow&file=Placement%2FArray%2FLevel%201%2F09%20Move%20negative%20elements%20to%20one%20side

def swapMe(arr):
    p=0
    n=0
    while(p<len(arr)):
        if arr[p]>0:
            arr[p],arr[n]=arr[n],arr[p]
            n+=1
        p+=1
    
    return arr

def swapMe2(arr):
    new_arr=[]
    p=[]
    n=[]
    for i in arr:
        if i>0:
            p.append(i)
        else:
            n.append(i)
    
    new_arr.extend(p)
    new_arr.extend(n)
    return new_arr

print(swapMe([1, -1, 3, 2, -7, -5, 11, 6 ]))
print(swapMe2([1, -1, 3, 2, -7, -5, 11, 6 ]))