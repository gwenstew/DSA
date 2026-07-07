""" 
Hash Table - Separate Chaining

A hash table implementation that resolves collisions via separate chaining,
using a linked list of Nodes per bucket. Each bucket starts with a head
Node (key=-1, value=-1) so inserts/deletes/searches can walk the list
uniformly without null-checking the bucket itself.

Features:
- Dynamic resizing: buckets double in size once the load factor reaches
  `max_load_factor` (0.75), keeping average lookup/insert close to O(1).
- `insert`  - O(1) average, O(n) worst case (all keys collide into one bucket)
- `search`  - O(1) average, O(n) worst case
- `delete`  - O(1) average, O(n) worst case
- `resize`  - O(n), amortized O(1) per insert over time

"""

class Node:
    # Nodes are initialized to -1 since the hash function cannot hash to a negative value
    def __init__(self, key = -1, value = -1, next= None):
        self.key = key
        self.value = value
        self.next = next


class HashTable:

    def __init__(self, size=1000):
        self.buckets = []
        self.size = size
        self.max_load_factor = 0.75
        self.count = 0
        self.resizing = 0
        self.buckets = [Node() for _ in range(self.size)]


    def clear(self):
        self.buckets = [Node() for _ in range(self.size)]
        self.count = 0


    def hashFunction(self, key):
        return hash(key) % len(self.buckets)
    
    def insert(self, key, value):
        # either update key value pair or insert into bucket (handle collisions)
        hashidx = self.hashFunction(key)
        cur = self.buckets[hashidx]

        while cur.next:
            # update value
            if cur.next.key == key:
                cur.next.value = value
                return
            cur = cur.next

        #insert new pair
        self.count += 1
        cur.next = Node(key, value)

        if self.load_balance() >= self.max_load_factor and not self.resizing:
            self.resize()

        
    
    def delete(self, key):
        #find and delete key
        #A: how would you change this function for a language that does not handle mem management?
        cur = self.buckets[self.hashFunction(key)]

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                self.count -= 1
                return

    
    def search(self, key):
        cur = self.buckets[self.hashFunction(key)]
        while cur.next:
            if cur.next.key == key:
                return cur.next.value
            cur = cur.next
        return "Key not found"
    
    def resize(self):
        self.resizing = 1
        self.count = 0
        old_buckets = self.buckets
        old_size = self.size
        self.size = self.size * 2
        self.buckets = [Node() for _ in range(self.size)]

        for idx in range(old_size):
            cur = old_buckets[idx]
            while cur.next:
                self.insert(cur.next.key, cur.next.value)
                cur = cur.next
        self.resizing = 0

    
    
    def load_balance(self):
        return self.count / self.size
    
