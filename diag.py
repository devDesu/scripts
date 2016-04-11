#!/usr/bin/python3
import matplotlib.pyplot as plt
from pandas import date_range,Series,DataFrame,read_csv, qcut
from pandas.tools.plotting import radviz,scatter_matrix,bootstrap_plot,parallel_coordinates
from numpy.random import randn
from pylab import *
import brewer2mpl
from matplotlib import rcParams

dark2_colors = brewer2mpl.get_map('Dark2', 'Qualitative', 7).mpl_colors

rcParams['figure.figsize'] = (10, 5)
rcParams['figure.dpi'] = 150
rcParams['axes.color_cycle'] = dark2_colors
rcParams['lines.linewidth'] = 2
rcParams['axes.facecolor'] = 'white'
rcParams['font.size'] = 12
rcParams['patch.edgecolor'] = 'white'
rcParams['patch.facecolor'] = dark2_colors[0]
rcParams['font.family'] = 'StixGeneral'

def remove_border(axes=None, top=False, right=False, left=True, bottom=True):
    """
    Minimize chartjunk by stripping out unnecesasry plot borders and axis ticks
    
    The top/right/left/bottom keywords toggle whether the corresponding plot border is drawn
    """
    ax = axes or plt.gca()
    ax.spines['top'].set_visible(top)
    ax.spines['right'].set_visible(right)
    ax.spines['left'].set_visible(left)
    ax.spines['bottom'].set_visible(bottom)
    
    #turn off all ticks
    ax.yaxis.set_ticks_position('none')
    ax.xaxis.set_ticks_position('none')
    
    #now re-enable visibles
    if top:
        ax.xaxis.tick_top()
    if bottom:
        ax.xaxis.tick_bottom()
    if left:
        ax.yaxis.tick_left()
    if right:
        ax.yaxis.tick_right()

s = [5, 5, 3, 3, 3, 3, 5, 3, 4, 1, 5, 2, 5, 0, 1, 3, 0, 0, 0, 2, 0, 2, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1,\
	0, 0, 0, 0, 2] #6.4
i = date_range('29/2/2016', periods=len(s))
i = [(str(i[n])[:str(i[n]).index(' ')]) for n in range(0, len(i))]
df = DataFrame(s, index=i, columns=['количество'])# date_range('29/3/2016', periods=len(s)))
df.plot(kind='bar');
#df.plot(kind='step')
plt.axhline(0, color='k');
plt.tight_layout()
plt.show()
