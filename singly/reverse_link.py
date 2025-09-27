class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def reverse(head):
    prev = None
    curr = head
    
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

def print_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    
    head = reverse(head) 
    print_list(head)
