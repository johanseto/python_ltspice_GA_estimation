# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 09:24:50 2020

@author: user
"""

from estimator_classes_trafo import ModelTrafo
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import numpy as np
from plot_file import plotting
#=np.load('popu_2020-Oct-29-08_45.npy')
#upper=np.load('upper_2020-Oct-29-08_45.npy')
#popu2=np.load('popu_2020-Oct-29-10_59.npy')
#upper2=np.load('upper_2020-Oct-29-10_59.npy')
upper_0=np.load('upper_2020-Oct-31-09_49.npy')
popu=np.load('popu_2020-Oct-31-13_31.npy')
upper=np.load('upper_2020-Oct-31-13_31.npy')
#upper_2=np.load('upper_2020-Oct-31-14_05.npy')
upper_3=np.load('upper_2020-Oct-31-23_24.npy')
#upper=np.concatenate((upper_2, upper_3), axis=0)
#upper_4=np.load('upper_2020-Nov-01-17_05.npy')
#prueba=np.concatenate((upper,upper upper_3), axis=0)
upper=np.concatenate((upper[:21,:], upper_3), axis=0)
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

axis2.plot(upper[:,3])
#axis5.title('Funcion fitness')
axis2.set_ylabel('$L$ [H]')
axis2.set_xlabel('$iteración$ [i]')



axis3.plot(upper[:,1])
#axis3.title('Funcion fitness')
axis3.set_ylabel('$R$ [$\Omega$]')
axis3.set_xlabel('$iteración$ [i]')

axis4.plot(upper[:,4])
#axis4.title('Funcion fitness')
axis4.set_ylabel('$L_{m}$ [H]')
axis4.set_xlabel('$iteración$ [i]')

axis5.plot(upper[:,2])
#axis2.title('Funcion fitness')
axis5.set_ylabel('$R_{c}$ [$\Omega$]')
axis5.set_xlabel('$iteración$ [i]')

axis6.plot(np.sqrt(upper[:,4]/upper[:,5]))
#axis6.title('Funcion fitness')
axis6.set_ylabel('$N$ ')
axis6.set_xlabel('$iteración$ [i]')

# axis6.plot(np.sqrt(upper[:,4]/upper[:,5]))
# #axis6.title('Funcion fitness')
# axis6.set_ylabel('$N$ ')
# axis6.set_xlabel('$iteración$ [i]')

#%%
signals_file='values_noise.csv'


measure,simulation_vars=ModelTrafo.signals_caracteristics(signals_file)


#%%
from pylab import cm
import matplotlib as mpl
import matplotlib.font_manager as fm
from fitness_functions import fitnessTrafo
import numpy as np
import matplotlib.pyplot as plt

fit_solution=np.array([upper[-1,1:]])
dist,measure,simulation_adjust=fitnessTrafo(fit_solution , models="true")

# upper2=np.array([[0,1,1000,0.01,1,0.01]])
# fit_solution2=np.array([upper2[-1,1:]])
# dist2,measure,simulation_article=fitnessTrafo(fit_solution2 , models="true")

colors = cm.get_cmap('tab10', 10)

#%%
colors = cm.get_cmap('tab10', 10)

# plt.plot(measure.v, measure.i, color=colors(0), label='Medidas',marker='o')
# plt.plot(simulation_article.v, simulation_article.i, color=colors(3), 
#          label=' Simulada Estado del arte ',marker='x',lineStyle=':')
# plt.plot(simulation_adjust.v, simulation_adjust.i, color=colors(6), 
#          label=' Simulada Metodología',marker='*',lineStyle=':',alpha=0.8)

# plt.title('Resultados')
   
# plt.xlabel('Tension[V]')

# plt.ylabel(r'Corriente[A]', labelpad=10)
# plt.legend()

fig, axis = plt.subplots(2, 2)
axis1=axis[0,0]
axis2=axis[0,1]
axis3=axis[1,0]
axis4=axis[1,1]




axis1.set_ylabel('Tension[V]')
axis1.set_xlabel('Tiempos[s]')
axis1.set_title('V1')
axis1.plot(measure.t, measure.v1 ,color=colors(2), label='Medidas propuesta',alpha=0.8,linewidth=2)
axis1.plot(simulation_adjust.t, simulation_adjust.v1,color='black',linestyle='--',label='Simulacion metodologia') 
axis1.legend(bbox_to_anchor=(1.2, 1.2), loc=10, frameon=True, fontsize=14)

axis2.set_title('V2')
axis2.set_ylabel('Tension[V]')
axis2.set_xlabel('Tiempo[s]')
axis2.plot(measure.t, measure.v2 ,color=colors(2), label='Medidas',alpha=0.8,linewidth=2)
axis2.plot(simulation_adjust.t, simulation_adjust.v2,color='black',linestyle='--',label='Simulacion metodologia') 



axis3.set_title('i1')
axis3.set_ylabel('Corriente[A]')
axis3.set_xlabel('Tiempo[s]')
axis3.plot(measure.t, measure.i1 ,color=colors(2), label='Medidas',alpha=0.8,linewidth=2)
axis3.plot(simulation_adjust.t, simulation_adjust.i1,color='black',linestyle='--',label='Simulacion metodologia') 


axis4.set_title('i2')
axis4.set_ylabel('Corriente[A]')
axis4.set_xlabel('Tiempo[s]')
axis4.plot(measure.t, measure.i2 ,color=colors(2), label='Medidas',alpha=0.8,linewidth=2)
axis4.plot(simulation_adjust.t, simulation_adjust.i2,color='black',linestyle='--',label='Simulacion metodologia')  




    

#%%
base_v1=max(measure.v1)-min(measure.v1)
base_i1=max(measure.i1)-min(measure.i1)
base_v2=max(measure.v2)-min(measure.v2)
base_i2=max(measure.i2)-min(measure.i2)
rmse_v1 = np.sqrt(mean_squared_error(measure.v1,simulation_adjust.v1))/base_v1
rmse_i1=np.sqrt(mean_squared_error(measure.i1/base_i1,
                                    simulation_adjust.i1/base_i1))#equival
rmse_v2=np.sqrt(mean_squared_error(measure.v2/base_v2,
                                    simulation_adjust.v2/base_v2))
rmse_i2=np.sqrt(mean_squared_error(measure.i2/base_i2,
                                    simulation_adjust.i2/base_i2))
 
rmse=[rmse_i1,rmse_v2,rmse_i2] #vector de  normas
rmse_norm=np.linalg.norm(rmse)
    
