# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 09:23:39 2020

@author: user
"""
import matplotlib.pyplot as plt
import numpy as np
import pickle
from estimator_classes import Model

from pylab import cm
import matplotlib as mpl



# new reading files
voltage_file='voltage.csv'
current_file='current.csv'

measure,simulation_vars=Model.signals_caracteristics(voltage_file,
                                                     current_file)

colors = cm.get_cmap('tab10', 10)
f, (ax2, ax1) = plt.subplots(2, 1)

ax1.plot(measure.t, measure.i,linewidth=3, color=colors(1), label='i- medida')
ax2.set_title('Señales medidas')
ax1.set_xlabel(r'Tiempo(s)', labelpad=10)
ax1.set_xlim(0, measure.t[-1])
ax1.set_ylim(min(measure.i)-0.1, max(measure.i)+0.1)
# ax1.set_xlabel('Iteracion(i)')

ax1.set_ylabel(r'Corriente(A)', labelpad=10)
# ax1.spines['right'].set_visible(False)
# ax1.spines['top'].set_visible(False)
ax1.xaxis.set_tick_params(which='major', size=10, width=2, direction='in')
ax1.xaxis.set_tick_params(which='minor', size=7, width=2, direction='in')
ax1.yaxis.set_tick_params(which='major', size=10, width=2, direction='in')
ax1.yaxis.set_tick_params(which='minor', size=7, width=2, direction='in')
ax1.grid(True)

ax1.xaxis.set_major_locator(mpl.ticker.MultipleLocator(1/120))
ax1.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(1/240))
ax1.yaxis.set_major_locator(mpl.ticker.MultipleLocator(max(measure.i)/4  ))
ax1.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(max(measure.i)/2  ))
ax1.legend(bbox_to_anchor=(0.78, 0.8), loc=10, frameon=True, fontsize=14)


ax2.plot(measure.t, measure.v, linewidth=3,color=colors(0),
         label='v-medida')

ax2.set_xlim(0, measure.t[-1])
ax2.set_ylim(min(measure.v)-10, max(measure.v)+10)
ax2.set_ylabel(r'Tension(V)', labelpad=10)

ax2.xaxis.set_tick_params(which='major', size=10, width=2, direction='in')
ax2.xaxis.set_tick_params(which='minor', size=7, width=2, direction='in')
ax2.yaxis.set_tick_params(which='major', size=10, width=2, direction='in')
ax2.yaxis.set_tick_params(which='minor', size=7, width=2, direction='in')
ax2.grid(True)

ax2.xaxis.set_major_locator(mpl.ticker.MultipleLocator(1/120))
ax2.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(1/240))
ax2.yaxis.set_major_locator(mpl.ticker.MultipleLocator(50))
ax2.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(25))
ax2.legend(bbox_to_anchor=(0.78, 0.8), loc=10, frameon=True, fontsize=14)
v_rms=np.sqrt(np.mean(measure.v**2))
i_rms= np.sqrt(np.mean(measure.i**2))



#%%Searching times 

with open("time.pickle", "rb") as f:
    time_sim = pickle.load(f)
    
with open("newsim_time.pickle", "rb") as f:
    time_sim2 = pickle.load(f)
    
dt=[]
for i in range(1,len(time_sim)):
    dt.append(time_sim[i]-time_sim[i-1])
    
dt2=[]
for i in range(1,len(time_sim)):
    dt2.append(time_sim2[i]-time_sim2[i-1])

dt=np.array(dt)
dt2=np.array(dt2)

fig = plt.figure()
ax1 = fig.add_axes([0.1, 0.1,0.8, 0.8])
ax1.plot(dt*1e6,linewidth=2, color=colors(0), label='ltspice dt')
ax1.plot(dt2*1e6,linewidth=2, color=colors(1), label='medida dt')
ax1.set_title('Pasos de integracion')
ax1.set_xlim(0, len(dt))
ax1.set_ylim(0, 2000)
ax1.set_ylabel('dt(us)')
# ax1.spines['right'].set_visible(False)
# ax1.spines['top'].set_visible(False)
ax1.xaxis.set_tick_params(which='major', size=10, width=2, direction='in')
ax1.xaxis.set_tick_params(which='minor', size=7, width=2, direction='in')
ax1.yaxis.set_tick_params(which='major', size=10, width=2, direction='in')
ax1.yaxis.set_tick_params(which='minor', size=7, width=2, direction='in')
ax1.grid(True)

f, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(dt*1e6,linewidth=2, color=colors(0), label='ltspice dt')
ax1.set_title('Pasos de integracion')
ax1.set_xlim(0, len(dt))
ax1.set_ylim(0, 2000)
ax1.set_ylabel('dt(us)')
# ax1.spines['right'].set_visible(False)
# ax1.spines['top'].set_visible(False)
ax1.xaxis.set_tick_params(which='major', size=10, width=2, direction='in')
ax1.xaxis.set_tick_params(which='minor', size=7, width=2, direction='in')
ax1.yaxis.set_tick_params(which='major', size=10, width=2, direction='in')
ax1.yaxis.set_tick_params(which='minor', size=7, width=2, direction='in')
ax1.grid(True)
ax1.legend(bbox_to_anchor=(0.78, 0.9), loc=10, frameon=True, fontsize=14)

ax2.plot(dt2*1e6,linewidth=2, color=colors(1), label='medida dt')


ax2.set_xlim(0, len(dt))
ax2.set_ylim(0, 20)
ax2.set_ylabel('dt(us)')
# ax1.spines['right'].set_visible(False)
# ax1.spines['top'].set_visible(False)
ax2.xaxis.set_tick_params(which='major', size=10, width=2, direction='in')
ax2.xaxis.set_tick_params(which='minor', size=7, width=2, direction='in')
ax2.yaxis.set_tick_params(which='major', size=10, width=2, direction='in')
ax2.yaxis.set_tick_params(which='minor', size=7, width=2, direction='in')
ax2.grid(True)
ax2.legend(bbox_to_anchor=(0.78, 0.8), loc=10, frameon=True, fontsize=14)