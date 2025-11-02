class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def reverse(head):
    current=head
    prev=None
    while current!=None:
        next_val=current.next
        current.next=prev
        prev=current
        current=next_val
    return prev
    
def print_list(head):
    current=head
    while current!=None:
        print(current.data,end="->")
        current=current.next

if __name__=="__main__":
    head=Node(10)
    head.next=Node(20)
    head.next.next=Node(30)
    head.next.next.next=Node(40)
    head.next.next.next.next=Node(50)
    
    reverse=reverse(head)
    print_list(reverse)

   