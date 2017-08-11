import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.widgets as mwidgets

def line_span():
	# draw a sin/cos line
	t = np.arange(-1,2,.01)
	s = np.sin(2*np.pi*t)
	plt.plot(t,s)

	# draw a red horizontal line of default location at y = 0 that spans xrange
	l = plt.axhline(linewidth=8,color='red')

	# draw a vertical line of default color at x = 1 that spans yrange
	l = plt.axvline(x=1, color='green')

	# draw a vertical line with min y. 
	l = plt.axvline(x=0, ymin=0.75, linewidth=8, color='blue')

	# draw a horizontal span with transparency degree 0.9
	p = plt.axhspan(0.25, 0.75, facecolor='0.5', alpha=0.9)

	# draw a vertical span
	p = plt.axvspan(1.25, 1.55, facecolor='0.5', alpha=0.3, zorder=1)
	p = plt.axvspan(0.25, 0.55, facecolor='0.5', alpha=0.6, zorder=3)

	# draw the range
	plt.axis([-1, 2, -1, 2])

	plt.show()
# line_span()


# subplot
def onselect_span(vmin, vmax):
	print(vmin, vmax)

def onselect_lasso(verts):
	print(verts)

def subplot():
	fig,ax = plt.subplots()
	ax.plot([1, 2, 3], [10, 50, 100])
	span = mwidgets.SpanSelector(ax, onselect_span, "horizontal", rectprops=dict(alpha=1, facecolor='red'), span_stays=True) 
	# choosing span_stays = True will make the selected area stay on the image.
	# lasso = mwidgets.LassoSelector(ax, onselect=onselect_lasso)

	plt.show()


subplot()

# plt.show()
plt.close()