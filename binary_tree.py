class BinaryTree():
    class Node():
        def __init__(self,element,left=None,right=None ):
            self.left = left
            self.right = right
            self.element = element
            
        def __str__(self):
            return str(self.element)
            
    def __init__(self,ele):
        self.root = self.Node(ele)
        
    def insert(self,value,parent=None):
        
        if parent is None:
            self.root = self.Node(value)
            return self.root
        
        if parent.element > value:
            #parent = parent.left
            if parent.left is None:
                parent.left = self.Node(value)
                return parent
            
            parent = parent.left
            self.insert(value,parent)
            
        elif parent.element < value:
            if parent.right is None:
                parent.right = self.Node(value)
                return parent
            
            parent = parent.right
            self.insert(value,parent)
        
    def search(self,key,parent=None):
        import pdb; pdb.set_trace()
        if parent is None:
            return "Couldn't find"
        
        if parent.element == key:
            return parent.element, self
        
        if parent.element > key:
            return self.search(key,parent.left), self
        elif parent.element < key:
            return self.search(key,parent.right) , self
        
        
    def printTree(self,root):
        if root == None:
            pass
        else:
            self.printTree(root.left)
            print root.element
            self.printTree(root.right)
        
        
a = [10,23,5,78,213,2]
import pdb;pdb.set_trace()
obj = BinaryTree(a[0])
for i in a[1:]:
    obj.insert(i,obj.root)
        
ele, parent = obj.search(23,obj.root)
import pdb; pdb.set_trace()
obj.printTree(obj.root)

