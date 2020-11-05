# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 21:05:05 2020

@author: user
"""

import pandas as pd
from pylab import cm
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
# Rebuild the matplotlib font cache
fm._rebuild()
import numpy as np
mpl.rcParams['font.family'] = 'Avenir'
plt.rcParams['font.size'] = 18
plt.rcParams['axes.linewidth'] = 2
colors = cm.get_cmap('tab10', 10)

a=pd.read_fwf('upper_120_100_40iter.txt')
a=np.array(a)
fit_solution=np.array([a[-1,1:]])
# Create figure and add axes object
# fig = plt.figure()
# ax = fig.add_axes([0, 0, 1, 1])

f, (ax1, ax2,ax3) = plt.subplots(3, 1)
ax1.plot(a[:,1],linewidth=2, color=colors(0), label='R')
ax1.set_title('PARAMETROS')
ax1.set_xlim(0, 88)
ax1.set_ylim(1500, 2250)
# ax1.set_xlabel('Iteracion(i)')

ax1.set_ylabel(r'Rd($\mathregular{\Omega}$)', labelpad=10)
# ax1.spines['right'].set_visible(False)
# ax1.spines['top'].set_visible(False)
ax1.xaxis.set_tick_params(which='major', size=10, width=2, direction='in')
ax1.xaxis.set_tick_params(which='minor', size=7, width=2, direction='in')
ax1.yaxis.set_tick_params(which='major', size=10, width=2, direction='in')
ax1.yaxis.set_tick_params(which='minor', size=7, width=2, direction='in')
ax1.grid(True)

ax1.xaxis.set_major_locator(mpl.ticker.MultipleLocator(10))
ax1.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(5))
ax1.yaxis.set_major_locator(mpl.ticker.MultipleLocator(250))
ax1.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(250/2))


ax2.plot(a[:,2],linewidth=2, color=colors(1), label='Rd')
ax2.set_xlim(0, 88)
ax2.set_ylim(0, 100)
ax2.set_ylabel(r'R($\mathregular{\Omega}$)', labelpad=10)
ax2.xaxis.set_tick_params(which='major', size=10, width=2, direction='in')
ax2.xaxis.set_tick_params(which='minor', size=7, width=2, direction='in')
ax2.yaxis.set_tick_params(which='major', size=10, width=2, direction='in')
ax2.yaxis.set_tick_params(which='minor', size=7, width=2, direction='in')
ax2.grid(True)

ax2.xaxis.set_major_locator(mpl.ticker.MultipleLocator(10))
ax2.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(5))
ax2.yaxis.set_major_locator(mpl.ticker.MultipleLocator(25))
ax2.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(25/2))


# Plot and show our data
ax3.plot(a[:,3]*1e6,linewidth=2, color=colors(2), label='C')
ax3.set_xlim(0, 88)
ax3.set_ylim(8.9,12.3)
ax3.set_ylabel(r'C(uF)', labelpad=10)
ax3.xaxis.set_tick_params(which='major', size=10, width=2, direction='in')
ax3.xaxis.set_tick_params(which='minor', size=7, width=2, direction='in')
ax3.yaxis.set_tick_params(which='major', size=10, width=2, direction='in')
ax3.yaxis.set_tick_params(which='minor', size=7, width=2, direction='in')
ax3.grid(True)

ax3.xaxis.set_major_locator(mpl.ticker.MultipleLocator(10))
ax3.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(5))
ax3.yaxis.set_major_locator(mpl.ticker.MultipleLocator(1))
ax3.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(0.5))
ax3.set_xlabel('Iteracion(i)')
plt.show()


#%%Load the solution

