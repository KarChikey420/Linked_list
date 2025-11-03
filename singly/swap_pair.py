class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
def swap_pair(head):
   new_head=head.next
   current=head
   pre=None
   
   while current!=None and current.next!=None:
       first=current
       second=current.next
       
       first.next=second.next
       second.next=first
       
       if pre:
           pre.next=second
       
       pre=first
       current=first.next
       
   return new_head
   
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

swapped = swap_pair(head)
print("After swapping pairs:")
print_list(swapped)

        