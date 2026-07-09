class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def display(head):
    cur = head
    while cur:
        print(cur.data, end=" ")
        cur = cur.next
    print()

def sort_descending(head):
    values = []
    cur = head
    while cur:
        values.append(cur.data)
        cur = cur.next

    values.sort(reverse=True)

    cur = head
    i = 0
    while cur:
        cur.data = values[i]
        i += 1
        cur = cur.next

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

sort_descending(head)

print("Sorted (descending) list:")
display(head)