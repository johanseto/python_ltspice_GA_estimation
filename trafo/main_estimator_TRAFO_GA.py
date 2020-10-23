# -*- coding: utf-8 -*-
"""
Created on Thu May 14 15:51:30 2020

@author: user
"""
import matplotlib.pyplot as plt
import numpy as np
import pickle
from estimator_classes_trafo import ModelTrafo
from functions_GA import evalPopu,upperData,nextPopu
from fitness_functions import fitnessTrafo






# new reading files
signals_file='values_noise.csv'
#measure=ModelTrafo.read_csv_signal(signals_file)

measure,simulation_vars=ModelTrafo.signals_caracteristics(signals_file)

#save classes to functions
with open("measure.pickle", "wb") as f:
    pickle.dump(measure, f)

with open("simulation_vars.pickle", "wb") as f:
    pickle.dump(simulation_vars, f)



#%%----------------------------GA------------------------------
popu_size=200
xover_rate=0.95
mut_rate=0.05
bit_n=12
limit=0
epsilon=1e-0



#r1=1
#r2=1000
#L1=0.01
#L2=1
#L3=0.01 #ASsociada a numero de vueltas


fitness_fcn= 'fitnessTrafo'
var_n=5

rango=np.array([[1e-3,10],
                [1e-3,2000],
                [1e-6,5],
                [1e-6,5],
                [1e-6,5]])

popu=np.random.rand(popu_size,bit_n*var_n) >0.5 #popu means population
popu=popu*1 #pass from bolean to int

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
fit_solution=np.array([upper[-1,1:]])
dist,measure,simulation_adjust=fitnessTrafo(fit_solution , models="true")
from pylab import cm
import matplotlib as mpl
import matplotlib.font_manager as fm

colors = cm.get_cmap('tab10', 10)
f, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(simulation_adjust.t, simulation_adjust.i1,linewidth=3, color=colors(0), 
         label=' i-simulada')
ax1.plot(measure.t, measure.i1,linewidth=3, color=colors(1), label='i- medida')
ax1.set_title('Resultados')
# ax1.set_xlim(0, measure.t[-1])
# ax1.set_ylim(min(measure.v1)-0.1, max(measure.i1)+0.1)
# ax1.set_xlabel('Iteracion(i)')

ax1.set_ylabel(r'Corriente(A)', labelpad=10)
# ax1.spines['right'].set_visible(False)
# ax1.spines['top'].set_visible(False)
# ax1.xaxis.set_tick_params(which='major', size=10, width=2, direction='in')
# ax1.xaxis.set_tick_params(which='minor', size=7, width=2, direction='in')
# ax1.yaxis.set_tick_params(which='major', size=10, width=2, direction='in')
# ax1.yaxis.set_tick_params(which='minor', size=7, width=2, direction='in')
# ax1.grid(True)

# ax1.xaxis.set_major_locator(mpl.ticker.MultipleLocator(1/120))
# ax1.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(1/240))
# ax1.yaxis.set_major_locator(mpl.ticker.MultipleLocator(max(measure.i)/4  ))
# ax1.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(max(measure.i)/2  ))
# ax1.legend(bbox_to_anchor=(0.78, 0.8), loc=10, frameon=True, fontsize=14)

ax2.plot(simulation_adjust.t, simulation_adjust.v1, linewidth=3,color=colors(0),
         label='v-simulada')
ax2.plot(measure.t, measure.v1, linewidth=3,color=colors(1),
         label='v-medida')

# ax2.set_xlim(0, measure.v1[-1])
# ax2.set_ylim(min(measure.v1)-10, max(measure.v)+10)
# ax2.set_ylabel(r'Tension(V)', labelpad=10)
# ax2.xaxis.set_tick_params(which='major', size=10, width=2, direction='in')
# ax2.xaxis.set_tick_params(which='minor', size=7, width=2, direction='in')
# ax2.yaxis.set_tick_params(which='major', size=10, width=2, direction='in')
# ax2.yaxis.set_tick_params(which='minor', size=7, width=2, direction='in')
# ax2.grid(True)

# ax2.xaxis.set_major_locator(mpl.ticker.MultipleLocator(1/120))
# ax2.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(1/240))
# ax2.yaxis.set_major_locator(mpl.ticker.MultipleLocator(50))
# ax2.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(25))
# ax2.legend(bbox_to_anchor=(0.78, 0.8), loc=10, frameon=True, fontsize=14)





plt.figure()
plt.subplot(221)
plt.plot(simulation_adjust.t, simulation_adjust.v1) 
plt.plot(measure.t, measure.v1)

plt.subplot(222)
plt.plot(simulation_adjust.t, simulation_adjust.v2) 
plt.plot(measure.t, measure.v2)

plt.subplot(223)
plt.plot(simulation_adjust.t, simulation_adjust.i1) 
plt.plot(measure.t, measure.i1)

plt.subplot(224)
plt.plot(simulation_adjust.t, simulation_adjust.i2) 
plt.plot(measure.t, measure.i2)


from sklearn.metrics import mean_squared_error
mse = mean_squared_error(measure.i1, simulation_adjust.i1)
rmse=np.sqrt(mse)

rms_v = np.sqrt(np.mean(measure.v1**2))
rms_imeas = np.sqrt(np.mean(measure.i1**2))
rms_isim = np.sqrt(np.mean(simulation_adjust.i1**2))

square_relative_error_fromIrms=rmse/rms_imeas
relative_root_mean_square_error=rmse/sum(measure.i1)

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