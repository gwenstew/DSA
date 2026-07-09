"""
Singly Linked List

A linked list implementation where each Node holds a single `next` pointer
to the following node. Supports insertion at the front, back, and after a
given key; deletion from the front, back, or by key; search; and in-place
reversal.

Design notes:
- prepend/append/insert_after take pre-constructed Node objects rather than
  raw data, so the caller retains a reference to the inserted node (needed
  for operations like insert_after that require locating an existing node).
- search() returns the matching Node object, or None if not found. 

Methods:
- prepend(node)      - O(1)
- append(node)        - O(n) 
- insert_after(data, newNode) - O(n) 
- delete(data)        - O(n)
- deleteFront()       - O(1)
- deleteBack()        - O(n)
- search(data)        - O(n)
- reverse()           - O(n)
"""


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

    def __len__(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def prepend(self, node):
        if self.head:
            node.next = self.head
        self.head = node
        self.count += 1

    def append(self, node):
        if self.is_empty():
            self.head = node
            self.count += 1
            return
        
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node
        self.count += 1

    def insert_after(self, data, newNode):
        prev = self.search(data)
        if prev is None:
            return "Node not found"
        
        post = prev.next
        prev.next = newNode
        newNode.next = post
        self.count += 1


    def delete(self, data):
        if self.is_empty():
            return "Empty LinkedList; cannot perform operation"
        
        node = self.search(data)
        if node is None:
            return "Node not found"
        
        #case 1: node is head
        if self.head == node:
            self.head = self.head.next
            self.count -= 1
            return
        
        #case 2/3: node within list/node is tail
        prev = self.head
        cur = prev.next
        while cur:
            if cur == node:
                prev.next = cur.next
                self.count -= 1
                return
            prev = cur
            cur = cur.next
    

    def deleteFront(self):
        if self.is_empty():
            return "Empty LinkedList; cannot perform operation"
        
        temp = self.head.next
        self.head = temp
        self.count -= 1


    def deleteBack(self):
        if self.is_empty():
            return "Empty LinkedList; cannot perform operation"

        #case 1: only one node in list
        if self.head.next is None:
            self.head = None
            self.count -= 1
            return

        #case 2: traverse list and delete tail
        cur = self.head
        while cur.next.next:
            cur = cur.next
        cur.next = None
        self.count -= 1


    def search(self, data):
        #finds first occurance within the LL
        #returns node object or None if not found
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

        
    def reverse(self):
        cur = self.head
        prev = None

        while cur:
            temp = cur.next

            cur.next = prev
            prev = cur
            cur = temp
        
        self.head = prev

    def __repr__(self):
        if not self.head:
            return "Empty LinkedList"
        values = []
        cur = self.head
        while cur:
            values.append(repr(cur.data))
            cur = cur.next
        return " -> ".join(values) + " -> None"



def main():

    linklist = SinglyLinkedList()
    linklist.append(Node(10))
    linklist.append(Node(9))
    linklist.append(Node(8))
    print(linklist)
    linklist.reverse()
    print(linklist)
    

if __name__ == "__main__":
    main()
