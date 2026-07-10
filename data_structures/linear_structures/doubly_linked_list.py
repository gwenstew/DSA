class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return f"Node(data = {self.data})"
    

class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def __len__(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def append(self, node):
        self.tail.next = node
        node.prev = self.tail

        if self.head is None:
            self.head = node
        self.count += 1

    def prepend(self, node):
        if self.head is None:
            self.tail = node
        node.next = self.head
        self.head = node
        self.count += 1

    def insert_after(self, data, node):
        cur = self.search(data)
        if cur is None:
            return -1
        
        temp = cur.next
        cur.next = node
        node.prev = cur
        node.next = temp
        self.count += 1

    def insert_before(self, data, node):
        cur = self.search(data)
        if cur is None:
            return -1
        
        temp = cur.prev
        node.next = cur
        cur.prev = node
        temp.next = node
        self.count += 1

    def delete(self, data):
        cur = self.search(data)
        if cur is None:
            return -1
        cur.prev.next = cur.next
        cur.next.prev = cur.prev
        self.count -= 1


    def deleteFront(self):
        if self.is_empty():
            return -1
        if self.count == 1:
            self.tail = self.head
        self.head = self.head.next
        self.head.prev = None
        self.count -= 1

    def deleteBack(self):
        if self.is_empty():
            return -1
        self.tail = self.tail.prev
        self.tail.next = None
        self.count -= 1

    def search(self, data):
        cur = self.head

        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def __repr__(self):
        if not self.head:
            return "Empty LinkedList"
        values = []
        cur = self.head
        while cur:
            values.append(repr(cur.data))
            cur = cur.next
        return " <-> ".join(values) + " <-> None"
