class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def sum_element(head):
    add=0
    current=head
    while current!=None:
        sum+=current.data
        current=current.next
    return sum
    
if __name__=="__main__":
    head=Node(10)
    head.next=Node(20)
    head.next.next=Node(30)
    head.next.next.next=Node(40)
    head=sum_element(head)
    print(head)
    
    
    