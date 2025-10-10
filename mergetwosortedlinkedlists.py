# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 or list2
        return dummy.next
    
def print_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    print(res)

if __name__ == "__main__":
    head1 = ListNode(1, ListNode(2, ListNode(4)))
    head2 = ListNode(1, ListNode(3, ListNode(4)))

    merged = Solution().mergeTwoLists(head1, head2)
    print_list(merged)