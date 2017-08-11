from sklearn import preprocessing
import numpy as np

def normalize_output():
	'''sklearn.preprocessing.normalize() method'''
	X = np.array([[1.,-1.,2.],[2.,0.,0.],[0.,1.,-1.]])

	# # normalized on row
	# X_normalized, normalizer = preprocessing.normalize(X, norm='l2', return_norm=True, axis=0)

	# print(X)
	# # [[ 1. -1.  2.]
	# #  [ 2.  0.  0.]
	# #  [ 0.  1. -1.]]

	# print(X_normalized)
	# # [[ 0.4472136  -0.70710678  0.89442719]
	# #  [ 0.89442719  0.          0.        ]
	# #  [ 0.          0.70710678 -0.4472136 ]]
	# print(normalizer)	
	# # [ 2.23606798  1.41421356  2.23606798]

	# print(normalizer.T*X_normalized) # by default multiply columnwise.
	# # [[ 1. -1.  2.]
	# #  [ 2.  0.  0.]
	# #  [ 0.  1. -1.]]
	# print(normalizer.T*X_normalized==X)
	# # [[ True  True  True]
	# #  [ True  True  True]
	# #  [ True  True  True]]


	# normalized on col
	X_normalized, normalizer = preprocessing.normalize(X, norm='l2', return_norm=True, axis=1)

	print(X_normalized)
	# [[ 0.40824829 -0.40824829  0.81649658]
	#  [ 1.          0.          0.        ]
	#  [ 0.          0.70710678 -0.70710678]]
	print(normalizer)
	# [ 2.44948974  2.          1.41421356]
	print(normalizer[:, np.newaxis]) # note: add "np.newaxis" to allow multiply rowwise.
	# [[ 2.44948974]
	#  [ 2.        ]
	#  [ 1.41421356]]

	print(X_normalized*normalizer[:, np.newaxis])
	# [[ 1.         -0.81649658  1.15470054]
	#  [ 2.44948974  0.          0.        ]
	#  [ 0.          1.41421356 -1.        ]]
	print(X_normalized*normalizer[:, np.newaxis]==X)
	# [[ True  True  True]
	#  [ True  True  True]
	#  [ True  True  True]]

normalize_output()



