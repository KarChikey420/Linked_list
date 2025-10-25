class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
def middle_node(head):
    slow=head
    fast=head
    
    while fast!=None and fast.next!=None:
        slow=slow.next
        fast=fast.next.next
    return slow
    
def print_list(head):
    current=head
    while current!=None:
        print(current.data,end="->")
        current=current.next

if __name__=="__main__":
    head=Node(10)
    head.next=Node(20)
    head.next.next=Node(30)
    head.next.next.next=Node(40)
    head.next.next.next.next=Node(50)
    
    mid=middle_node(head)
    print("middle node",mid.data)








    