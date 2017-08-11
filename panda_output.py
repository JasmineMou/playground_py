import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

# basics of Series, DataFrame, Panel
def df_basics():
	'''
		https://pandas.pydata.org/pandas-docs/stable/indexing.html
		Object Type		Selection				Return Value Type
		Series			series[label]			scalar value
		DataFrame			frame[colname]			Series corresponding to colname
		Panel				panel[itemname]			DataFrame corresponding to the itemname
	'''
	dates = pd.date_range("1/1/2000", periods=8)
	df = pd.DataFrame(np.random.randn(8,4), index=dates, columns=["A", "B", "C", "D"])
	print(df)
	panel = pd.Panel({"one":df, "two":df-df.mean()})
	print(panel)
# df_basics()


# astype()
def np_astype():
	'''cast into different types'''
	x = np.array([1,2,2.5])
	y = x.astype(int)
	z = x.astype(str)
	print(x,y,z)
	# (array([ 1. ,  2. ,  2.5]), array([1, 2, 2]), array(['1.0', '2.0', '2.5'], dtype='|S32'))
# np_astype()


# linalg

def df_create():
	'''create DataFrame object'''
	# create empty df
	df0 = pd.DataFrame(np.nan, index=[0,1,2,3], columns=['A'], dtype="int") # dtype define the certain type for data frame, default to be "float"
	print(df0)


	# 2d
	data2d = np.array([['','Col1','Col2'],['Row1',1,2],['Row2',3,4]])
	# print(data2d)
	df1 = pd.DataFrame(data=data2d[1:,1:], index=data2d[1:,0], columns=data2d[0,1:])
	print(df1)


	# dict
	datadict = {1:[1,3], 2:[2,4], 3:[5,6]} # key:col, value:col_row_val
	df2 = pd.DataFrame(datadict)
	print(df2)


	# dict via zipped list
	keys = ['Country', 'Total'] 
	values = [['United States', 'Soviet Union', 'United Kingdom'], [1118, 473, 273]]
	zipped = list(zip(keys,values))
	# print(zipped)
	# [('Country', ['United States', 'Soviet Union', 'United Kingdom']), ('Total', [1118, 473, 273])]
	datadict2 = dict(zipped)
	df3 = pd.DataFrame(datadict2)
	print(df3)
	#           Country  Total
	# 0   United States   1118
	# 1    Soviet Union    473
	# 2  United Kingdom    273	


	# series
	dataseries = pd.Series({"Belgium":"Brussels", "India":"New Delhi", "United Kingdom":"London", "United States":"Washington"})
	df4 = pd.DataFrame(dataseries)
	print(df4)
# df_create()

def df_broadcast():
	'''broadcasting features of DataFrame'''
	cities = ['Manheim', 'Preston park', 'Biglerville', 'Indiana', 'Curwensville', 'Crown', 'Harveys lake', 'Mineral springs', 'Cassville', 'Hannastown', 'Saltsburg', 'Tunkhannock', 'Pittsburgh', 'Lemasters', 'Great bend']
	state = 'PA'
	d = {'state':state, 'city':cities}
	df = pd.DataFrame(d)
	# print(df)
	#                city state
	# 0           Manheim    PA
	# 1      Preston park    PA
	# 2       Biglerville    PA
	# 3           Indiana    PA
	# 4      Curwensville    PA
	# 5             Crown    PA
	# 6      Harveys lake    PA
	# 7   Mineral springs    PA
	# 8         Cassville    PA
	# 9        Hannastown    PA
	# 10        Saltsburg    PA
	# 11      Tunkhannock    PA
	# 12       Pittsburgh    PA
	# 13        Lemasters    PA
	# 14       Great bend    PA
# df_broadcast()


def df_import_export():
	'''import & export data'''
	filepath = "xxx.csv"
	col_names = ['col1', 'col2']
	dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S') # defines date_parser format
	data = pd.read_csv(filepath, header=None, comment='#', names=col_names, na_values={'sunspots':[' -1']}, index_col="date", parse_dates=[0,1,2], date_parser=dateparse) 
		# na_values need to be exactly the same as the NaN values in the data, including the unstripped space, etc.
		# header=3: skip the first 3 lines. 
		# index_col="date": to force the "date" column in the raw data to be the index.
		# parse_dates specifies which columns are of date format
		## can also combine multiple columns into 1 DateTime column as:
		## parse_dates={'datetime':['date','time']}
		# date_parser customizes the display format of dates

	data.to_csv('yyy.csv', index=False) # save without index
	data.to_csv('yyy.tsv', sep='\t')
	data.to_excel('yyy.xlsx')


def df_transform():
	'''transform & change data'''
	# needs to set inplace=True to apply changes to original dataframe

	df = pd.DataFrame({1:[1,3], 2:[2,4], 3:[5,6]}, index=['row0','row1'])
	print(df)
	#       1  2  3
	# row0  1  2  5
	# row1  3  4  6

	# log-scale
	np_vals_log10 = np.log10(df.values)
	df_log10 = np.log10(df)

	# reassign column names
	df.columns = ['col0', 'col1', 'col2']

	# add rows
	df.loc['added_row0'] = [7,8,9]
	df.loc['added_row1'] = [10,11,12]

	# add cols
	df['added_col0'] = df['col2'] + 1
	df['added_col1'] = pd.Series([0,9,5,3], index=df.index)
	print(df)
	#             col0  col1  col2  added_col0  added_col1
	# row0           1     2     5           6           0
	# row1           3     4     6           7           9
	# added_row0     7     8     9          10           5
	# added_row1    10    11    12          13           3

	# operations on indices
	## 1) change index
	# df.set_index(['col3'], inplace=True)
	# print(df)
	#       col1  col2  added_col0  added_col1
	# col3                                    
	# 5        1     2           6           0
	# 6        3     4           7           9
	# 9        7     8          10           5

	## 2) delete indices, rows, cols
	df.drop('col1', axis=1, inplace=True) # axis = 1, drop column
	df.drop('row0', axis=0, inplace=True) # axis = 0, drop row
	print(df)
	#             col0  col2  added_col0  added_col1
	# row1           3     6           7           9
	# added_row0     7     9          10           5
	# added_row1    10    12          13           3

	df.drop(df.columns[[0]], axis=1, inplace=True)
	print(df)
	#             col2  added_col0  added_col1
	# row1           6           7           9
	# added_row0     9          10           5
	# added_row1    12          13           3

	df.drop(df.index[0], inplace=True) # drop the index at position 1
	print(df)
	#             col2  added_col0  added_col1
	# added_row0     9          10           5
	# added_row1    12          13           3

	## i) reset index, keep the index
	df.reset_index(inplace=True)
	print(df)
	#         index  col2  added_col0  added_col1
	# 0  added_row0     9          10           5
	# 1  added_row1    12          13           3

	## ii) reset index, index removed
	# df.reset_index(drop=True, inplace=True)
	# print(df)
	#    col2  added_col0  added_col1
	# 0  	9          10           5
	# 1  	12         13           3

	# drop duplicate, 'keep' argument specifies which of the duplicates to keep
	df.loc[2] = df.loc[1]
	print(df)
	#         index  col2  added_col0  added_col1
	# 0  added_row0     9          10           5
	# 1  added_row1    12          13           3
	# 2  added_row1    12          13           3
	print(df.duplicated())
	# 0    False
	# 1    False
	# 2     True

	## i) without keep
	# df.drop_duplicates(subset='index', inplace=True)
	# print(df)
	#         index  col2  added_col0  added_col1
	# 0  added_row0     9          10           5
	# 1  added_row1    12          13           3

	## ii) with keep
	df.drop_duplicates(subset='index', inplace=True, keep='last')
	print(df)
	#         index  col2  added_col0  added_col1
	# 0  added_row0     9          10           5
	# 2  added_row1    12          13           3

	# rename index/cols
	new_indices = {0:'new_index0', 2:'new_index1'}
	new_cols = {'index':'new_col0', 'col2':'new_col1', 'added_col0':'new_col2', 'added_col1':'new_col3'}
	df.rename(index=new_indices, columns=new_cols, inplace=True)
	print(df)
	#               new_col0  new_col1  new_col2  new_col3
	# new_index0  added_row0         9        10         5
	# new_index1  added_row1        12        13         3

	# apply functions
	# replace values
	df.replace(['added_row0', 'added_row1'], [0,-1], inplace=True)
	print(df)
	#             new_col0  new_col1  new_col2  new_col3
	# new_index0         0         9        10         5
	# new_index1        -1        12        13         3

	# lambda function with apply(), which only applies lambda function along the axis of DataFrame -- either row or column but not element-wise.
	doubler = lambda x:x*2
	# df['new_index1'] = df['new_col1'].apply(doubler)
	# print(df)
	#             new_col0  new_col1  new_col2  new_col3
	# new_index0         0        18        10         5
	# new_index1        -1        24        13         3

	# lambda funciton with applymap(), which applies lambda function element-wise
	df = df.applymap(doubler)
	print(df)
	#             new_col0  new_col1  new_col2  new_col3
	# new_index0         0        18        20        10
	# new_index1        -2        24        26         6
# df_transform()


def df_replace():
	'''replace(), map() function'''
	df = pd.DataFrame([[1,2,'+3b'],[4,5,'-6B'],[7,8,'+9A']], columns=['class','test','result'])
	print(df)
	#    class  test result
	# 0      1     2    +3b
	# 1      4     5    -6B
	# 2      7     8    +9A

	# replace values, see "apply functions" ~ "replace values" in df_transform()
	# replace values, apply regex
	df['result'] = df['result'].map(lambda x:x.lstrip('+-').rstrip('aAbBcC'))
	print(df)
	#    class  test result
	# 0      1     2      3
	# 1      4     5      6
	# 2      7     8      9
# df_replace()

def df_split_join():
	'''use str.split(), stack() to split, and join() to join'''
	df = pd.DataFrame([[34,0,'23:44:55'], [22,0,'66:77:88'], [19,1,'43:68:05 56:34:12']], columns=['Age','PlusOne','Ticket'])
	# print(df)
	#    Age  PlusOne             Ticket
	# 0   34        0           23:44:55
	# 1   22        0           66:77:88
	# 2   19        1  43:68:05 56:34:12

	ticket_series = df['Ticket'].str.split(' ').apply(pd.Series,1).stack()
	ticket_series.index = ticket_series.index.droplevel(-1)
	# print(ticket_series.index)
	# Int64Index([0, 1, 2, 2], dtype='int64')
	ticketdf = pd.DataFrame(ticket_series)
	# print(ticketdf)
	#           0
	# 0  23:44:55
	# 1  66:77:88
	# 2  43:68:05
	# 2  56:34:12

	del df['Ticket']
	df_cleaned = df.join(ticketdf) # Join columns with other DataFrame either on index or on a key column
	# print(df_cleaned)
	#    Age  PlusOne         0
	# 0   34        0  23:44:55
	# 1   22        0  66:77:88
	# 2   19        1  43:68:05
	# 2   19        1  56:34:12
# df_split_join()

def df_reshape():
	'''pivot, stack, unstack, melt'''
	'''references: 
		http://pandas.pydata.org/pandas-docs/stable/reshaping.html
		http://nikgrozev.com/2015/07/01/reshaping-in-pandas-pivot-pivot-table-stack-and-unstack-explained-with-pictures/
	'''
	products = pd.DataFrame({'category': ['Cleaning', 'Cleaning', 'Entertainment', 'Entertainment', 'Tech', 'Tech'],'store': ['Walmart', 'Dia','Walmart', 'Fnac', 'Dia','Walmart'],'price':[11.42, 23.50, 19.99, 15.95, 55.75, 111.55],'testscore': [4, 3, 5, 7, 5, 8]})
	# print(products)
	#         category   price    store  testscore
	# 0       Cleaning   11.42  Walmart          4
	# 1       Cleaning   23.50      Dia          3
	# 3  Entertainment   19.99  Walmart          5
	# 4  Entertainment   15.95     Fnac          7
	# 5           Tech   55.75      Dia          5
	# 6           Tech  111.55  Walmart          8

	# pivot()
	pivot_products0 = products.pivot(index='category', columns='store', values='price')
	# values: specify which values to display in pivot table 
	# columns: specify which variables to display in columns
	# index: specify which variable to become the index

	# print(pivot_products0)
	# store            Dia   Fnac  Walmart
	# category                            
	# Cleaning       23.50    NaN    11.42
	# Entertainment    NaN  15.95    19.99
	# Tech           55.75    NaN   111.55

	pivot_products1 = products.pivot(index='category', columns='store')
	# print(pivot_products1)
	#                price                testscore             
	# store            Dia   Fnac Walmart       Dia Fnac Walmart
	# category                                                  
	# Cleaning       23.50    NaN   11.42       3.0  NaN     4.0
	# Entertainment    NaN  15.95   19.99       NaN  7.0     5.0
	# Tech           55.75    NaN  111.55       5.0  NaN     8.0

	# pivot_table(), used when index contains duplicate entries
	# add one more Dia-Cleaning entry in products2 compared to products1
	products2 = pd.DataFrame({'category': ['Cleaning', 'Cleaning', 'Cleaning', 'Entertainment', 'Entertainment', 'Tech', 'Tech'],'store': ['Walmart', 'Dia', 'Dia', 'Walmart', 'Fnac', 'Dia','Walmart'],'price':[11.42, 23.50, 40.00, 19.99, 15.95, 55.75, 111.55],'testscore': [4, 3, 6, 5, 7, 5, 8]}) 
	# print(products2)
	#         category   price    store  testscore
	# 0       Cleaning   11.42  Walmart          4
	# 1       Cleaning   23.50      Dia          3
	# 2       Cleaning   40.00      Dia          6
	# 3  Entertainment   19.99  Walmart          5
	# 4  Entertainment   15.95     Fnac          7
	# 5           Tech   55.75      Dia          5

	pivot_products2 = products2.pivot_table(index='category', columns='store', values='price', aggfunc='mean') # notice the Dia-Cleaning value looks dft from pivot_products1
	# print(pivot_products2)
	# # store            Dia   Fnac  Walmart
	# # category                            
	# # Cleaning       31.75    NaN    11.42
	# # Entertainment    NaN  15.95    19.99
	# # Tech           55.75    NaN   111.55

	# melt()
	people = pd.DataFrame({'FirstName' : ['John', 'Jane'],'LastName' : ['Doe', 'Austen'],'BloodType' : ['A-', 'B+'],'Weight' : [90, 64]})
	# print(people)
	#   BloodType FirstName LastName  Weight
	# 0        A-      John      Doe      90
	# 1        B+      Jane   Austen      64

	melt_people = pd.melt(people, id_vars=['FirstName','LastName'], var_name='measurements')
	print(melt_people)
	#   FirstName LastName measurements value
	# 0      John      Doe    BloodType    A-
	# 1      Jane   Austen    BloodType    B+
	# 2      John      Doe       Weight    90
	# 3      Jane   Austen       Weight    64

	# Multiple Index
	row_idx = pd.MultiIndex.from_tuples(list(zip(['r0','r0'],['r-00','r-01'])))
	col_idx = pd.MultiIndex.from_tuples(list(zip(['c0', 'c0', 'c1'], ['c-00', 'c-01', 'c-10'])))
	df = pd.DataFrame(np.arange(6).reshape(2,3), index=row_idx, columns=col_idx).applymap(lambda x: (x//3, x%3))
	print("Original: ")
	print(df)

	# stack()
	s = df.stack()
	print("Stack: ")
	print(s)

	# unstack()
	print("Unstack: ")
	u = df.unstack()
	print(u)

# df_reshape()

def df_iter():
	'''Iteration over rows'''
	df = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['A', 'B', 'C'])
	for index, row in df.iterrows():
		print(row['A'], row['B'])
# df_iter()


def df_check_info():
	'''check information'''
	df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7,8,9], [11,12,13]]), index=(2,1,'A',4))
	df.iloc[0,0] = None 
	df.columns = ['col1', 'col2', 'col3']
	print(df)

	# summary 
	# print(df.info())
	# print(df.columns.values)

	# head, tail
	# print(df.head(3))
	# print(df.tail(3))

	# size
	# print(df.shape)
	# print(len(df.index)) # get the height/# of rows
	# print(df['col1'].count()) # will exclude NaN option

	# indexing
	# print(df.iloc[1][0]) 		#i-: only accept input of index position
	# print(df.loc[1]['col1'])    # accept both index label and position
	# print(df.iat[1,0])			#i-: only accept input of index position
	# print(df.at[1,'col1'])		# only accept index label
	# print(df.get_value(1,'col1')) # only accept input of index label

	# indexing rows/cols
	# print(df.iloc[0])			# row 0
	# print(df.loc[:,'col1'])		# col A

	# comparison of loc, iloc, ix
	print(df.loc[2])			# row labeled 2
	print(df.iloc[2])			# 3rd row
	print(df.ix[2])				# 3rd row, ix takes index label when index is integer-based, and takes position when it's not integer-based (not just contains integer).

	# format
	# print(type(df.values), type(df))
	# <class 'numpy.ndarray'>, <class 'pandas.core.frame.DataFrame'> 
# df_check_info()



def df_plot():
	'''plot'''
	# suppose "appl" data exists

	close_arr = appl['close'].values # numpy.ndarry
	plt.plot(close_arr)


	close_series = appl['close'] # pandas.core.series.Series
	# option 1
	plt.plot(close_series) # similar plot but nicer x axis
	# option 2
	close_series.plot() # "date" & legend are appended to the x axis


	# plot all the series on the same pic with legends
	appl.plot() 
	plt.plot(appl) # use the matplotlib, use the dataframe as the args
	plt.yscale("log") # logarithmic scale on vertical axis

	# break each serie into different plot
	appl.plot(subplots=True)

	# plot only appointed series
	cols = ['col1','col2']
	appl[cols].plot()


	# customizing plots
	appl['open'].plot(color='b', style='.-', legend=True)
	appl['close'].plot(color='r', style='.', legend=True)
	plt.title("APPL's stock")
	plt.xlabel('x label')
	plt.ylabel('y label')
	plt.axis('2001','2002',0,100) # zoom the axis to xrange 2001~2002, with vertical scale 0~100.


	# save plots
	appl.loc['2001':'2004', ['open','close','high','low']].plot()
	plt.savefig('appl.png')
	plt.savefig('appl.jpg')
	plt.savefig('appl.pdf')

	plt.show()

def df_gt():
	df1 = pd.DataFrame({'A':[50,-50], 'B':[-20,-20],'C':[-1,1]})
	print(df1)
	df2 = df1.gt(0)
	print(df2)
	print(df2.sum()>0)
# df_gt()

def df_dot():
	'''dot product of data frame and array'''
	df = pd.DataFrame({'A': [1., 1., 1., 2., 2., 2.], 'B': np.arange(1., 7.)})
	v2 = np.array([2,3])
	df2 = df.dot(v2)
	print(df)
	print(v2)
	print(df2)
# df_dot()

def rename():
	# change series.name
	print("Series' rename")
	s = pd.Series([1, 2, 3])
	print(s)
	s.rename('my_name', inplace=True)
	print(s)

	# change serie's label
	s.rename(lambda x: x ** 2, inplace=True)
	print(s)
	s.rename({1:3,2:5}, inplace=True)
	print(s)

	# change dataframe's cols
	print("DataFrame's rename")
	df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
	print(df)
	df.rename(index=str, columns={"A":"a", "B":"b"}, inplace=True)
	print(df)
# rename()

def df_locate():
	'''
		Locate the rows with index location number.
		Select rows whose column value satisfy conditions.
		https://stackoverflow.com/questions/17071871/select-rows-from-a-dataframe-based-on-values-in-a-column-in-pandas
	'''
	df = pd.DataFrame({'A': [1., 1., 1., 2., 2., 2.], 'B': np.arange(1., 7.), 'C': [8,9,10,9,11,12]})
	df["A"].iat[2] = 10
	print(df)
	print()



	row_n = df.shape[0]
	t = 3
	interval = 1
	indexes = df.loc[df["C"]==9].index
	l = []
	for index in indexes:
		print(type(index), index)
		ll = list(range(index-t*interval, index+(t+1)*interval, interval))
		l.extend(ll)
	l = set(l)
	l = list(filter(lambda x: x>=0 and x<row_n, l))

	print(l)

	#### get the dims
	# ## get number of rows
	# print(len(df.index))
	# print(df.shape[0]) 	# <- faster

	# ## get number of cols
	# print(df.shape[1])


	#### BY INTEGER INDEX, ix(), iloc()
	# ## get the first row
	# print(df.ix[2])
	# print(df.iloc[2])
	# # A     1.0
	# # B     3.0
	# # C    10.0
	# # Name: 2, dtype: float64

	# print(df.ix[[2]])	# <- the result is neater.
	# print(df.iloc[[2]])
	# #      A    B   C
	# # 2  1.0  3.0  10

	# ## get the last row
	# print(df.iloc[[-1]])

	# ## get the specific column value, with integer index.
	# ## df.iloc[2, "B"] doesn't work
	# print(df.ix[2, "B"])
	# print(df["B"].iloc[2])
	# print(df["B"].iat[2]) # <- faster


	# ## get the specific column value in last row, with integer index.
	# ## df.ix[-1, "B"] doesn't work. thus change to select the column first, then get the value by selecting row from that column.
	# print(df["B"].iat[-1])


	#### BY LABEL, loc()
	# ### column value equals a scalar
	# ## get the whole row
	# print(df.loc[df['A']==2])
	# print(df.loc[df['A']!=2])	# not equal
	# print()

	# ## get the specific column values, with labeled index, which type is <class 'numpy.ndarray'>
	# print(df.loc[df['A']==2, "B"].values)
	# print(df.loc[df['A']==2, "B"].values[0])	
	# print()

	# ## get the index
	# print(df.loc[df['A']==2].index)
	# print(df.loc[df['A']==2].index[0])
	# print()

	# ### column value in an interable
	# print(df.loc[df['A'].isin(range(-1,2))])
	# print(df.loc[~df['A'].isin(range(-1,2))])	# not in
	# print(df.loc[df['A'].isin(range(-1,2)), "B"].values)
	# print(df.loc[df['A'].isin(range(-1,2)), "B"].index)
	# print()

	# ### column values satisfy multiple conditions
	# print(df.loc[(df['A'] == 2) & (df['C'].isin(range(9,14)))])
	# print(df.loc[(df['A'] == 2) & (df['C'].isin(range(9,14))), "B"])
	# print(df.loc[(df['A'] == 2) & (df['C'].isin(range(9,14))), "B"].values)
	# print(df.loc[(df['A'] == 2) & (df['C'].isin(range(9,14))), "B"].index)
	# print()	
df_locate()

def df_combine():
	'''
		Multiple ways to combine dataframes.
		pd.concat(): https://pandas.pydata.org/pandas-docs/stable/merging.html#concatenating-objects
		pd.append(): https://pandas.pydata.org/pandas-docs/stable/merging.html#concatenating-using-append
		pd.merge(): https://pandas.pydata.org/pandas-docs/stable/merging.html#database-style-dataframe-joining-merging
	'''
	pass
# df_combine()



























