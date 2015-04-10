"""
Heap sort is used to keep the closest distance values of points from origin.

@author: Sathish kumar.S
@date: 21-Mar-2015
"""
import traceback

class HeapDistance():
    """
    Assumption : N is stream of data, 
                we cannot maintain all the data in memory and also it makes space complexity as O(n), 
                so we are restricting the heap list(array) size with K closest points.
    """ 
    class Item:
        """Dictionay key comparision"""
    
        def __init__(self, k, v):
            self._key = k
            self._value = v
    
        def __lt__(self, other):
            return self._key < other._key # compare items based on their keys
    
    def __init__(self,k_closest_points):
        """create a new empty list and max size of heap used of keeping K closest points."""
        self._data = [] 
        # restrict the maximum element in a list which is equivalent to K closest points
        self.heap_max_size = k_closest_points 
        
        
    def __len__(self):
        """ Return the number of items in the list."""
        return len(self._data)
    
    def _parent(self,ele):
        return (ele-1) // 2
    
    def _left(self,ele):
        return 2*ele + 1
    
    def _right(self,ele):
        return 2*ele + 2
    
    def _chk_left(self,ele):
        return self._left(ele) < len(self._data) # should go beyond the index
    
    def _chk_right(self,ele):
        return self._right(ele) < len(self._data)
    
    def swap(self,i,j):
        """swap the element in list"""
        self._data[i], self._data[j] = self._data[j], self._data[i]
    
    def _heapify_after_add(self,ele):
        """after the element is added at end of list we need heapify it"""
        parent = self._parent(ele)
        if ele > 0  and self._data[ele] < self._data[parent]:
            self.swap(ele, parent)
            self._heapify_after_add(parent)
         
    def _heapify_after_remove(self,ele):
        """after the element is removed from end of list we need heapify it"""
        
        if self._chk_left(ele):
            left = self._left(ele)
            find_small_child = left
            # below to find which child has small integer
            if self._chk_right(ele):
                right = self._right(ele)
                if self._data[left] > self._data[right]:
                    find_small_child = right
            
            if self._data[find_small_child] < self._data[ele]:
                self.swap(ele, find_small_child)
                self._heapify_after_remove(find_small_child)
        
        
    def add(self,key,value):
        """add values to list"""
        try:
            self._data.append(self.Item(key,value)) # insert as Item class object with key value.
            self._heapify_after_add(len(self._data) - 1 )
            return self._data
        except Exception, e:
            print "Error occurred in HeapDistance: add method", e
    
    def minimum_val(self):
        """return minimum value"""
        if self.is_empty():
            raise "List is Empty"
        item = self._data[0]
        return item._key, item._value
    
    def is_empty(self):
        if self._data == []:
            raise "List is empty"
    
    def remove_min(self):
        """remove the minimum value which is root node."""
        try:
            if self.is_empty():
                raise "List is Empty"
            
            self.swap(0,len(self._data)-1) 
            element = self._data.pop() # remove the value from list.
            self._heapify_after_remove(0) # heapify the list
            return element._key, element._value
        
        except Exception, e:
            print "Error occurred in HeapDistance: remove_min", e
            print traceback.print_exc(e)

if __name__ == "__main__":
    K_closest_point = 3
    obj = HeapDistance(K_closest_point)
    
    list_of_dict = [
                    {9 : (0, 9)}, 
                    {8 : (-1, -8)}, 
                     
                    {11 : (9, -7)},
                    {5 : (-3, 5)}, 
                    {6 : (-4, 5)},
                    {10 : (-8, -7)}, 
                    {12 : (-9, -10)},
                    ]
    
    for i in list_of_dict:
        for key, value in i.items():
            data =  obj.add(key, value)
            for i in data:
                print i._key
                print i._value
                print "END====="
        
        
    for i in range(len(list_of_dict)):
        print "Remove Elements..."
        print obj.remove_min()
    