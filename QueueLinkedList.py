    
class QueueLinked():
    class _Node():
        def __init__(self, elem,next):
            self.ele = elem
            self.next = next
            
    def __init__(self,capacity):
        self._size = 0
        self._head = None
        self._tail = None
        self.queue_size = capacity
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def top(self):
        if self.is_empty():
            return "Stack is empty"
        
        return self._head.ele
    
    def enqueue(self, elem):
        if self._size >= self.queue_size:
            return "Queue is full"
        if self.is_empty():
            self._tail = self._head = self._Node(elem,None)
        else:
            self._tail.next = self._Node(elem,None)
            self._tail = self._tail.next
            
        self._size += 1
    
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        
        item = self._head.ele
        self._head = self._head.next
        self._size -= 1
        return item
    
    def list_queue(self):
        item = self._head
        while True:
            if item is None:
                break
            print "\n".join(item.ele)
            item = item.next
            
        
        
capacity = 10
obj = QueueLinked(capacity)
print obj.top()
obj.enqueue(["sathish"])
obj.enqueue(["kumar"])
obj.enqueue(["divya"])
obj.enqueue(["jayan"])
print "After Enqueue ============"
obj.list_queue()
print obj.dequeue()
print obj.dequeue()
print "After Dequeue"
obj.list_queue()