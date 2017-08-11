# normal way, assigning l1 to a different location, then l0 will not be affected. 
l0 = ['a','b','c',['ab','ba']]
l1 = l0
l1 = ['x','y','z']
print(l0, l1)

# normal way, change an element in l1 or add/delete element will affect l0.
l0 = ['a','b','c',['ab','ba']]
l1 = l0
l1[0] = 'e'
# l1.append(10)
print(l0, l1)

# copy with slicing/copy.copy, change l1 will not affect single element in l0, but will affect the sublist element. 
# http://www.python-course.eu/deep_copy.php

l0 = ['a','b','c',['ab','ba']]
l2 = l0[:] 
# l2=copy(l0)
l2[0] = 'e'
l2[-1][-1] = 'f'
print(l0, l2)

# copy with deepcopy, problem solved
from copy import deepcopy
l0 = ['a','b','c',['ab','ba']]
l3 = deepcopy(l0)
l3[0] = 'e'
l3[-1][-1] = 'f'
print(l0, l3)


