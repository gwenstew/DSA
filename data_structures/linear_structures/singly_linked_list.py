class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node(data = {self.data})"
    

class SinglyLinkedList():
    def __init__(self):
        self.count = 0
        self.head = None
        pass

    def __len__(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def prepend(self, node):
        if self.head:
            node.next = self.head
        
        self.head = node

    def append(self, node):
        cur = self.head
        while cur.next:
            cur = cur.next
        
        cur.next = node

    def insert_after(self, prevnode, newnode):
        #ISSUES: this should use a search function to ensure that the node exists in the LL
        if prevnode.next == None:
            prevnode.next = newnode
            return
        
        temp = prevnode.next
        prevnode.next = newnode
        newnode.next = temp


    def delete(self, node):
        pass

    def deleteFront(self):
        pass

    def deleteBack(self):
        pass


    def search(self, key):
        pass

    def reverse(self):
        pass

    def __repr__(self):
        if not self.head:
            return "Empty LinkedList"
        values = []
        cur = self.head
        while cur:
            values.append(repr(cur.data))
            cur = cur.next
        return " -> ".join(values) + " -> None"




