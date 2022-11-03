# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def revert(node):
    """Revert list in-place"""

    prev = None
    while node:
        prev, node.next, node = node, prev, node.next

    return prev


def addTwoNumbers(A, B):
    ptr1 = A
    n = 0
    while ptr1 != None:
        n += 1
        ptr1 = ptr1.next
    m = 0
    ptr2 = B
    while ptr2 != None:
        m += 1
        ptr2 = ptr2.next
    if n > m:
        d = n - m
        while d > 0:
            ptr2 = ListNode(0)
            ptr2 = ptr2.next
            d -= 1
    else:
        d = n - m
        while d > 0:
            ptr1 = ListNode(0)
            ptr1 = ptr1.next
            d -= 1
    A = revert(A)
    B = revert(B)
    res = ListNode(-1)
    ptr = res
    carry = 0
    while A != None and B != None:
        print(A.val, B.val)
        ptr.val = (A.val + B.val + carry) % 10
        carry = (A.val + B.val + carry) // 10
        A = A.next
        B = B.next
        ptr.next = ListNode(0)
        ptr = ptr.next

    return revert(res.next)

def solve(A, B):
    ptr=A
    cnt=1
    while(ptr and ptr.next):
        ptr=ptr.next
        cnt+=1
    print(cnt)

q = ListNode(2)
q.next = ListNode(4)
q.next.next = ListNode(3)

r = ListNode(5)
r.next = ListNode(6)
r.next.next = ListNode(4)

ans = addTwoNumbers(q, r)
print(ans)
while ans != None:
    print(ans.val)
    ans = ans.next



