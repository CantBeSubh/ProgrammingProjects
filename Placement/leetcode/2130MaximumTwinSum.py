class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def soln(head: ListNode) -> int:
    n = 0
    temp = head
    while temp:
        temp = temp.next
        n += 1
    arr = [0] * n // 2
    i = 0
    temp = head
    while i != n // 2:
        arr[i] = temp.val
        temp = temp.next
        i += 1
    while i != n:
        arr[n - i] += temp.val
        temp = temp.next
        i += 1

    return max(arr)


def soln2(head: ListNode) -> int:
    n = 0
    temp = head
    while temp:
        temp = temp.next
        n += 1

    ll1 = head
    ll2 = head
    for i in range(n // 2):
        ll2 = ll2.next

    temp = ll2
    ll2.next = None
    ll2 = temp.next

    arr = [0] * (n // 2)
    for i in range(n // 2):
        arr[i] += ll1.val
        arr[n // 2 - i - 1] += ll2.val
        ll1 = ll1.next
        ll2 = ll2.next
    return max(arr)
