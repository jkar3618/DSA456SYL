'''
Name: Taehwa Hong
Student ID: 132546227
'''


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class SinglyLinkedList:
    def __init__(self):
        self.head = None 

    def is_empty(self):
        return self.head is None

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_after(self, target, data):
        if target is None:
            return
        new_node = Node(data)
        new_node.next = target.next
        target.next = new_node

    def delete(self, target):
        if self.is_empty() or target is None:
            return False

        if self.head == target:
            self.head = self.head.next
            return True

        current = self.head
        while current.next and current.next != target:
            current = current.next

        if current.next == target:
            current.next = target.next
            return True

        return False

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def print(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
