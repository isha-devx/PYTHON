"""
my_tuple = (1, 2, 3, 4)
my_tuple = 1, 2, 3, 4
#my_tuple = 1,   # this will be tuple since comma is there.
#my_tuple = (1)   # this will be integer since only one element is there.
print(my_tuple, type(my_tuple))

#UNPACKING
a, b, c, d = 1, 2, 3, 4   #TUPLE UNPACKING
a, b, c, d = [1, 2, 3, 4]   #LIST UNPACKING
print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))
"""

a, b, c, d = 1, 2, 3, "ISHA"  #TUPLE UNPACKING
print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))