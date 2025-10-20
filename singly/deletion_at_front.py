class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def delete_at_front(head):
    temp=head
    head=head.next
    return head
    
def print_list(head):
    current=head
    while current!=None:
        print(current.data,end="->")
        current=current.next

if __name__=="__main__":
    head=Node(10)
    head.next=Node(20)
    head.next.next=Node(30)
    head=delete_at_front(head)
    print_list(head)
    
    
    