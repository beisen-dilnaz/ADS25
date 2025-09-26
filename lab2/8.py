class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_front(self, val):
        node = Node(val)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        print("ok")

    def add_back(self, val):
        node = Node(val)
        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        print("ok")

    def erase_front(self):
        if self.head is None:
            print("error")
        else:
            print(self.head.val)
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            else:
                self.head.prev = None

    def erase_back(self):
        if self.tail is None:
            print("error")
        else:
            print(self.tail.val)
            self.tail = self.tail.prev
            if self.tail is None:
                self.head = None
            else:
                self.tail.next = None

    def front(self):
        if self.head is None:
            print("error")
        else:
            print(self.head.val)

    def back(self):
        if self.tail is None:
            print("error")
        else:
            print(self.tail.val)

    def clear(self):
        self.head = None
        self.tail = None
        print("ok")


dll = DoublyLinkedList()

while True:
    command = input().split()
    if command[0] == "exit":
        print("goodbye")
        break
    elif command[0] == "add_front":
        dll.add_front(command[1])
    elif command[0] == "add_back":
        dll.add_back(command[1])
    elif command[0] == "erase_front":
        dll.erase_front()
    elif command[0] == "erase_back":
        dll.erase_back()
    elif command[0] == "front":
        dll.front()
    elif command[0] == "back":
        dll.back()
    elif command[0] == "clear":
        dll.clear()