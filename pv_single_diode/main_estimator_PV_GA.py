# -*- coding: utf-8 -*-
"""
Created on Thu May 14 15:51:30 2020

@author: user
"""
import matplotlib.pyplot as plt
import numpy as np
import pickle
from estimator_classes_pv import ModelPv
from functions_GA import evalPopu,upperData,nextPopu
from fitness_functions import fitnessPv






# new reading files
voltage_current_file='french_solar_cell.csv'


measure,simulation_vars=ModelPv.signals_caracteristics(voltage_current_file)

#save classes to functions
with open("measure.pickle", "wb") as f:
    pickle.dump(measure, f)

with open("simulation_vars.pickle", "wb") as f:
    pickle.dump(simulation_vars, f)



#%%----------------------------GA------------------------------
popu_size=40
xover_rate=0.9
mut_rate=0.3
bit_n=20
limit=0
epsilon=1e-0



#ind_fl=np.array([[52.4768,0.0367251,0.760849,1.43,33,0.29815e-6]])
#]#Rshunt,Rserie,saturation currenta,emission coeef,ilambda,temperature
fitness_fcn= 'fitnessPv'
var_n=6
#with the deppendicie of number of cell n can change his value for a cosntant 
#and the recision of if isat one cell(pA-ua) many cells:,(na-ua)
rango=np.array([[0.1,1000],    
                [0.1,100],      
                [0.1e-9,100e-6], #Take care o the number of cell for precition
                [1,3],           #Change fittness funtion for includes Kcells*n
                [0.1e-3,10],
                [0,100]])        

popu=np.random.rand(popu_size,bit_n*var_n) >0.5 #popu means population
popu=popu*1

upper=np.array([]) #Matriz para mejores individuos

#popu_eval=evalPopu(popu,bit_n,rango,fitness_fcn) prueba de funcion  
i=0

while limit<=40:
    
    #popu_fit means popu fit evaluated
    popu_eval=evalPopu(popu,bit_n,rango,fitness_fcn)  
    upper=upperData(upper,popu_eval,i,var_n,bit_n,rango,popu)
    
    
    if i>=1:
        if upper[i,0]==upper[i-1,0]:
            limit+=1
        else:
            limit=0
          
    i+=1
    popu=nextPopu(popu,popu_eval,xover_rate,mut_rate)
    
    
    
#%% plotting
#fit_solution=np.array([upper[-1,:]])
fit_solution=np.array([[1.946521368734263888e+03,1.888197756923780801e+01,1.201735957885099540e-05]])
dist,measure,simulation_adjust=fitnessPv(fit_solution , models="true")
from pylab import cm
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

colors = cm.get_cmap('tab10', 10)
f, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(simulation_adjust.t, simulation_adjust.i,linewidth=3, color=colors(0), 
         label=' i-simulada')
ax1.plot(measure.t, measure.i,linewidth=3, color=colors(1), label='i- medida')
ax1.set_title('Resultados')
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

ax2.plot(simulation_adjust.t, simulation_adjust.v, linewidth=3,color=colors(0),
         label='v-simulada')
ax2.plot(measure.t, measure.v, linewidth=3,color=colors(1),
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





plt.figure()
plt.subplot(211)
plt.plot(simulation_adjust.t, simulation_adjust.i) 
plt.plot(measure.t, measure.i)

plt.subplot(212)
plt.plot(simulation_adjust.t, simulation_adjust.v) 
plt.plot(measure.t, measure.v)

from sklearn.metrics import mean_squared_error
mse = mean_squared_error(measure.i, simulation_adjust.i)
rmse=np.sqrt(mse)

rms_v = np.sqrt(np.mean(measure.v**2))
rms_imeas = np.sqrt(np.mean(measure.i**2))
rms_isim = np.sqrt(np.mean(simulation_adjust.i**2))

square_relative_error_fromIrms=rmse/rms_imeas
relative_root_mean_square_error=rmse/sum(measure.i)

#%%Searching times 
import pickle
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