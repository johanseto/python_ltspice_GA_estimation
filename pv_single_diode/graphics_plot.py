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


axis1.plot(np.abs(upper[:,0]))
axis1.set_ylabel('RMSE')
axis1.set_xlabel('$iteración$ [i]')

axis2.plot(upper[:,4])
#axis5.title('Funcion fitness')
axis2.set_ylabel('$n$[Emission]')
axis2.set_xlabel('$iteración$ [i]')



axis3.plot(upper[:,2])
#axis3.title('Funcion fitness')
axis3.set_ylabel('$R_{s}$ [$\Omega$]')
axis3.set_xlabel('$iteración$ [i]')

axis4.plot(upper[:,3]*10e6)
#axis4.title('Funcion fitness')
axis4.set_ylabel('$I_s$ [$uA$]')
axis4.set_xlabel('$iteración$ [i]')

axis5.plot(upper[:,1])
#axis2.title('Funcion fitness')
axis5.set_ylabel('$R_{sh}$ [$\Omega$]')
axis5.set_xlabel('$iteración$ [i]')

axis6.plot(upper[:,5])
#axis6.title('Funcion fitness')
axis6.set_ylabel('$I_\lambda$ [$A$]')
axis6.set_xlabel('$iteración$ [i]')

#%%
voltage_current_file='leibold_solar_module_4-100.csv'


measure,simulation_vars=ModelPv.signals_caracteristics(voltage_current_file)
plt.figure()
plt.plot(measure.v,measure.i,linewidth=2,marker='o')
plt.title('Curva V-I de medidas modulo Leibold solar(STE 4/100)',fontsize=15)
plt.xlabel('Tension[V]')
plt.ylabel('Corriente[A]')
plt.xlim(measure.v.min(),measure.v.max()+0.1)
plt.ylim(measure.i.min(),measure.i.max()+0.001)

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

plt.figure()
plt.plot(measure.v, measure.i, color=colors(0), label='Medidas',marker='o')
plt.plot(simulation_article.v, simulation_article.i, color=colors(3), 
         label=' Simulada Estado del arte ',marker='x',lineStyle=':')
plt.plot(simulation_adjust.v, simulation_adjust.i, color=colors(6), 
         label=' Simulada Metodología',marker='*',lineStyle=':',alpha=0.8)

plt.title('Resultados')
   
plt.xlabel('Tension[V]')

plt.ylabel(r'Corriente[A]', labelpad=10)
plt.legend()