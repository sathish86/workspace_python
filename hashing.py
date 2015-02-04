class Hashing():
    def __init__(self):
        import pdb; pdb.set_trace()
        self.size = 11
        self.slot = [None] * self.size
        self.data = [None] * self.size
        
    def hashing(self,key,size):
        return (key%size)
    
    def rehashing(self,old_key,size):
        return (old_key+1%size)
    
    def put(self,key,value):
        import pdb; pdb.set_trace()
        hash_key = self.hashing(key,self.size)
        if self.slot[hash_key] == None:
            self.slot[hash_key] = key
            self.data[hash_key] = value
        else:
            if self.slot[hash_key] == key:
                self.data[hash_key] = value
            else:
                new_hash_key = self.rehashing(hash_key,self.size)
                while self.slot[new_hash_key] != None and self.slot[new_hash_key] != key:
                    #self.data[new_hash_key] = value
                    new_hash_key = self.rehashing(new_hash_key,self.size)
                    
                self.slot[new_hash_key] = key
                self.data[new_hash_key] = value
    
    
    def get(self,key):
        #import pdb; pdb.set_trace()
        hash_key = self.hashing(key,self.size)
        position = hash_key
        if self.slot[hash_key] == key:
            print self.data[hash_key]
            return (self.data[hash_key])
        else:
            new_hash_key = self.rehashing(hash_key,self.size)
            while position != new_hash_key:
                if self.slot[new_hash_key] == key:
                    return self.data[new_hash_key]
                else:
                    new_hash_key = self.rehashing(new_hash_key,self.size)
            return "object not found"
        
    def __getitem__(self,key):
        self.get(key)
                     
    def __setitem__(self,key,value):
        self.put(key,value)
            
        
H = Hashing()
H[12] = 'sathish'
H[23] = 'kumar'
print H.slot
a = H[12]
print a
print H.data 