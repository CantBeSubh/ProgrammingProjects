class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse(head):
    prev = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev


def addTwoNumbers(l1, l2):
    l1 = reverse(l1)
    l2 = reverse(l2)
    carry = 0
    dummy = ListNode(0)
    temp = dummy
    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next

        temp.next = ListNode(carry % 10)
        temp = temp.next
        carry //= 10

    return reverse(dummy.next)
