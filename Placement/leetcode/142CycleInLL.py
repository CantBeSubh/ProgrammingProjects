class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def detectCycle( head ):
    if(head ==None or head.next==None):
        return -1
    pos=0
    a,b=head,head.next.next
    l=[]
    while(a!=b):
        l.append(a.val)
        a=a.next
        b=b.next.next
        pos+=1
    return l.index(a.next.val)