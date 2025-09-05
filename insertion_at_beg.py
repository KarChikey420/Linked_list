class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def insert_at_beginning(head,data):
    new_node=Node(data)
    new_node.next=head
    return new_node

        
node =Node(10)
node1=Node(20)
node2=Node(30)

node.next=node1
node1.next=node2
node2.next=None

head=node

head=insert_at_beginning(head,5)

current=head
while current is not None:
    print(current.data,end='<-')
    current=current.next
print("none")