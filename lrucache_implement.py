class Node:   
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cacheStore={}
        self.head=None
        self.tail=None
        

    def get(self, key: int) -> int:  ## complexity O(1)
        if key in self.cacheStore:
            new_node =  self.cacheStore.get(key)
            self.movetoHead(new_node)
            return new_node.value
        return -1
            
    def put(self, key: int, value: int) -> None:  ## complexity O(1)
        
        if key in self.cacheStore:
            new_node = self.cacheStore.get(key)
            self.movetoHead(new_node)
            new_node.value=value
        else:
            if len(self.cacheStore) >= self.capacity:
                self.removeFromTail()
            new_node = Node(key,value)
            self.addHead(new_node)
            self.cacheStore[key]=value
            
    def movetoHead(self,data):
        if data==self.head:
            return
        elif data==self.tail:
            self.tail=self.tail.prev
            self.tail.next=None
            self.addHead(data)
        else:
            data.prev.next=data.next
            data.next.prev = data.prev
            self.addHead(data)
    
    def removeFromTail(self):
        if self.tail and self.tail.prev:
            self.tail.next = None
        else:
            self.head=None
        if self.tail:
            self.cacheStore.pop(self.tail.key)
            self.tail = self.tail.prev
    
    def addHead(self,data):
        if self.head is None:
            self.head=self.tail=data
        else:
            data.next=self.head
            self.head.prev=data
            self.head=data
        
        
            
            
            
        