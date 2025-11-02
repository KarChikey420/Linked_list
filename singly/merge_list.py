# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
        
# def merge_two_list(list1,list2):
#     if not list1:
#         return list2
#     if not list2:
#         return list1
    
#     if list1.data<=list2.data:
#         list1.next=merge_two_list(list1.next,list2)
#         return list1
#     else:
#         list2.next=merge_two_list(list1,list2.next)
#         return list2
    
# def print_list(head):
#     current=head
#     while current!=None:
#         print(current.data,end="->")
#         current=current.next
        
# if __name__=="__main__":
#     a=Node(10)
#     a.next=Node(15)
#     a.next.next=Node(20)
    
#     b=Node(5)
#     b.next=Node(12)
    
#     merge=merge_two_list(a,b)
#     print_list(merge)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_list(list1, list2):
    dummy = Node(0)
    current = dummy

    while list1 is not None and list2 is not None:
        if list1.data <= list2.data:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    if list1 is not None:
        current.next = list1
    else:
        current.next = list2

    return dummy.next

def print_list(head):
    current = head
    while current is not None:
        print(current.data, end="->")
        current = current.next
    print("None")

if __name__ == "__main__":
    a = Node(1)
    a.next = Node(3)
    a.next.next = Node(5)

    b = Node(2)
    b.next = Node(4)

    merged = merge_list(a, b)
    print_list(merged)
