class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_last(head):
    if head is None or head.next is None:
        return None

    temp = head

    while temp.next.next is not None:
        temp = temp.next

    temp.next = None
    return head

def display(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

print("Before deletion:")
display(head)

head = delete_last(head)

print("After deletion:")
display(head)