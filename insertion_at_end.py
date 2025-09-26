class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
def insertAtEnd(head,data):
    newNode=Node(data)
    if head is None:
        return newNode
    curr=head
    while curr.next!=None:
        curr=curr.next
    curr.next=newNode
    newNode.next=None
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
    
    val = 3
    head = insertAtEnd(head,val)
    printList(head)