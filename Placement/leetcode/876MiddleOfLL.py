class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(head):
    m=head
    m2=head
    while(m2!=None and m2.next!=None):
        m=m.next
        m2=m2.next
        if m2.next!=None:
            m2=m2.next
    
    return m

