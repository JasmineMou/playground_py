import pickle

# dumps(), loads() function returns/reads a bytes object
# dump(), load() function return/read a stream object

# without 's' and interact with file

def save_pkl():
	dict = {'lion':'yellow', 'cat':'red'}
	pickle.dump(dict, open('pickle_output.pkl', 'wb'))

save_pkl()

def open_pkl(old_f):
	with open(old_f, 'rb') as f:
		data = pickle.load(f)
		print(data)

open_pkl("pickle_output.pkl")

# with 's' and interact locally
from sklearn import svm
from sklearn import datasets

def svm_iris():
	clf = svm.SVC()
	iris = datasets.load_iris()

	X,y = iris.data, iris.target
	clf.fit(X,y)

	s = pickle.dumps(clf)
	clf2 = pickle.loads(s)
	clf2.predict(X[0:1])
	print(y[0])

svm_iris()




