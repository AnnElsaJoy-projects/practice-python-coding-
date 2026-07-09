class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def display(value):
    cur = value
    values = []
    while cur:
        values.append(str(cur.data))
        cur = cur.next
    print(" <-> ".join(values))

def reverse(value):
    cur = value
    new_head = None
    while cur:
        cur.prev, cur.next = cur.next, cur.prev  
        new_head = cur
        cur = cur.prev  
    return new_head

n1 = Node(34)
n2 = Node(4)
n3 = Node(10)
n4 = Node(67)

n1.next = n2
n2.prev = n1
n2.next = n3
n3.prev = n2
n3.next = n4
n4.prev = n3

head = n1

print("Original list:")
display(head)

head = reverse(head)

print("Reversed list:")
display(head)