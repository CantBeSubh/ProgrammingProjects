# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def insertionSortList(A):
    ptr = A
    n = 0
    while ptr != None:
        ptr = ptr.next
        n += 1
    for i in range(1, n):
        j = i
        while j > 0:
            k = j
            ptr = A
            while k > 1 and ptr != None:
                ptr = ptr.next
                k -= 1
            if ptr != None and ptr.next != None and ptr.val > ptr.next.val:
                ptr.val, ptr.next.val = ptr.next.val, ptr.val
            j -= 1
    return A


def revert(node):
    """Revert list in-place"""

    prev = None
    while node:
        prev, node.next, node = node, prev, node.next

    return prev


def insertionSortList2(A):
    """This solution:
    * doesn't swap the values themselves
        -> in Python it doesn't matter much,
            but in general doing so would kind of defeat
            one advantage of having a linked list
    * doesn't create new node
    * builds the output list in decreasing order
        -> if input list is already sorted,
            the complexity would be O(n)
    """

    source = A
    dest = None

    while source:
        prev = None
        node = dest
        # Find insertion point (between prev and node)
        while node and node.val > source.val:
            prev, node = node, node.next
        if prev is None:
            dest = source
        else:
            prev.next = source
        source.next, source = node, source.next

    return revert(dest)


q = ListNode(1)
q.next = ListNode(3)
q.next.next = ListNode(2)
q.next.next.next = ListNode(5)
q.next.next.next.next = ListNode(6)
q.next.next.next.next.next = ListNode(4)
a = insertionSortList(q)
while a != None:
    print(a.val)
    a = a.next
