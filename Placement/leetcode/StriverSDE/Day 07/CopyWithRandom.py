# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        head2 = Node(0)
        cur = head
        cur2 = head2
        while cur:
            cur2.next = Node(cur.val)
            cur2 = cur2.next
            cur2.random = cur
            temp = cur.next
            cur.next = cur2
            cur = temp
        cur = head
        cur2 = head2.next
        while cur2 and cur2.next:
            if cur.random:
                cur2.random = cur.random.next
            cur = cur2.next.random
            cur2 = cur2.next
        return head2.next
