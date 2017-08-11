# reference from: http://machinelearningmastery.com/difference-time-series-dataset-python/

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
# from pandas.tseries.offsets import * 

def parser(x):
	return pd.datetime.strptime('190'+x, '%Y-%m')

# test with shampoo-sales.csv
series = pd.read_csv('shampoo-sales.csv', header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
print(series)
print(len(series))
print(type(series))


def dfc_manual(dataset, interval=1):
	'''interval = lag'''
	diff = list()
	for i in range(interval, len(dataset)):
		value = dataset[i] - dataset[i-interval]
		diff.append(value)
	return pd.Series(diff)


def dfc_test():
	# diff = dfc_manual(series.values)
	diff = series.diff() 	# built-in diff() library

	plt.plot(diff)
	plt.show()

	window = 6
	s = pd.Series.diff(series[::window])/window # the slope over each window

	print(s)
	plt.plot(s)
	plt.show()
dfc_test()

def offset_output():
	d = pd.datetime(2017, 6, 19, 3, 4)
	offset = BMonthEnd()
	print(d, offset.rollforward(d), offset.rollback(d))
# offset_output()


# reference from: https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.rolling.html
def rolling_output():
	'''smoothing method'''

	## rolling vs resampling: 
	### both are window operations: rolling is time-based, resampling is frequency-based. 
	### https://pandas.pydata.org/pandas-docs/stable/computation.html#time-aware-rolling-vs-resampling

	## available tuning parameters
	### window: 1) size of the moving window -- the # of observations used for calculating the statistic; each window will be a fixed size, int. 2) offset -- the time period of each window; each window will have a variable sized based on the observations included in the time-period, only valid for datetimelike indexes, offset. 

	### min_periods: minimum # of observations in window required to have a value, int, default 1. 
	### center: set the labels at the center of the window, boolean, default False (right edge of the window).
	### win_type: window type, string, default None.  
	### on: for a DataFrame, choose which column to calculate the rolling window on rather than the index, string.
	### closed: interval closure option, options: 'right', 'left', 'both', 'neither; default to 'right'.
	### axis: int or string, default 0 (row)

	sr0 = series
	plt.plot(sr0, label="raw")

	# 1) compare pd.Series.rolling(data).apply(func), pd.rolling_apply(data, func), data.rolling(win_type).func() methods: 
	## the results vizs are the same given the functions the same; 
	## there are limited func() in data.rolling(win_type).func() but more choices in win_type; ## pd.rolling_apply() will be deprecated in future; 
	## func can be customized as a lambda expression. 
	## Thus recommend using pd.Series.rolling(data).apply(func) and data.rolling(win_type).func() when having specific requirements in win_type. 
	# note: there is no func() called median for Windows object.

	# compare centered vs not centered: there is a left shift for the centered from the not centered one.
	
	sr1 = pd.Series.rolling(sr0, window=4, center=True).apply(func=np.mean)
	plt.plot(sr1, label="series_rolling_apply_mean", linestyle='-.')

	# sr10 = pd.rolling_apply(sr0, window=4, func=np.mean)
	# plt.plot(sr10, label="rolling_apply_mean_not_centered", linestyle='-.')

	sr11 = sr0.rolling(window=4, center=True).mean()
	plt.plot(sr11, label="rolling_mean", linestyle=':')

	# sr12 = sr0.rolling(window=4).mean()
	# plt.plot(sr12, label="rolling_mean_not_centered", linestyle=':')

	sr13 = sr0.rolling(window=4, center=True).median()
	plt.plot(sr13, label="rolling_median", linestyle=':')

	sr14 = sr0.rolling('60d').mean()
	plt.plot(sr14, label="rolling_mean_by_time_units_60days", linestyle=':')


	# 2) compare different window_type for the data.rolling(win_type).func() function.
	# win_type_paras = ['triang', 'boxcar', 'blackman']
	# rollings2 = [sr0.rolling(window=4, win_type=p, center=True).mean() for p in win_type_paras]
	# for r,p in zip(rollings2, win_type_paras):
	# 	plt.plot(r, label="rolling_mean_{}".format(p), linestyle='--')

	# sr21 = sr0.rolling(window=4, win_type='gaussian', center=True).mean(std=0.5)
	# plt.plot(sr21, label="rolling_mean_gaussian", linestyle='--')

	# sr22 = sr0.rolling(window=4, win_type='general_gaussian', center=True).mean(power=1, std=0.5, width=2)
	# plt.plot(sr22, label="rolling_mean_general_gaussian_p1_std050", linestyle='--')

	# sr23 = sr0.rolling(window=4, win_type='general_gaussian', center=True).mean(power=2, std=0.5, width=2)
	# plt.plot(sr23, label="rolling_mean_general_gaussian_p2_std050", linestyle='--')

	# sr24 = sr0.rolling(window=4, win_type='general_gaussian', center=True).mean(power=2, std=0.05, width=2)
	# plt.plot(sr24, label="rolling_mean_general_gaussian_p2_std005", linestyle='--')

	# sr25 = sr0.rolling(window=4, win_type='general_gaussian', center=True).mean(power=0.05, std=0.5, width=2)
	# plt.plot(sr25, label="rolling_mean_general_gaussian_p005_std05", linestyle='--')


	# 3) compare different window sizes
	## cmap = matplotlib.cm.autumn
	# cmap = matplotlib.cm.get_cmap('autumn_r') # trick: reverse the colormap color
	# norm = matplotlib.colors.Normalize(vmin=0, vmax=10)
	# windows = [1,3,5,7,9]
	# rollings3 = [pd.Series.rolling(sr0, window=i, center=True).apply(func=np.mean) for i in windows]
	# for r,w in zip(rollings3, windows):
	# 	plt.plot(r, label="series_rolling_apply_mean_win{}".format(w), linestyle=':', color=cmap(norm(w)))

	plt.legend()
	plt.show()
# rolling_output()

def weighted_output():
	'''
		2 ways of doing it: data.groupby.apply(), data.groupby.agg(); np.average(data, weights)
		reference: http://pbpython.com/weighted-average.html
				   https://docs.scipy.org/doc/numpy-1.12.0/reference/generated/numpy.average.html
	'''
	# load the data
	sales = pd.read_excel("sales-estimate.xlsx")
	print(sales.head())

	# # 1) data.groupby.apply()
	# ## normal mean
	# mean = sales.groupby("Manager")["Current_Price"].mean()
	# print(mean)

	# ## weighted mean
	# def wavg(group, avg_name, weight_name):
	# 	data = group[avg_name]
	# 	weight = group[weight_name]
	# 	try:
	# 		return (data*weight).sum()/weight.sum()
	# 	except ZeroDivisionError:
	# 		return data.mean()
	# mean_weighted_groupby = sales.groupby("Manager").apply(wavg, "Current_Price", "Quantity")
	# print(mean_weighted_groupby)

	# ## weighted_mean multiple criteria
	# mean_weighted_mul = sales.groupby(["Manager", "State"]).apply(wavg, "Current_Price", "Quantity")
	# print(mean_weighted_mul)

	# ## multiple aggregations - different measures for different columns, yet the measures are limited to what functions have. 
	# m = {'New_Product_Price':['mean'], 'Current_Price':['median'], 'Quantity':['sum', 'mean']}
	# mean_mul_agg = sales.groupby(["Manager","State"]).agg(m)
	# print(mean_mul_agg)

	# ## to customize multiple aggregations, so far can only combine results by hard-coding
	# mean_new_product_price = sales.groupby("Manager").apply(wavg, "New_Product_Price", "Quantity")
	# mean_current_price = sales.groupby("Manager").apply(wavg, "Current_Price", "Quantity")
	# mean_manual_agg = pd.DataFrame(data=dict(c1=mean_new_product_price, c2=mean_current_price))
	# mean_manual_agg.columns = ["New_Product_Price", "Current_Price"]
	# print(mean_manual_agg.head())

	# 2) use np.average(data, weights)
	## weighted mean without group
	mean_weighted_np = np.average(sales["Current_Price"], weights=sales["Quantity"])
	print(mean_weighted_np)

	## weighted mean with group
	mean_weighted_np_grouped = sales.groupby("Manager").apply(lambda x: np.average(x['New_Product_Price'], weights=x['Quantity']))
	print(mean_weighted_np_grouped) 

# weighted_output()

def reindex_output():
	'''
		np.reindex() method
		reference: https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.reindex.html
	'''
	# fill in the missing value with specific value
	# index0 = ['Firefox', 'Chrome', 'Safari', 'IE10', 'Konqueror']
	# df0 = pd.DataFrame({'http_status':[200,200,404,404,301], 'response_time':[0.04, 0.02, np.NaN, 0.08, 1.0]}, index=index0)
	# index1 = ['Safari', 'Iceweasel', 'Comodo Dragon', 'IE10', 'Chrome']
	# df11 = df0.reindex(index1)
	# df12 = df0.reindex(index1, fill_value='missing')	# note if the previously existing value is np.NaN, fill_value method will not change the result.
	# print(df0)
	# print(df11)
	# print(df12)

	# fill in the missing value with estimated value, only for monotonically increasing/decreasing index. Note: regardless whether the old index appears in the new reindexed series, the old values always affect the filling value in the reindexed series. 
	date_index0 = pd.date_range('5/22/2017', periods=12, freq='7D')
	df3 = pd.DataFrame({"prices":range(6)+[np.NaN, np.NaN]+range(8,12)}, index=date_index0)
	print(df3)
	#             prices
	# 2017-05-22     0.0
	# 2017-05-29     1.0
	# 2017-06-05     2.0
	# 2017-06-12     3.0
	# 2017-06-19     4.0
	# 2017-06-26     5.0
	# 2017-07-03     NaN
	# 2017-07-10     NaN
	# 2017-07-17     8.0
	# 2017-07-24     9.0
	# 2017-07-31    10.0
	# 2017-08-07    11.0

	date_index1 = pd.date_range('6/22/2017', periods=19, freq='2D')
	df40 = df3.reindex(date_index1) # note it will only include what the new index covers.
	print(df40)
	# 2017-06-22     NaN
	# 2017-06-24     NaN
	# 2017-06-26     5.0	<- original
	# 2017-06-28     NaN
	# 2017-06-30     NaN
	# 2017-07-02     NaN
	# 2017-07-04     NaN
	# 2017-07-06     NaN
	# 2017-07-08     NaN
	# 2017-07-10     NaN	<- original
	# 2017-07-12     NaN
	# 2017-07-14     NaN
	# 2017-07-16     NaN
	# 2017-07-18     NaN
	# 2017-07-20     NaN
	# 2017-07-22     NaN
	# 2017-07-24     9.0	<- original
	# 2017-07-26     NaN
	# 2017-07-28     NaN

	df41 = df3.reindex(date_index1, method='bfill') # 'bfill' means use the next valid observation to fill gap
	print("backfill/bfill")
	print(df41)
	#             prices
	# 2017-06-22     5.0
	# 2017-06-24     5.0
	# 2017-06-26     5.0	<- original
	# 2017-06-28     NaN
	# 2017-06-30     NaN
	# 2017-07-02     NaN
	# 2017-07-04     NaN
	# 2017-07-06     NaN
	# 2017-07-08     NaN
	# 2017-07-10     NaN	<- original
	# 2017-07-12     8.0
	# 2017-07-14     8.0
	# 2017-07-16     8.0
	# 2017-07-18     9.0
	# 2017-07-20     9.0
	# 2017-07-22     9.0
	# 2017-07-24     9.0	<- original
	# 2017-07-26    10.0
	# 2017-07-28    10.0


	df42 = df3.reindex(date_index1, method='ffill') # 'ffill' means propagate last valid observation forward to next valid
	print("pad/ffill")
	print(df42)
	#             prices
	# 2017-06-22     4.0
	# 2017-06-24     4.0
	# 2017-06-26     5.0	<- original
	# 2017-06-28     5.0
	# 2017-06-30     5.0
	# 2017-07-02     5.0
	# 2017-07-04     NaN
	# 2017-07-06     NaN
	# 2017-07-08     NaN
	# 2017-07-10     NaN	<- original
	# 2017-07-12     NaN
	# 2017-07-14     NaN
	# 2017-07-16     NaN
	# 2017-07-18     8.0
	# 2017-07-20     8.0
	# 2017-07-22     8.0
	# 2017-07-24     9.0	<- original
	# 2017-07-26     9.0
	# 2017-07-28     9.0

	df43 = df3.reindex(date_index1, method='nearest') # 'nearest' means use the nearest valid observation
	print("nearest")
	print(df43)
	#             prices
	# 2017-06-22     4.0
	# 2017-06-24     5.0
	# 2017-06-26     5.0	<- original
	# 2017-06-28     5.0
	# 2017-06-30     NaN
	# 2017-07-02     NaN
	# 2017-07-04     NaN
	# 2017-07-06     NaN
	# 2017-07-08     NaN
	# 2017-07-10     NaN	<- original
	# 2017-07-12     NaN
	# 2017-07-14     8.0
	# 2017-07-16     8.0
	# 2017-07-18     8.0
	# 2017-07-20     8.0
	# 2017-07-22     9.0
	# 2017-07-24     9.0	<- original
	# 2017-07-26     9.0
	# 2017-07-28    10.0

# reindex_output()



