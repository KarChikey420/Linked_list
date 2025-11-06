class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def reverse(head):
    current=head
    pre=None
    
    while current!=None:
        next_value=current.next
        current.next=pre
        pre=current
        current=next_value
    return pre
    
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
    head.next.next.next.next=Node(50)
    
    reverse=reverse(head)
    print_list(reverse)

   