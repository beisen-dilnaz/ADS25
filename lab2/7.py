class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insert(head: Node, node: Node, p: int):
    if p == 0:  # insert at head
        node.next = head
        return node
    cur = head
    for _ in range(p - 1):
        cur = cur.next
    node.next = cur.next
    cur.next = node
    return head

def remove(head: Node, p: int):
    if not head:
        return None
    if p == 0:
        return head.next
    cur = head
    for _ in range(p - 1):
        cur = cur.next
    if cur.next:
        cur.next = cur.next.next
    return head

def printAll(head: Node):
    if not head:
        print(-1)
        return
    cur = head
    res = []
    while cur:
        res.append(str(cur.val))
        cur = cur.next
    print(" ".join(res))

def replace(head: Node, p1: int, p2: int):
    if p1 == p2:
        return head
    dummy = Node(0, head)
    prev1 = dummy
    for _ in range(p1):
        prev1 = prev1.next
    node1 = prev1.next
    prev1.next = node1.next
    cur = dummy
    for _ in range(p2):
        cur = cur.next
    node1.next = cur.next
    cur.next = node1
    return dummy.next

def reverse(head: Node):
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev

def cyclic_left(head: Node, x: int):
    if not head or not head.next:
        return head
    # find length
    n = 0
    cur = head
    while cur:
        n += 1
        cur = cur.next
    x %= n
    if x == 0:
        return head
    cur = head
    for _ in range(x - 1):
        cur = cur.next
    new_head = cur.next
    cur.next = None
    tail = new_head
    while tail.next:
        tail = tail.next
    tail.next = head
    return new_head

def cyclic_right(head: Node, x: int):
    if not head or not head.next:
        return head
    n = 0
    cur = head
    while cur:
        n += 1
        cur = cur.next
    x %= n
    if x == 0:
        return head
    return cyclic_left(head, n - x)


head: Node = None

while True:
    try:
        vals = [int(i) for i in input().split()]
    except EOFError:
        break
    if not vals:
        continue
    if vals[0] == 0:
        break
    elif vals[0] == 1:
        head = insert(head, Node(vals[1]), vals[2])
    elif vals[0] == 2:
        head = remove(head, vals[1])
    elif vals[0] == 3:
        printAll(head)
    elif vals[0] == 4:
        head = replace(head, vals[1], vals[2])
    elif vals[0] == 5:
        head = reverse(head)
    elif vals[0] == 6:
        head = cyclic_left(head, vals[1])
    elif vals[0] == 7:
        head = cyclic_right(head, vals[1])