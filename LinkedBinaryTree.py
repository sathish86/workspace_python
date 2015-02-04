"""
This Binary tree will do the following operation.
1. insertion
2. max value in binary tree
3. min value in binary tree
4. Total size of binary tree
5. save binary tree in text file.
6. read the values from text file and make binary tree.
7. traverse inorder and preorder.
8. delete operation with 3 possibilities.

"""

class LinkedBinaryTree():
    class _Node():
        def __init__(self,element,parent=None,left=None, right=None):
            self._left = left
            self._right = right
            self._parent = parent
            self._element = element
        
        def __str__(self):
            return str(self._element)
        
    # creating binary tree
    def __init__(self):
        self._root = None
        self._size = 0
        self.type = "" # this attribute is used for traverse extreme left or right.
        self._fileobj = None # attribute is used for reading binary tree text file.
        
    def __len__(self):
        """return total number of nodes in the binary tree"""
        return self._size
    
    def total_size(self):
        """return total element in binary tree"""
        return self._size
    
    def root(self):
        """return root element in binary tree"""
        return self._root
    
    def search(self,key,node=None):
        """search the binary tree and return the element in O(logn) time."""
        
        if self.root() is None:
            raise ValueError("Binary Tree is Empty")
        
        if node is None:
            return None, None # this return both parent, lookup element as None
        
        if node._element == key:
            return node._parent, node # this return parent and lookup node objects.
        elif node._element > key:
            return self.search(key,node._left)
        elif node._element < key:
            return self.search(key,node._right)
        
    
    def insert(self,ele,node=None):
        """insert elements in binary tree using property"""
        if self._root is None:
            self._root = self._Node(ele)
            self._size += 1
            return self._root._element
        
        if node is None:
            node = self._root
    
        if node._element >= ele:
            if node._left is None:
                node._left = self._Node(ele,parent=node)
                print node._left._element
                self._size += 1
            else:
                self.insert(ele, node._left)
            
        
        elif node._element <= ele:
            if node._right is None:
                node._right = self._Node(ele,parent=node)
                print node._right._element
                self._size += 1
            else:
                self.insert(ele, node._right)
            

    def inorder(self, node=None):
        """It traverse and print the inorder of binary tree data."""
         
        if self._root is None:
            raise ValueError("Tree is Empty")
        
        if node is None:
           return
        
        self.inorder(node._left)
        print node._element
        self.inorder(node._right)
        
    def _create_bt_file(self):
        """ create binary tree file"""
        self._fileobj = open("binary_tree.txt","w")
        
    def save_binarytree(self,ele):
        """it saves the binary tree in a txt file"""
        if self._fileobj is None:
            self._create_bt_file()
            
        self._fileobj.write(str(ele)+"\n")
        
        
    def preorder(self, node=None,save=False):
        """It traverse in preorder of binary tree data and saves the data's in txt file"""
        
        if self._root is None:
            raise ValueError("Tree is Empty")
        
        if node is None:
           return
         
        print node._element
        if save:
            self.save_binarytree(node._element)
            
        self.preorder(node._left,save)
        self.preorder(node._right,save)
        
    def _extreme(self,node):
        """ it traverse extreme left/right level of the tree """
        node = self._root
        while node:
            if self.type == "left":
                curr = node
                node = node._left
            else:
                curr = node
                node = node._right
                
            if node is None:
                break
                
        return curr._element
                
    def minimum(self):
        """Returns the least value from the tree"""
        self.type = "left"
        return self._extreme(self._root._left)
    
    def maximum(self):
        """Returns the highest value from the tree"""
        self.type = "right"
        return self._extreme(self._root._right)
    
    
    def read_bt_file(self):
        """
        It reads the binary tree text file and form the tree object.
        We can also use Pickle file to store the tree object which is easy and convenient to read back
        """
        self._fileobj = open("binary_tree.txt","r")
        
        for rec in self._fileobj.readlines():
            self.insert(int(rec))
            
        self._fileobj.close()
    
    def children_count(self,node):
        """It count the children of particular node."""
        count = 0
        if node._left is not None:
            count +=1
        if node._right is not None:
            count +=1 
        return count
    
    def delete(self,key):
        """delete a element from binary tree"""
        parent, node = self.search(key, self.root())
        if node:
            children = self.children_count(node)
            if children == 0:
                # node has no children, which mean its a leaf node.
                if parent:
                    if parent._left == node:
                        parent._left = None
                    else:
                        parent._right = None
                    del node
                else:
                    node._element = None
                    
            elif children == 1:
                if node._left is not None:
                    temp = node._left
                else:
                    temp = node._right
                    
                if parent:
                    if parent._left == node:
                        parent._left = temp
                    else:
                        parent._right = temp
                    del node
                else:
                    # incase the delete is happening on root node.
                    self._root._left = temp._left
                    self._root._right = temp._right
                    self._root._element = temp._element
              
            else:
                # node has two children
                parent = node
                successor = node._right
                while successor._left:
                    parent = successor
                    successor = successor._left
                
                node._element = successor._element
                if parent._left == successor:
                    parent._left = successor._right
                else:
                    parent._right = successor._right
            
    
if __name__ == "__main__":
    obj = LinkedBinaryTree()
    a= [10,5,17,8,2,20,25,1,30,4]
    for i in a:
        obj.insert(i)
    
    print "In-order"
    print obj.inorder(obj.root())
    print "Pre order"
    print obj.preorder(obj.root(),True)
    
    print  "_-------"
    print obj.minimum()
    print obj.maximum()
    print obj.total_size()
    obj = None
    import pdb; pdb.set_trace()
    print "Object became None"
    
    obj = LinkedBinaryTree()
    obj.read_bt_file()
    #print obj.total_size()
    print "Final "
    print obj.preorder(obj.root())
    print "Search Result:"
    parent, ele = obj.search(1,obj.root())
    obj.delete(30)
    print "After delete 1:"
    print obj.inorder(obj.root())
    obj.delete(17)
    print "After delete 2:"
    print obj.inorder(obj.root())
    obj.delete(5)
    print "After delete 3:"
    print obj.inorder(obj.root())