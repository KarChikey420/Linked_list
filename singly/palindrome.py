class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def is_palindrome(head):
    value=[]
    current=head
    while current!=None:
        value.append(current.data)
        current=current.next
    
    if value==value[::-1]:
        return True
    return False

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