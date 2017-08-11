import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

## simulate data
np.random.seed(1234)
df = pd.DataFrame({'px_last':100+np.random.randn(1000).cumsum()}, index=pd.date_range('2010-01-01', periods=1000, freq='B'))
df['50dma'] = df['px_last'].rolling(window=50,center=False).mean()
df['200dma'] = df['px_last'].rolling(window=200,center=False).mean()

df['label'] = np.where(df['50dma'] > df['200dma'], 1, -1)
#x#x# df['label'] = np.where(df['50dma'] > df['200dma'], True, False) # <- only 1,-1 work well 


## plot
df = df.dropna(axis=0, how='any')
fig,ax = plt.subplots()

def plot_func(group):
	print(group)

	# color = 'r' if (group.label<0).all() else 'g'
	color = 'r' if (group.label==False).all() else 'g'

	ax.plot(group.index, group.px_last, c=color, linewidth=2)

## Look into results
# df['shift'] = df['label'].shift()
# df['shift_label'] = df['label'].shift() * df['label']<0 # only get True when switch happens & the condition "50dma > 200dma" doesn't stand. 
# df['shift_label_cumsum'] = (df['label'].shift() * df['label']<0).cumsum() # cumsum only increments when "shift_label" is True, as False==0.
# df.groupby(df['shift_label_cumsum']).apply(plot_func)

## apply groupby methods
df.groupby((df.label.shift() * df.label<0).cumsum()).apply(plot_func)
#x#x# df.groupby((df.label.shift() * df.label==False).cumsum()).apply(plot_func) # <- only 1,-1 work well 

ax.plot(df.index, df['50dma'], 'k--', label='MA-50')
ax.plot(df.index, df['200dma'], 'b--', label='MA-200')
ax.legend(loc='best')

print(df.to_string())

plt.show()
plt.close()