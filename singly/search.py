class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def search_element(head,target):
    current=head
    while current!=None:
        if current.data==target:
            return True
        else:
            False
        current=current.next
    return head
    
if __name__=="__main__":
    head=Node(10)
    head.next=Node(20)
    head.next.next=Node(30)
    head.next.next.next=Node(40)
    head=search_element(head,20)
    print(head)
    
    
    