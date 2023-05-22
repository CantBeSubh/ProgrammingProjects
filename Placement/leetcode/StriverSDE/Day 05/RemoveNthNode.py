class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n):
    length = 0
    temp = head
    while temp:
        length += 1
        temp = temp.next

    if length == 1:
        return None
    if length == n:
        return head.next

    temp = head
    for i in range(length - n - 1):
        temp = temp.next

    temp.next = temp.next.next
    return head


def better(head, n):
    dummy = ListNode(0)
    dummy.next = head
    slow = fast = dummy
    for i in range(n + 1):
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return dummy.next
