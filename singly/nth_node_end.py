class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def reverse(head):
    previous=None
    current=head
    while current!=None:
        next_value=current.next
        current.next=previous
        previous=current
        current=next_value
    return previous

def Nth_Node(head,n):
    head=reverse(head)
    current=head
    for i in range(n-1):
        current=current.next
    result=current.data
    return result

if __name__=="__main__":
    head=Node(10)
    head.next=Node(20)
    head.next.next=Node(30)
    head.next.next.next=Node(40)
    head.next.next.next.next=Node(50)
    
    head=Nth_Node(head,2)
    print("Nth Node is: ",head)