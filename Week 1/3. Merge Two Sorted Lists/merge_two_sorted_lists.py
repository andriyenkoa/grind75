# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        class Solution:
            def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
                temp = head = ListNode()

                while list1 and list2:
                    val1 = list1.val
                    val2 = list2.val

                    if val1 < val2:
                        head.next = list1
                        list1 = list1.next
                    else:
                        head.next = list2
                        list2 = list2.next

                    head = head.next

                if list1 or list2:
                    head.next = list1 if list1 else list2

                return temp.next

