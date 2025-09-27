class Node:
    def __init__(self,data):
       self.data=data
       self.next=None

def sum_of_node(head):
    curr=head
    sum=0
    while curr!=None:
        sum+=curr.data
        curr=curr.next
    return sum

if __name__=="__main__":
    head=Node(1)
    head.next=Node(2)
    head.next.next=Node(3)
    head.next.next.next=Node(4)
    
    sum=sum_of_node(head)
    print(sum)