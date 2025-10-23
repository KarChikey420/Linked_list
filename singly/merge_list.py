class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
def merge_two_list(list1,list2):
    if not list1:
        return list2
    if not list2:
        return list1
    
    if list1.data<=list2.data:
        list1.next=merge_two_list(list1.next,list2)
        return list1
    else:
        list2.next=merge_two_list(list1,list2.next)
        return list2
    
def print_list(head):
    current=head
    while current!=None:
        print(current.data,end="->")
        current=current.next
        
if __name__=="__main__":
    a=Node(10)
    a.next=Node(15)
    a.next.next=Node(20)
    
    b=Node(5)
    b.next=Node(12)
    
    merge=merge_two_list(a,b)
    print_list(merge)