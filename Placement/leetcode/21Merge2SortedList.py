class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    i=list1
    j=list2
    a,b=0,0
    res=None
    flag=True
    while(i!=None):
        a+=1
        i=i.next
    while(j!=None):
        b+=1
        j=j.next
    i,j=list1,list2
    if a<b:
        while(i!=None):
            if i.val<j.val:
                res=ListNode(i.val)
                res.next=ListNode(j.val)
            else:
                res=ListNode(j.val)
                res.next=ListNode(i.val)
            i=i.next
            j=j.next
            if flag==True:
                temp=res
                flag=False
            res=res.next.next
        while(j!=None):
            res.val=j.val
            j=j.next
            res=res.next
    else:
        while(j!=None):
            if i.val<j.val:
                res=ListNode(i.val)
                res.next=ListNode(j.val)
            else:
                res=ListNode(j.val)
                res.next=ListNode(i.val)
            i=i.next
            j=j.next
            if flag==True:
                temp=res
                flag=False
            res=res.next.next
        while(i!=None):
            res.val=i.val
            i=i.next
            res=res.next
    return temp

a=ListNode(1)
temp=a
a.next=ListNode(2)
a=a.next
a.next=ListNode(4)
a=temp

b=ListNode(1)
temp=b
b.next=ListNode(3)
b=b.next
b.next=ListNode(4)
b=temp

c=mergeTwoLists(a,b)

while(c!=None):
    print(c.val)
    c=c.next