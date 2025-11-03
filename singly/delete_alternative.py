class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
def delete_alternative(head):
    current=head
    while current!=None and current.next!=None:
        current.next=current.next.next
        current=current.next
    return head
   
def print_list(node):
    while node:
        print(node.data, end="→" if node.next else "\n")
        node = node.next

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

print("Original list:")
print_list(head)

swapped = delete_alternative(head)
print("After swapping pairs:")
print_list(swapped)

        