import argparse

ap=argparse.ArgumentParser()

## no argument added
def no_args():	
	args = ap.parse_args()
	print(args)
# no_args() 
# > python argparser_output.py
# Namespace()



# add positional arguments
## echo
def echo_args():
	ap.add_argument("echo")
	args = ap.parse_args()
	print(args)
# echo_args() 
# > python argparser_output.py echo
# Namespace(echo='echo')

## verbosity
def v_args():
	ap.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true") # action="store_true" means to set its value to be true.
	args = ap.parse_args()
	if(args.verbose):
		print("v is in command line")
# v_args()
# > python argparser_output.py --verbose
# v is in command line
# > python argparser_output.py -v
# v is in command line

## square
def square_args():
	ap.add_argument("square", type=int, help="display a square of #s.")
	args = ap.parse_args()
	print(args.square**2)
# square_args()

## verbosity + square
def verb_square_comb():
	# ap.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
	ap.add_argument("-v", "--verbose", help="increase output verbosity", type=int, choices=[0,1,2])
	ap.add_argument("square", help="display a square of #s.", type=int)
	args = ap.parse_args()
	answer = args.square**2

	if(args.verbose==1):
		print("the square of {} equals {}".format(args.square, answer))
	elif(args.verbose==2):
		print("{}^2=={}".format(args.square, answer))
	else:
		print(answer)
# verb_square_comb()
# > python argparser_output.py 5 
# 25
# > python argparser_output.py 5 -v
# usage: argparser_output.py [-h] [-v {0,1,2}] square
# argparser_output.py: error: argument -v/--verbose: expected one argument
# > python argparser_output.py 5 -v 1
# the square of 5 equals 25
# > python argparser_output.py 5 -v 2
# 5^2==25
# > python argparser_output.py 5 -v 3
# usage: argparser_output.py [-h] [-v {0,1,2}] square
# argparser_output.py: error: argument -v/--verbose: invalid choice: 3 (choose from 0, 1, 2)

## verbose (count version) + square
def verb_square_comb_count():
	ap.add_argument("-v", "--verbose", help="increase output verbosity", action="count", default=0)
	ap.add_argument("square", help="display a square of #s.", type=int)
	args = ap.parse_args()
	answer = args.square**2

	print("Running {}".format(__file__))
	if(args.verbose==1):
		print("the square of {} equals {}".format(args.square, answer))
	elif(args.verbose==2):
		print("{}^2=={}".format(args.square, answer))
	else:
		print(answer)	
# verb_square_comb_count()
# > python argparser_output.py 5 
# 25
# > python argparser_output.py 5 -v
# the square of 5 equals 25
# > python argparser_output.py 5 -vv
# 5^2==25
# > python argparser_output.py 5 -vvv
# 25
# > python argparser_output.py 5 -v 1
# usage: argparser_output.py [-h] [-v] square
# argparser_output.py: error: unrecognized arguments: 1

## mutually exclusive group to avoid conflicts in optional arguments, and add descriptions.
ap2 = argparse.ArgumentParser(description="calculate X to the power of Y")
def mutually_exclusive():
	group = ap2.add_mutually_exclusive_group()

	# optional arguments 
	group.add_argument("-v", "--verbose", action="store_true")
	group.add_argument("-q", "--quiet", action="store_true")

	# positional arguments
	ap2.add_argument("x", type=int, help="the base")
	ap2.add_argument("y", type=int, help="the exponent")

	args = ap2.parse_args()
	answer = args.x**args.y

	if(args.quiet):
		print(answer)
	elif(args.verbose):
		print("{} to the power {} equals {}".format(args.x, args.y, answer))
	else:
		print("{}^{}=={}".format(args.x, args.y, answer))
mutually_exclusive()
# > python argparser_output.py 5 6
# 5^6==15625
# > python argparser_output.py 5 6 -q
# 15625
# > python argparser_output.py 5 6 -v
# 5 to the power 6 equals 15625
# > python argparser_output.py 5 6 -v -q
# usage: argparser_output.py [-h] [-v | -q] x y
# argparser_output.py: error: argument -q/--quiet: not allowed with argument -v/--verbose	

def get_customized_path():
	parser = argparse.ArgumentParser()
	parser.add_argument("--train", help="training data path")
	parser.add_argument("--test", help="test data path")
	parser.add_argument("--prediction-results", help="prediction data path")
	paths = parser.parse_args()
	return paths
paths = get_customized_path()
print(paths.train, paths.test, paths.prediction_results)
# > python test.py --train path_of_training_data.txt --prediction path_of_output_data.txt --test path_of_test_data.txt
# path_of_training_data.txt path_of_output_data.txt path_of_test_data.txt




