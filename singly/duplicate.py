# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def deleteDuplicates(head):
    current=head
    while current!=None and current.next!=None:
        if current.val==current.next.val:
            current.next=current.next.next
        else:
            current=current.next
    return head

def print_list(head):
    current = head
    while current is not None:
        print(current.val, end="->")
        current = current.next
    print("None")

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(3)

    print("Original list:")
    print_list(head)

    head = deleteDuplicates(head)

    print("List after removing duplicates:")
    print_list(head)

