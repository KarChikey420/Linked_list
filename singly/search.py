class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
def search(head,key):
    curr=head
    while curr!=None:
        if curr.data==key:
            return True
        else:
            False
        curr=curr.next
    
if __name__=="__main__":
    head=Node(1)
    head.next=Node(2)
    head.next.next=Node(3)
    head.next.next.next=Node(4)
    
    print(search(head,2))
    