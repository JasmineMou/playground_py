import numpy as np
import pandas as pd 
from pandas_datareader.data import DataReader
import statsmodels.api as sm 
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

def use_ols():
	dat = sm.datasets.get_rdataset("Guerry", "HistData").data
	# print(dat)

	results = smf.ols("Lottery ~ Literacy + np.log(Pop1831)", data=dat).fit()
	# print(results.summary())
# use_ols()

def tsa_unemployment():
	'''
		http://www.statsmodels.org/stable/examples/notebooks/generated/statespace_cycles.html
	'''
	endog = DataReader("UNRATE", "fred", start="1954-01-01")
	print(endog)

	hp_cycle, hp_trend = sm.tsa.filters.hpfilter(endog, lamb=129600)
	print(hp_cycle, hp_trend)

	## Unobserved components and ARIMA model (UC-ARIMA)
	mod_ucarima = sm.tsa.UnobservedComponents(endog, 'rwalk', autoregressive=4)
	# Here the powell method is used, since it achieves a
	# higher loglikelihood than the default L-BFGS method
	res_ucarima = mod_ucarima.fit(method="powell", disp=False)
	print(res_ucarima.summary())

	## Unobserved components with stochastic cycle (UC)
	mod_uc = sm.tsa.UnobservedComponents(endog, 'rwalk', cycle=True, stochastic_cycle=True, damped_cycle=True,)
	# Here the powell method gets close to the optimum
	res_uc = mod_uc.fit(method='powell', disp=False)
	# but to get to the highest loglikelihood we do a
	# second round using the L-BFGS method.
	res_uc = mod_uc.fit(res_uc.params, disp=False)
	print(res_uc.summary())

	fig, axes = plt.subplots(2,figsize=(13,5))
	axes[0].set(title='Level/trend component')
	axes[0].plot(endog.index, res_uc.level.smoothed, label='UC')
	axes[0].plot(endog.index, res_ucarima.level.smoothed, label='UC-ARIMA(2,0)')
	axes[0].plot(hp_trend, label='HP Filter')
	axes[0].legend(loc='upper left')
	axes[0].grid()

	axes[1].set(title='Cycle component')
	axes[1].plot(endog.index, res_uc.cycle.smoothed, label='UC')
	axes[1].plot(endog.index, res_ucarima.autoregressive.smoothed, label='UC-ARIMA(2,0)')
	axes[1].plot(hp_cycle, label='HP Filter')
	axes[1].legend(loc='upper left')
	axes[1].grid()

	fig.tight_layout()

	plt.show()
	plt.close()

tsa_unemployment()

def check_methods_in_module():
	'''
		https://stackoverflow.com/questions/139180/listing-all-functions-in-a-python-module
		Example used here is to find out the content of statsmodels.api.tsa.filters.hpfilter().
	'''

	## list all methods of a module after importing
	print(dir(sm))
	# ['GEE', 'GLM', 'GLS', 'GLSAR', 'Logit', 'MNLogit', 'MixedLM', 'NegativeBinomial', 'NominalGEE', 'OLS', 'OrdinalGEE', 'PHReg', 'Poisson', 'ProbPlot', 'Probit', 'QuantReg', 'RLM', 'WLS', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add_constant', 'categorical', 'cov_struct', 'datasets', 'distributions', 'emplike', 'families', 'formula', 'genmod', 'graphics', 'iolib', 'load', 'nonparametric', 'qqline', 'qqplot', 'qqplot_2samples', 'regression', 'robust', 'show_versions', 'stats', 'test', 'tools', 'tsa', 'version', 'webdoc']

	## list module and find the file location.
	print(sm.__dict__.get("tsa"))
	# <module 'statsmodels.tsa.api' from '/anaconda/lib/python3.6/site-packages/statsmodels/tsa/api.py'>

	# then in terminal: 
	# > open /anaconda/lib/python3.6/site-packages/statsmodels/tsa/api.py
	# find this line "from .filters import api as filters"
	# > open /anaconda/lib/python3.6/site-packages/statsmodels/tsa/filters/api.py
	# find this line "from .hp_filter import hpfilter"
	# > open /anaconda/lib/python3.6/site-packages/statsmodels/tsa/filters/hp_filter.py

