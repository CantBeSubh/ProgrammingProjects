class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    arr=[]
    a=head
    while(a!=None):
        arr.append(a.val)
        a=a.next
    if len(arr)>0:
        b=ListNode(arr[-1])
        res=b
        for i in arr[len(arr)-2::-1]:
            b.next=ListNode(i)
            b=b.next
    else:
        return None
    return res
a=ListNode(1)
temp=a
a.next=ListNode(2)
a=a.next
a.next=ListNode(3)
a=a.next
a.next=ListNode(4)
a=a.next
a.next=ListNode(5)
a=temp
c=reverseList(a)

while(c!=None):
    print(c.val)
    c=c.next
