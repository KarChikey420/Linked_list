class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def count_element(head):
   count=0
   current=head
   while current!=None:
       current=current.next
       count+=1
   return count
    
if __name__=="__main__":
    head=Node(10)
    head.next=Node(20)
    head.next.next=Node(30)
    head.next.next.next=Node(40)
    head=count_element(head)
    print(head)
    
    
    