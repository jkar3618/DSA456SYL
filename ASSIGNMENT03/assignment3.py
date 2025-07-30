'''
Name: Taehwa Hong
Student ID: 132546227
'''

class SortedTable:
    class Record:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self, cap=32):
        self.the_table = [None for _ in range(cap)]
        self.cap = cap

    def insert(self, key, value):
        if self.search(key) is not None:    # O(n)
            return False

        if len(self) == self.cap:   # O(n)
            new_table = [None for _ in range(self.cap * 2)]     # O(n)
            for i in range(self.cap):   # O(n)
                new_table[i] = self.the_table[i]    # O(n)
            self.the_table = new_table  # O(1)
            self.cap *= 2   # O(1)

        self.the_table[len(self)] = self.Record(key, value) # O(n)
        size = len(self)

        # Bubble sort: O(n^2)
        for i in range(size - 1):
            for j in range(size - 1 - i):
                if self.the_table[j].key > self.the_table[j + 1].key:
                    self.the_table[j], self.the_table[j + 1] = self.the_table[j + 1], self.the_table[j]
        return True
    # Total Number of Operation: O(n) + O(n) + O(n^2)
    # Time Complexity: O(n^2)

    def modify(self, key, value):
        i = 0
        while i < len(self) and self.the_table[i].key != key:   # O(n)
            i += 1
        if i == len(self):
            return False
        else:
            self.the_table[i].value = value # O(1)
            return True
        # Total Number of Operation: O(n)
        # Time Complexity: O(n)

    def remove(self, key):
        i = 0
        size = len(self)    # O(n)
        while i < size and self.the_table[i].key != key:    # O(n)
            i += 1
        if i == size:
            return False
        while i + 1 < size: # O(n)
            self.the_table[i] = self.the_table[i + 1]
            i += 1
        self.the_table[i] = None    # O(1)
        return True
        # Total Number of Operation: O(n) + O(n)
        # Time Complexity: O(n)

    def search(self, key):
        i = 0
        size = len(self)    # O(n)
        while i < size and self.the_table[i].key != key:    # O(n)
            i += 1
        if i == size:
            return None
        else:
            return self.the_table[i].value  # O(1)
        # Total Number of Operation: O(n)
        # Time Complexity: O(n)

    def capacity(self):
        return self.cap # O(1)
    # Total Number of Operation: 1
    # Time Complexity: O(1)

    def __len__(self):
        count = 0
        for record in self.the_table:   # O(n)
            if record is not None:  # O(1)
                count += 1
        return count
    # Total Number of Operation: O(n)
    # Time Complexity: O(n)
