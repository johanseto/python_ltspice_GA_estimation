# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 15:09:17 2021

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 21:28:04 2020
@author: user
"""
from estimator_classes import Model
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import numpy as np
from plot_file import plotting
from pylab import cm
import matplotlib as mpl
#=np.load('popu_2020-Oct-29-08_45.npy')
#upper=np.load('upper_2020-Oct-29-08_45.npy')
#popu2=np.load('popu_2020-Oct-29-10_59.npy')
#upper2=np.load('upper_2020-Oct-29-10_59.npy')
popu=np.load('popu_2021-Jan-12-20_36.npy')
upper=np.load('upper_2021-Jan-12-20_36.npy')
fig, axis = plt.subplots(2, 2)
axis1=axis[0,0]
axis2=axis[0,1]
axis3=axis[1,0]
axis4=axis[1,1]

nlabel_axis=25
nlabel_signal=25

axis1.plot(np.sqrt(np.abs(upper[:,0])))
axis1.set_ylabel('Fitness',fontsize=nlabel_axis)
axis1.set_xlabel('$iteración$ [i]',fontsize=nlabel_axis)

axis2.plot(upper[:,1])
#axis5.title('Funcion fitness')
axis2.set_ylabel('$R$ [$\Omega$]',fontsize=nlabel_axis)
axis2.set_xlabel('$iteración$ [i]',fontsize=nlabel_axis)



axis3.plot(upper[:,2])
#axis3.title('Funcion fitness')
axis3.set_ylabel('$R_{d}$ [$\Omega$]',fontsize=nlabel_axis)
axis3.set_xlabel('$iteración$ [i]',fontsize=nlabel_axis)

axis4.plot(upper[:,3]*1e6)
#axis4.title('Funcion fitness')
axis4.set_ylabel('$C$ [$uF$]',fontsize=nlabel_axis)
axis4.set_xlabel('$iteración$ [i]',fontsize=nlabel_axis)




#%%
voltage_file='voltage.csv'
current_file='current.csv'

nlabel_axis=25
nlabel_signal=25


measure,simulation_vars=Model.signals_caracteristics(voltage_file,current_file)
colors = cm.get_cmap('tab10', 10)
f, (ax2, ax1) = plt.subplots(2, 1)

ax2.plot(measure.t*1e3, measure.v, linewidth=3,color=colors(1),
         label='v-Medida')

ax2.set_xlim(0, measure.t[-1]*1e3)
ax2.set_ylim(min(measure.v)-10, max(measure.v)+10)
ax2.set_ylabel(r'Tensión(V)', fontsize=nlabel_axis)
ax2.set_xlabel(r'Tiempo(ms)', fontsize=nlabel_axis)
ax2.xaxis.set_tick_params(labelsize=20)
ax2.yaxis.set_tick_params(labelsize=20)
ax2.legend(bbox_to_anchor=(0.78, 0.8), loc=10, frameon=True, fontsize=nlabel_signal)

ax1.plot(measure.t*1e3, measure.i,linewidth=3, color=colors(0), 
         label=' i-Medida')
ax2.set_title('Señales medidas CFL',fontsize=nlabel_axis)
ax1.set_xlim(0, measure.t[-1]*1e3)
ax1.set_ylim(min(measure.i)-0.1, max(measure.i)+0.1)
# ax1.set_xlabel('Iteracion(i)')
ax1.set_xlabel(r'Tiempo(ms)', fontsize=nlabel_axis)
ax1.set_ylabel(r'Corriente(A)', fontsize=nlabel_axis)
ax1.xaxis.set_tick_params(labelsize=20)
ax1.yaxis.set_tick_params(labelsize=20)
ax1.legend(bbox_to_anchor=(0.78, 0.8), loc=10, frameon=True, fontsize=nlabel_signal)






#%%


fit_solution=np.array([upper[-1,1:]])



fx=plotting(fit_solution)


