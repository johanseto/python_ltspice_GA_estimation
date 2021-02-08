# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 21:28:04 2020

@author: user
"""
from estimator_classes_pv import ModelPv
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import numpy as np
from plot_file import plotting
#=np.load('popu_2020-Oct-29-08_45.npy')
#upper=np.load('upper_2020-Oct-29-08_45.npy')
#popu2=np.load('popu_2020-Oct-29-10_59.npy')
#upper2=np.load('upper_2020-Oct-29-10_59.npy')
popu=np.load('popu_2020-Nov-01-12_03.npy')
upper=np.load('upper_2020-Nov-01-12_03.npy')
fig, axis = plt.subplots(3, 2)
axis1=axis[0,0]
axis2=axis[0,1]
axis3=axis[1,0]
axis4=axis[1,1]
axis5=axis[2,0]
axis6=axis[2,1]

nlabel_axis=25
nlabel_signal=25
ntick=7
axis1.plot(np.abs(upper[:,0]))
axis1.set_ylabel('Fitness',fontsize=nlabel_axis)
axis1.set_xlabel('$iteración$ [i]',fontsize=nlabel_axis)


axis2.plot(upper[:,4])
#axis5.title('Funcion fitness')
axis2.set_ylabel('$n$[Emission]',fontsize=nlabel_axis)
axis2.set_xlabel('$iteración$ [i]',fontsize=nlabel_axis)



axis3.plot(upper[:,2])
#axis3.title('Funcion fitness')
axis3.set_ylabel('$R_{s}$ [$\Omega$]',fontsize=nlabel_axis)
axis3.set_xlabel('$iteración$ [i]',fontsize=nlabel_axis)

axis4.plot(upper[:,3]*1e9)
#axis4.title('Funcion fitness')
axis4.set_ylabel('$I_s$ [$nA$]',fontsize=nlabel_axis)
axis4.set_xlabel('$iteración$ [i]',fontsize=nlabel_axis)

axis5.plot(upper[:,1])
#axis2.title('Funcion fitness')
axis5.set_ylabel('$R_{sh}$ [$\Omega$]',fontsize=nlabel_axis)
axis5.set_xlabel('$iteración$ [i]',fontsize=nlabel_axis)

axis6.plot(upper[:,5])
#axis6.title('Funcion fitness')
axis6.set_ylabel('$I_{ph}$ [$A$]',fontsize=nlabel_axis)
axis6.set_xlabel('$iteración$ [i]',fontsize=nlabel_axis)

#%%
voltage_current_file='leibold_solar_module_4-100.csv'

ntick=15

measure,simulation_vars=ModelPv.signals_caracteristics(voltage_current_file)
plt.figure()
plt.plot(measure.v,measure.i,linewidth=2,marker='o',markersize=12)
plt.title('Curva V-I de medidas modulo Leibold solar(STE 4/100)',fontsize=25)
plt.xlabel('Tension[V]',fontsize=nlabel_axis)
plt.ylabel('Corriente[A]',fontsize=nlabel_axis)
plt.xlim(measure.v.min(),measure.v.max()+0.1)
plt.ylim(measure.i.min(),measure.i.max()+0.001)
plt.xticks(fontsize=ntick)
plt.yticks(fontsize=ntick)

#%%
from pylab import cm
import matplotlib as mpl
import matplotlib.font_manager as fm
from fitness_functions import fitnessPv
import numpy as np
import matplotlib.pyplot as plt

fit_solution=np.array([upper[-1,1:]])
dist,measure,simulation_adjust=fitnessPv(fit_solution , models="true")

upper2=np.array([[0,2184,2.558,0.12984e-9,1.0304,0.02646]])
fit_solution2=np.array([upper2[-1,1:]])
dist2,measure,simulation_article=fitnessPv(fit_solution2 , models="true")

colors = cm.get_cmap('tab10', 10)

#%%

ntick=15

plt.figure()
plt.plot(measure.v, measure.i, color=colors(0), label='Medidas',marker='o',linewidth=2,markersize=15)
plt.plot(simulation_article.v, simulation_article.i, color=colors(1), 
         label=' Simulada Estado del arte ',marker='x',lineStyle=':',linewidth=2,markersize=15)
plt.plot(simulation_adjust.v, simulation_adjust.i, color=colors(3), 
         label=' Simulada Metodología propuesta ',marker='*',lineStyle=':',alpha=0.8,linewidth=2,markersize=15)

plt.title('Resultados',fontsize=nlabel_axis)
   
plt.xlabel('Tension[V]',fontsize=nlabel_axis)

plt.ylabel(r'Corriente[A]',fontsize=nlabel_axis)
plt.legend(fontsize=nlabel_signal)
plt.xticks(fontsize=ntick)
plt.yticks(fontsize=ntick)