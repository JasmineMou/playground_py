import pandas as pd
import numpy as np

def series_map():
	'''
		https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.map.html
	'''
	x = pd.Series([1,2,3], index=['one', 'two', 'three'])
	y = pd.Series(['foo', 'bar', 'baz'], index=[1,2,3])
	z = x.map(y)

	a = {1: 'A', 2: 'B', 3: 'C'}
	b = x.map(a)

	## method 1
	result1 = pd.concat((x.rename('x'),y.rename('y'), z.rename('z'), b.rename('b')), axis=1)
	print(result1)

	## method 2
	# method2 = pd.concat((x,y,z,b), axis=1).rename(columns={0:'x', 1:'y', 2:'z', 3:'b'}, inplace=True)
	# print(method2)

	## na_action: control whether NA values are affected by the mapping function.
	s = pd.Series([1,2,3,np.nan])
	s2 = s.map('this is a string {}'.format, na_action=None)
	s3 = s.map('this is a string {}'.format, na_action='ignore')
	print(pd.concat((s,s2,s3), axis=1).rename(columns={0:'original',1:'naaction_None', 2:'naaction_ignore'}))


series_map()