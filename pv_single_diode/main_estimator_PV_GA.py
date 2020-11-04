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
from plot_file import plotting
import datetime




# new reading files
voltage_current_file='leibold_solar_module_4-100.csv'


measure,simulation_vars=ModelPv.signals_caracteristics(voltage_current_file)

#save classes to functions
with open("measure.pickle", "wb") as f:
    pickle.dump(measure, f)

with open("simulation_vars.pickle", "wb") as f:
    pickle.dump(simulation_vars, f)



#%%----------------------------GA------------------------------
popu_size=250
xover_rate=0.98
mut_rate=0.01
bit_n=12
limit=0
epsilon=1e-0


# ind_module=np.array([[2184,2.558,0.12984e-9,1.0304,0.02646,20]])
#ind_cell=np.array([[52.4768,0.0367251,0.29815e-6,1.43,0.760849,33]])
#]#Rshunt,Rserie,saturation currenta,emission coeef,ilambda,temperature
fitness_fcn= 'fitnessPv'
var_n=5
#with the deppendicie of number of cell n can change his value for a cosntant 
#and the recision of if isat one cell(pA-ua) many cells:,(na-ua)
# rango=np.array([[0.1,1000],    
#                 [1e-9,5],      
#                 [1e-9,50e-6], #Take care o the number of cell for precition
#                 [1,2],           #Change fittness funtion for includes Kcells*n
#                 [0.1e-3,1]])#cero to 1 in cells
#                # [0,100]])        
rango=np.array([[0.1,3000],    
                [1e-9,5],      
                [1e-10,0.1e-6], #Take care o the number of cell for precition
                [1,2],           #Change fittness funtion for includes Kcells*n
                [0.1e-9,1]])#cero to 1 in cells
               # [0,100]]) 


popu=np.random.rand(popu_size,bit_n*var_n) >0.5 #popu means population
popu=popu*1

upper=np.array([]) #Matriz para mejores individuos

#popu_eval=evalPopu(popu,bit_n,rango,fitness_fcn) prueba de funcion  
i=0

while limit<=25:
    
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
    
    
    
#%% Saving progress numpy arrays
#fit_solution=np.array([upper[-1,:]])

today=datetime.datetime.today()
today_str='{:%Y-%b-%d-%H_%M}'.format(today)
np.save('upper_'+today_str+'.npy',upper)
np.save('popu_'+today_str+'.npy',popu)
#%% plotting
cost1=plotting(upper)
#upper2=np.array([[0,52.4768,0.0367251,0.29815e-6,1.43,0.760849]])
upper2=np.array([[0,2184,2.558,0.12984e-9,1.0304,0.02646]])
cost2=plotting(upper2)