class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def insertPos(head, pos, val):

    if pos < 1:
        return head

    if pos == 1:
        newNode = Node(val)
        newNode.next = head
        return newNode

    curr = head

    for i in range(1, pos - 1):
        if curr is None:
            return head
        curr = curr.next

    if curr is None:
        return head

    newNode = Node(val)

    newNode.next = curr.next
    curr.next = newNode

    return head

def printList(head):
    curr = head
    while curr:
        print(curr.val, end="")
        if curr.next:
            print(" -> ", end="")
        curr = curr.next
    print()

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(4)
    
    val, pos = 3, 3
    head = insertPos(head, pos, val)
    printList(head)