class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(head):
    if not head:
        return head
    prev = head
    nxt = head.next
    while nxt:
        temp = nxt.next
        nxt.next = prev
        prev = nxt
        nxt = temp
    head.next = None
    return prev
