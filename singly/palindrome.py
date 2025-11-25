# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# def is_palindrome(head):
#     value=[]
#     current=head
#     while current!=None:
#         value.append(current.data)
#         current=current.next
    
#     if value==value[::-1]:
#         return True
#     return False

# if __name__=="__main__":
#     head=Node(1)
#     head.next=Node(2)
#     head.next.next=Node(3)
#     head.next.next.next=Node(2)
#     head.next.next.next.next=Node(1)
    
#     if is_palindrome(head):
#         print("Palindrome")
#     else:
#         print("Not a Palindrome")

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def reverse(head):
    previous=None
    current=head
    
    while current!=None:
        next_node=current.next
        current.next=previous
        previous=current
        current=next_node
    return previous

def is_palindrome(head):
    slow=head
    fast=head
    
    while fast!=None and fast.next!=None:
        slow=slow.next
        fast=fast.next.next
        
    second_half=reverse(slow)
    first_half=head
    
    while second_half!=None:
        if first_half.data !=second_half.data:
            return False
        first_half=first_half.next
        second_half=second_half.next
    return True

# def isPalindrome(head):
#         values=[]

#         current=head
#         while current:
#             values.append(current.data)
#             current=current.next
#         return values==values[::-1] 

if __name__=="__main__":
    head=Node(1)
    head.next=Node(2)
    head.next.next=Node(3)
    head.next.next.next=Node(2)
    head.next.next.next.next=Node(1)
    
    if is_palindrome(head):
        print("Palindrome")
    else:
        print("Not a Palindrome")