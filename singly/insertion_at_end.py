class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
def insert_at_end(head,data):
    new_node=Node(data)
    current=head
    while current.next!=None:
        current=current.next
    current.next=new_node
    new_node.next=None
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
    
    head=insert_at_end(head,40)
    print_list(head)
    