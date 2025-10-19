class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
def insert_at_begning(head,data):
    new_node=Node(data)
    new_node.next=head
    head=new_node
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
    
    head=insert_at_begning(head,1)
    print_list(head)        