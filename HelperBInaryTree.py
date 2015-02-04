
        
    class Position():
        """This represent the location of single element."""
        
        def __init__(self,container,node):
            self._container = container
            self._node = node
            
        def element(self):
            """Return the element stored in this Position"""
            return self._node._element
    
    def _make_position(self,node):
        """ return Position instance instead of direct node"""
        return self.Postion(self,node) if node is not None else None
    
    # creating binary tree
    
    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        """return total number of nodes in the binary tree"""
        return self._size
    
    
    def root(self):
        """ Return root position of the tree"""
        return self._make_position(self._root)
    
    def parent(self, p):
        return self._make_position(p._parent)
    
    def left(self, p):
        return self._make_position(p._left)
    
    def right(self, p):
        return self._make_position(p._right)




LEFT = 0
RIGHT = 1
VALUE = 2
SORT_KEY = -1

class BinarySearchTree(object):

    def __init__(self, sort_key=None):
        self._root = []  
        self._sort_key = sort_key
        self._len = 0  

def insert(self, val):
    if self._sort_key is None:
        sort_key = val // if no sort key, sort key is value
    else:
        sort_key = self._sort_key(val)

    node = self._root
    while node:
        if sort_key < node[_SORT_KEY]:
            node = node[LEFT]
        else:
            node = node[RIGHT]

    if sort_key is val:
        node[:] = [[], [], val]
    else:
        node[:] = [[], [], val, sort_key]
    self._len += 1

def minimum(self):
    return self._extreme_node(LEFT)[VALUE]

def maximum(self):
    return self._extreme_node(RIGHT)[VALUE]

def find(self, sort_key):
    return self._find(sort_key)[VALUE]

def _extreme_node(self, side):
    if not self._root:
        raise IndexError('Empty')
    node = self._root
    while node[side]:
        node = node[side]
    return node

def _find(self, sort_key):
    node = self._root
    while node:
        node_key = node[SORT_KEY]
        if sort_key < node_key:
            node = node[LEFT]
        elif sort_key > node_key:
            node = node[RIGHT]
        else:
            return node
    raise KeyError("%r not found" % sort_key)