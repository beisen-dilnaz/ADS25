class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertNode(head, data, position):
    new_node = Node(data)
    if position == 0:
        new_node.next = head
        return new_node
    current = head
    for i in range(position - 1):
        current = current.next
    new_node.next = current.next
    current.next = new_node
    return head

n = int(input())
values = [int(input()) for _ in range(n)]
data = int(input())
pos = int(input())

head = Node(values[0])
cur = head
for i in range(1, n):
    cur.next = Node(values[i])
    cur = cur.next

head = insertNode(head, data, pos)

cur = head
while cur:
    print(cur.data, end=" ")
    cur = cur.next