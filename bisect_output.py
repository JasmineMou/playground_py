import bisect

def grade(score, breakpoints=[60,70,80,90], grades='FDCBA'):
	i = bisect.bisect(breakpoints, score)
	return grades[i]

# print [grade(score) for score in [0,99,32,80,100]]

def insertion_point(l, insert):
	left = bisect.bisect_left(l,insert) 
	right = bisect.bisect_right(l,insert) 
	print(l[left], l[right])

l1 = range(10)
l2 = [1,2,5,6] # sorted
l3 = [5,6,2,7] # unsorted
insertion_point(l1,4) 
# (4, 5)
insertion_point(l2,4)
# (2, 2)
insertion_point(l3,4)
# (7, 7)