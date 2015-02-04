    
class StackLinked():
    class _Node():
        def __init__(self, elem,next):
            self.ele = elem
            self.next = next
            
    def __init__(self,capacity):
        self._size = 0
        self._head = None
        self._tail = None
        self.stack_size = capacity
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def top(self):
        if self.is_empty():
            return "Stack is empty"
        
        return self._head.ele
    
    def push(self, elem):
        if self._size >= self.stack_size:
            return "Stack is full"
        if self.is_empty():
            self._tail = self._head = self._Node(elem,None)
        else:
            self._head = self._Node(elem,self._head)
            
        self._size += 1
    
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        
        item = self._head.ele
        self._head = self._head.next
        self._size -= 1
        return item
    
    def list_stack(self):
        item = self._head
        while True:
            if item is None:
                break
            print "\n".join(item.ele)
            item = item.next
            
        
        
capacity = 10
obj = StackLinked(capacity)
print obj.top()
obj.push(["sathish"])
obj.push(["kumar"])
obj.push(["divya"])
obj.push(["jayan"])
print "After push ============"
obj.list_stack()
print obj.pop()
print obj.pop()
print "After Pop"
obj.list_stack()