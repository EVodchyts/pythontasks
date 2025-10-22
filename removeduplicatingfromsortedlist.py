from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        prev_val = None

        while head:
            if head.val != prev_val:
                current.next = ListNode(head.val)
                current = current.next
                prev_val = head.val
            head = head.next

        return dummy.next
        
    
if __name__ == "__main__":
    head = ListNode(1, ListNode(1, ListNode(2, ListNode(2))))

    print(Solution().deleteDuplicates(head))
    