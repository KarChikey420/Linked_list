class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(head):
        if not head or not head.next:
            return head
        pre=None
        current=head
        next_val=head.next

        while current and current.next:
            next_pair=current.next.next
            second=current.next
        
            second.next=current
            if pre:
               pre.next=second
            current.next=next_pair

            pre=current
            current=next_pair
        return next_val
