# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __len__(self):
        if self.next is None:
            return 1
        else:
            return 1 + len(self.next)


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        temp = head
        n = 0
        while temp != None:
            temp = temp.next
            n += 1
        k = k % n
        slw = head
        fst = head
        for _ in range(k):
            fst = fst.next
        while fst.next != None:
            fst = fst.next
            slw = slw.next
        fst.next = head
        head = slw.next
        slw.next = None
        return head
