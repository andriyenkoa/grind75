# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        even, odd = ListNode(next=head), head
        temp1 = head
        temp2 = head.next
        while odd and odd.next and odd.next.next:
            even.next = odd.next
            odd.next = even.next.next
            even = even.next
            odd = odd.next
        even.next = odd.next
        odd.next = temp2
        return temp1
