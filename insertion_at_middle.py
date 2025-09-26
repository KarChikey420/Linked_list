class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    @staticmethod
    def insert_at_middle(head, data, position):
        new_node = Node(data)
        current = head
        while current is not None and current.data != position:
            current = current.next
        if current is None:
            # Position not found, do not insert
            print("Position not found")
            return head
        new_node.next = current.next
        current.next = new_node
        return head

node =Node(10)
node1=Node(20)
node2=Node(30)
node3=Node(40)

node.next=node1
node1.next=node2
node2.next=node3
node3.next=None

head=node
head=Node.insert_at_middle(head,25,20)

