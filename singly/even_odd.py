class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def oddEvenList(head):
    odd=head
    even=head.next
    even_head=even

    while even and even.next:
        odd.next=even.next
        odd=odd.next
        
        even.next=odd.next
        even=even.next
        
    odd.next=even_head
    return head