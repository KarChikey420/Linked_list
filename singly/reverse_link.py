class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def reverse(head):
    previous=None
    current=head
    while current!=None:
        next_val=current.next
        current.next=previous
        previous=current
        current=next_val
    return previous
    
def print_list(head):
    current=head
    while current != None:
        print(current.data,end="->")
        current=current.next
        
if __name__=="__main__":
    head=Node(10)
    head.next=Node(20)
    head.next.next=Node(30)
    head.next.next.next=Node(40)
    head=reverse(head)
    print_list(head)
    
    