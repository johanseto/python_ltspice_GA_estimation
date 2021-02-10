# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 17:32:07 2021

@author: user
"""

import numpy as np
import pickle
from estimator_classes_general import Model,SimulationInfo
from functions_GA import evalPopu,upperData,nextPopu
from plot_file import plotting
import datetime

#%%Measure data recolecction

signals_file='values_noise.csv'
n=4

signal_name=['v1','i1','v2','i2']
measure=Model.read_csv_signal(signals_file,4)
measure2=Model(measure.time,measure.signals[1:])
with open("measure.pickle", "wb") as f:
    pickle.dump(measure2, f)

#%%Prepare the inputs characteristics

sim_name='trafo_single'
sim_raw='/'+sim_name+'.raw'
netlist_path= r'C:\Users\user\Desktop\python_spice\trafo\trafo_single.net'


parameters=['R1','R2','L1','L2','L3']

#signals=['V(n001)','I(R1)','V(n004)','I(L4)']

signals2=['I(R1)','V(n004)','I(L4)']
simu_data=SimulationInfo(netlist_path,sim_raw,parameters,signals2,norm=True)

#simu_data.netlistGen(netlist_path,parameters)


#%%----------------------------GA------------------------------
popu_size=100
xover_rate=0.98
mut_rate=0.4
bit_n=10
limit=0
epsilon=1e-0
stop_criteria=20


#r1=1
#r2=1000
#L1=0.01
#L2=1
#L3=0.01 #ASsociada a numero de vueltas


fitness_fcn= 'fitnessGeneral'
var_n=5

rango=np.array([[1e-3,10],
                [1e-3,2000],
                [1e-6,2],
                [1e-6,2],
                [1e-6,2]])


popu=np.random.rand(popu_size,bit_n*var_n) >0.5 #popu means population
popu=popu*1 #pass from bolean to int

upper=np.array([]) #Matriz para mejores individuos

i=0

while limit<=stop_criteria:
    
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
dist=plotting(upper2)
