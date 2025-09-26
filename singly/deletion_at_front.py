class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def delete_at_front(head):
    if head is None:
        return None
    
    temp=head
    head=head.next 
    return head

def printList(head):
    curr = head
    while curr:
        print(curr.data, end="")
        if curr.next:
            print(" -> ", end="")
        curr = curr.next
    print()

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(4)
    
    head = delete_at_front(head)
    printList(head)


