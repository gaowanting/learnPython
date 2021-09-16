from collections import namedtuple
# factory function for creating tuple subclasses with named fields
# they add the ability to access fields by name instead of position index.
p = namedtuple("point", "x y")
A = p(4, 5)
print(A.x)
print(A.y)