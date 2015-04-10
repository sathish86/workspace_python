"""
This module will identify the K closest points from the orgin in 2D plane, given a stream of N points.
 
Assumption: Assume that N is too large to fit in memory. 
            K is much smaller than N and N is very large. 

@author: S.Sathish Kumar.
@data: 21-March-2015
"""
from heap_distance import HeapDistance
import math
import utils
import traceback
 
class DetectClosestPoint():
    
    """
    This class receives N points and it calculate each of the distance from orgin (0,0).
    For implement purpose we have declared set of N points.
    Once the distance is calculated it is passed to HeapDistance module which maintain the K closest points.
    
    Time complexity: 
    we need to process all the data which is O(N) and heap calculation O(logK), 
    so the overall time complexity would be O(NlogK)
    """
    
    def __init__(self, N_points= [], k_points=0):
        """ 
        Initialise the required attributes like N points in list, K closest point as integer,
        and create a object of HeapDistance to maintain K closest points.
        """
        
        self._data = N_points # list of tuples which contains (x2,y2) coordinate
        self._origin = (0,0) # (x1, y1) coordinate points.
        self._k_closest = k_points
        self.heap = HeapDistance(self._k_closest)
        
    def __len__(self):
        return len(self._data)
    
    def _get_distance(self,coord):
        """
        it uses the formula to identify the distance of two points.
        """
        try:
            x1 = self._origin[0]
            y1 = self._origin[1]
            
            x2 = coord[0]
            y2 = coord[1]
            
            value = pow((x2 - (x1)), 2 ) + pow((y2 - (y1)), 2 )
            result = round(math.sqrt(value),2) # the value is rounded to 2 decimal points.
            return result
        except Exception,e :
            print "Error occurred in DetectClosestPoint: _get_distance"
            print traceback.print_exc(e)
            
    def calc_distance(self):
        """
        it will iterate each points and calculate the distance from the origin
        """
        try:
            for ele in self._data:
                distance = self._get_distance(ele)
                self.heap.add(distance, ele)
        except Exception, e:
            print "Error occurred in DetectClosestPoint: calc_distance method:"
            print traceback.print_exc(e) 
            
    def return_closest_points(self):
        """
        Return the K closest point from orgin.
        """
        try:
            
            closest_coord = []
            for rec in range(self._k_closest):
                distance, coord = self.heap.remove_min()
                closest_coord.append(coord)
            print "List of K closest from origin: \n"
            print closest_coord
            
            return closest_coord 
        except Exception, e:
            print "Error occurred in DetectClosestPoint: return_closest_points", e
            print traceback.print_exc(e)
            
if __name__ == "__main__":
    
    list_of_coord = [
                    (0, 9), 
                    (-1, -8), 
                    (9, -7),
                    (-3, 5), 
                    (-4, 5),
                    (-8, -7), 
                    (-9, -10),
                    ]
    #list_of_coord = utils.generate_coordinates()
    print list_of_coord
    k_closet_points = 3
    obj = DetectClosestPoint(list_of_coord, k_closet_points)
    obj.calc_distance()
    obj.return_closest_points()
    