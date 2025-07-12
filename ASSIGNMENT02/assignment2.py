class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class SortedLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        elif data < self.head.data:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            curr = self.head
            while curr.next and curr.next.data < data:
                curr = curr.next
            new_node.next = curr.next
            new_node.prev = curr
            if curr.next:
                curr.next.prev = new_node
            else:
                self.tail = new_node
            curr.next = new_node
        self.count += 1

    def remove(self, data):
        curr = self.head
        while curr:
            if curr.data == data:
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
                else:
                    self.tail = curr.prev
                self.count -= 1
                return True
            curr = curr.next
        return False

    def is_present(self, data):
        curr = self.head
        while curr:
            if curr.data == data:
                return True
            curr = curr.next
        return False

    def __len__(self):
        return self.count

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.data
            curr = curr.next
