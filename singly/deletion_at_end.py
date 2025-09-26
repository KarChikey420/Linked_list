class Node:
    def __init__(self,data):
        self.data=data
        self.next=None 
        
def delete_at_end(head):
    if head is None:
        return None
    if head.next is None:
        return None
    
    curr=head.next
    pre=head
    while curr.next!=None:
       pre=curr
       curr=curr.next
    pre.next=None
    return head 

    # curr=head
    # while curr.next.next!=None:
    #     curr=curr.next
    # curr.next=None
    # return head

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
    
    head = delete_at_end(head)
    printList(head)


