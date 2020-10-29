# -*- coding: utf-8 -*-
"""
Created on Thu May 14 15:51:30 2020

@author: user
"""

import numpy as np
import pickle
from estimator_classes_trafo import ModelTrafo
from functions_GA import evalPopu,upperData,nextPopu
from plot_file import plotting
import datetime






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
popu_size=250
xover_rate=0.98
mut_rate=0.1
bit_n=10
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
                [1e-6,2],
                [1e-6,2],
                [1e-6,2]])

# popu=np.random.rand(popu_size,bit_n*var_n) >0.5 #popu means population
# popu=popu*1 #pass from bolean to int
popu=np.load('popu_2020-Oct-28-01_23.npy')
upper=np.array([]) #Matriz para mejores individuos


i=0

while limit<=15:
    
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
plotting(upper)
upper2=np.array([[0,1,1000,0.01,1,0.01]])
