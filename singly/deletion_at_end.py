class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
def delete_at_end(head):
    pre=head
    current=head.next
    while current.next!=None:
        pre=current
        current=current.next
    pre.next=None
    return head

def print_list(head):
    current=head
    while current!=None:
       print(current.data,end="->")  
       current=current.next
       
if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(4)
    
    head = delete_at_end(head)
    print_list(head)


