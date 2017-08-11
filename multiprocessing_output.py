# from multiprocessing import Queue, Process, Lock
from Queue import Queue

# queue


def try_queue():
	q = Queue()
	for i in range(10):
		q.put(i)

	p = Queue()
	for j in iter(q.get,8):
		p.put(j)

	# option 1, use while, works. 
	while not p.empty():
		print(p.get())

	# option 2, use iter(), doesn't work
	# for k in iter(p.get, None): # None is the sentinel here
	# 	print(k)

try_queue()


# Lock
def printer(single_item, lk):
	lk.acquire()
	try:
		print(single_item)
	finally:
		lk.release()

def print_with_lock():
	lock = Lock()
	to_print = ["hello", 123, "world"]

	# create a process for each item
	for i in to_print:
		p = Process(target=printer, args=(i, lock)) 
		p.start()

# print_with_lock()

