# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 21:28:44 2020

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
colors = cm.get_cmap('tab10', 2)

a=pd.read_fwf('upper_120_100_40iter.txt')
a=np.array(a)
fit_solution=np.array([a[-1,1:]])
mpl.rcParams['font.family'] = 'Avenir'
plt.rcParams['font.size'] = 18
plt.rcParams['axes.linewidth'] = 2
colors = cm.get_cmap('tab10', 2)

a=pd.read_fwf('upper_120_100_40iter.txt')
a=np.array(a)
fit_solution=np.array([a[-1,1:]])
# Create figure and add axes object
# fig = plt.figure()
# ax = fig.add_axes([0, 0, 1, 1])

#




# fig = plt.figure(figsize=(3, 3))
fig = plt.figure()
ax1 = fig.add_axes([0.1, 0.1,0.8, 0.8])
ax1.plot(a[:,1],linewidth=2, color=colors(0), label='Sample 1')
ax1.set_title('PARAMETROS')
ax1.set_xlim(0, 88)
ax1.set_ylim(1500, 2250)
ax1.set_xlabel('Iteracion(i)')
ax1.set_ylabel('R')
# ax1.spines['right'].set_visible(False)
# ax1.spines['top'].set_visible(False)
ax1.xaxis.set_tick_params(which='major', size=10, width=2, direction='in')
ax1.xaxis.set_tick_params(which='minor', size=7, width=2, direction='in')
ax1.yaxis.set_tick_params(which='major', size=10, width=2, direction='in')
ax1.yaxis.set_tick_params(which='minor', size=7, width=2, direction='in')
ax1.grid(True)

ax1.xaxis.set_major_locator(mpl.ticker.MultipleLocator(10))
ax1.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(5))
ax1.yaxis.set_major_locator(mpl.ticker.MultipleLocator(500))
ax1.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(250))
