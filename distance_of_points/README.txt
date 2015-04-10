Problem Statement:
==================

Find the K closest points to the origin in 2D plane, given a stream of N points. 
Assume that N is too large to fit in memory. You can assume K is much smaller than 
N and N is very large. You need only use standard math operators: 
addition, subtraction, multiplication, and division. 


Platform:
==========
This source code will run in both windows and linux based platform machine.

Run the code:
=============

Step1:
-----

Keep all the source file in one directory.

Step 2:
------

change the directory into source file and run the below command. It has sample input data 
and it will return the output. 

Input:
******
[(0, 9), (-1, -8), (9, -7), (-3, 5), (-4, 5), (-8, -7), (-9, -10)]


$ python detect_closest_point.py

Output:
*******

List of K closest from origin:

[(-3, 5), (-4, 5), (-1, -8)]


Step 3:
-------

Please pass your inputs in this line number #91 which accepts list of tuples to this class "DetectClosestPoint()".

class attributes:

list_of_coord => Which contains the list of tuples of (x,y) coordinates.

k_closet_points => accepts integer values which is number of closest values we want to find from origin (0,0).
 
 
Testing:
-------
please run this test file which contains unit testing method.

$ python test_detect_closest_point.py

It will show the result of unit testing.


Extra files:
------------

utils.py => It is used to generate random coordinate numbers.
heap_distance.py => which does a heap algorithm logic.

 







