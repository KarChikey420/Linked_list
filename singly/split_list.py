class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def split_list(head):
    previous=None
    slow=head
    fast=head
    
    while fast!=None and fast.next!=None:
        previous=slow
        slow=slow.next
        fast=fast.next.next
    previous.next=None
    
    return head,slow

def print_list(head):
    current=head
    while current!=None:
        print(current.data,end="->")
        current=current.next
    print("None")
    
if __name__=="__main__":
    head=Node(10)
    head.next=Node(20)
    head.next.next=Node(30)
    head.next.next.next=Node(40)
    
    first,second=split_list(head)
    print_list(first)
    print()
    print_list(second)
    
    
    
    
    
    
    
    
    
    