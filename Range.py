class Range():
    def __init__(self,start, stop=None, step=1):
        if step == 0:
            raise "Step cannot be zero"
        
        self._length = max(0,(stop-start + step - 1) // step)
        
        if stop is None:
            start, stop = 0, start
        
        if stop is not None:
            self.start = start
            self.stop = stop
            self.step = step
    
    def __len__(self):
        return self._length
    
    def __getitem__(self,key):
        if key < 0:
            key = self.length - key
        
        if key >= 0 and key > self._length:
            raise "Index error"
        
        return self.start + (key * self.step)
        
 
obj = Range(0,10,2)
print len(obj)
print obj[6]

   