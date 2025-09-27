class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
def deletion_at_pos(head,pos):
    if pos==1:
        return head.next
    curr=head
    for _ in range(pos-2):
        curr=curr.next
    curr.next=curr.next.next 
    return head

def printlist(head):
    curr=head
    while curr!=None:
        print(curr.data,end="")
        curr=curr.next

if __name__=="__main__":
    head=Node(1)
    head.next=Node(2)
    head.next.next=Node(3)
    head.next.next.next=Node(4)
    
    pos=3
    head=deletion_at_pos(head,pos)
    printlist(head)
    