# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        res = dummy
        total = carry = 0
        while list1 or list2 or carry:
            total = carry
            
            if list1:
                total += list1.val
                list1 = list1.next
            if list2:
                total += list2.val
                list2 = list2.next

            num = total % 10
            carry = total // 10

            dummy.next = ListNode(num)
            dummy = dummy.next
        return res.next

if __name__ == "__main__":
    head1 = ListNode(9, ListNode(9, ListNode(9)))
    head2 = ListNode(9, ListNode(9, ListNode(9)))

    print(Solution().mergeTwoLists(head1, head2))
    