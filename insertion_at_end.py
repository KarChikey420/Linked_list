class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
    
def insert_at_end(head,data):
    new_node=Node(data)
    current=head
    
    while current.next:
        current=current.next
        
    current.next=new_node
    return head
    

node=Node(10)
node1=Node(20)
node2=Node(30)

node.next=node1
node1.next=node2
node2.next=None

head=node 

head=insert_at_end(head,40)

current=head
while current:
    print(current.data,"<-")
    current=current.next
    
print("none")