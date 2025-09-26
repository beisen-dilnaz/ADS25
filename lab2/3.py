class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def delete_every_second(self):
        cur = self.head
        while cur and cur.next:
            cur.next = cur.next.next
            cur = cur.next

    def print_list(self):
        cur = self.head
        res = []
        while cur:
            res.append(str(cur.val))
            cur = cur.next
        print(" ".join(res))

n = int(input())
nums = list(map(int, input().split()))

ll = LinkedList()
for x in nums:
    ll.add(x)

ll.delete_every_second()
ll.print_list()