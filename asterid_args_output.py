## https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists

## function definitions

# non keyworded vars with the *-operator -- all the args left are wrapped up in a tuple. 
def single_asterid(v1, v2, *args):
	print(v1, v2, args)
single_asterid(1,2,3,4,5)
# (1, 2, (3, 4, 5))


# keyworded vars with the **-operator
def double_asterids(**kwargs):
	if kwargs is not None:
		for key,value in kwargs.items():
			print("Key: {}, Value: {}".format(key,value))
double_asterids(attr="soga")
# Key: attr, Value: soga


## parameter passings
def test_passing(k1,k2,k3):
	print(k1,k2,k3)

# # with *args
# args = (1,2,3)
# test_passing(*args)

# # with **kwargs
# kwargs = {"k1":1, "k2":2, "k3":3}
# test_passing(**kwargs)


# order when a mix of all situations
# def mix_asterids(args, *args, **kwargs):

# combined with os.path.join()
import os
def get_path(dir):
	return os.path.join(os.getcwd(), *dir)

print(get_path(["data", "parsed"]))
print(get_path(["data"]))


