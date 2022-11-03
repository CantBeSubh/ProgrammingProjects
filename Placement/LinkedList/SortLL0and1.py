# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        one, zero = 0, 0
        while A != None:
            if A.val == 1:
                one += 1
            else:
                zero += 1
            A = A.next
        if zero == 0:
            res = ListNode(1)
            ptr = res
            for i in range(one - 1):
                ptr.next = ListNode(1)
                ptr = ptr.next
        else:
            res = ListNode(0)
            ptr = res
            for i in range(zero - 1):
                ptr.next = ListNode(0)
                ptr = ptr.next
            for i in range(one):
                ptr.next = ListNode(1)
                ptr = ptr.next

    def better(self, A):
        one, zero = (0,)
        ptr = A
        while ptr != None:
            if ptr.val == 1:
                one += 1
            else:
                zero += 1
            ptr = ptr.next
        ptr = A
        while ptr != None:
            if zero != 0:
                ptr.val = 0
                zero -= 1
            elif one != 0:
                ptr.val = 1
                one -= 1
            ptr = ptr.next

        return A
