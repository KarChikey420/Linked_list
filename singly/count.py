class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
def count_nodes(head):
        count=0
        curr=head
        while curr!=None:
            curr=curr.next
            count+=1
        return count
    
if __name__=="__main__":
    head=Node(1)
    head.next=Node(2)
    head.next.next=Node(3)
    
    count=count_nodes(head)
    print(count)