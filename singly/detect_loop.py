class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
def detect_loop(head):
    slow=head
    fast=head
    
    while fast!=None and fast.next!=None:
        slow=slow.next
        fast=fast.next.next
        
        if slow==fast:
            break
        
    while slow.next!=fast.next:
        slow=slow.next
        fast=fast.next
    fast.next=None
    
def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    
    head.next.next.next.next.next = head.next.next

    detect_loop(head)
    print_list(head)
    