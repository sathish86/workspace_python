
import unittest
from detect_closest_point import DetectClosestPoint


class TestDetectClosestPoint(unittest.TestCase):

    def setUp(self):
        self.k_closest_point = 3
        self.list_of_coord = [
                                (0, 9), 
                                (-1, -8), 
                                (9, -7),
                                (-3, 5), 
                                (-4, 5),
                                (-8, -7), 
                                (-9, -10),
                                ]
        
        self.detect_obj = DetectClosestPoint(self.list_of_coord, self.k_closest_point)
        
        

    def test_heap_data(self):
        """ call the method and check the output. """
        
        self.detect_obj.calc_distance()
        self.assertEqual([(-3, 5), (-4, 5), (-1, -8)], self.detect_obj.return_closest_points())
    
    
    def test_heap_value(self):
        """check the distance for that coordinated are returned back."""
        
        self.detect_obj.calc_distance()
        self.assertEqual(5.83, self.detect_obj.heap._data[0]._key)
    
     
if __name__ == '__main__':
    unittest.main()