class Node:
    def __init__(self,k,v,i):
        self.k=k
        self.v=v
        self.i=i
        self.n=None
    
class LL:
    head=None

def firstRepeated(arr):
    n=len(arr)
    m=LL()
    key=list()
    for i in range(n):
        if arr[i] not in key:
            if m.head==None:
                temp=Node(arr[i],1,i)
                m.head=temp
            else:
                temp=Node(arr[i],1,i)
                temp2=m.head
                while(temp2.n!=None):
                    temp2=temp2.n
                temp2.n=temp
            key.append(arr[i])
        else:
            temp=m.head
            while(temp.n!=None and temp.k!=arr[i]):
                temp=temp.n
            temp.v+=1
        
    temp=m.head
    while(temp!=None and temp.v==1):
        temp=temp.n
    try:
        res=temp.i+1
        return res
    except:
        return -1

print(firstRepeated([7,4,0,9,4,8,8,2,4,5,5,1]))