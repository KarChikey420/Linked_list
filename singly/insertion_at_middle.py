class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
def insert_at_pos(head,data,index):
    new_node=Node(data)
    current=head
    
    for i in range(1,index-1):
        current=current.next
    
    new_node.next=current.next
    current.next=new_node
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
    
    head=insert_at_pos(head,25,2)
    print_list(head)