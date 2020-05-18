# -*- coding: utf-8 -*-
"""
Created on Thu May 14 15:51:30 2020

@author: user
"""
import matplotlib.pyplot as plt
import numpy as np
import pickle
from estimator_classes import Model
from functions_GA import evalPopu,upperData,nextPopu
from fitness_functions import fitnessCfl






# new reading files
voltage_file='voltage.csv'
current_file='current.csv'

measure,simulation_vars=Model.signals_caracteristics(voltage_file,
                                                     current_file)

#save classes to functions
with open("measure.pickle", "wb") as f:
    pickle.dump(measure, f)

with open("simulation_vars.pickle", "wb") as f:
    pickle.dump(simulation_vars, f)



#%%----------------------------GA------------------------------
popu_size=40
xover_rate=0.9
mut_rate=0.3
bit_n=16
limit=0
epsilon=1e-0



r1=5.978e2
r2=60
c1=3.62e-6

fitness_fcn= 'fitnessCfl'
var_n=3

rango=np.array([[0.1,10e3],
                [0.1,1e3],
                [1-9,100e-6]])

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
fit_solution=np.array([upper[-1,1:]])
dist,measure,simulation_adjust=fitnessCfl(fit_solution , models="true")


plt.figure()
plt.subplot(211)
plt.plot(simulation_adjust.t, simulation_adjust.i) 
plt.plot(measure.t, measure.i)

plt.subplot(212)
plt.plot(simulation_adjust.t, simulation_adjust.v) 
plt.plot(measure.t, measure.v)
