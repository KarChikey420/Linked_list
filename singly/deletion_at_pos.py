class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def delete_at_pos(head,pos):
    pre=head
    current=head.next
    
    for i in range(1,pos-1):
      if current.next!=None:
          pre=current
          current=current.next
    pre.next=current.next
    
    return head

def printlist(head):
    curr=head
    while curr!=None:
        print(curr.data,end="->")
        curr=curr.next

if __name__=="__main__":
    head=Node(1)
    head.next=Node(2)
    head.next.next=Node(3)
    head.next.next.next=Node(4)
    
    pos=3
    head=delete_at_pos(head,pos)
    printlist(head)
    
        