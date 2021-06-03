#q.6: Write a Python program to convert an array to an array of machine values and return the bytes representation.

from array import *

x = array('b', [1, 2, 3, 4, 5, 6])
s = x.tobytes()
print(s)