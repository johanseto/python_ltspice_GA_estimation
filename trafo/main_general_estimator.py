# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 17:32:07 2021

@author: user
"""

import numpy as np
import pickle
from estimator_classes_general import Model,SimulationInfo
from functions_GA import evalPopu,upperData,nextPopu,geneticAlgoritm
from plot_file import plotting
import datetime

#%%Measure data recolection

signals_file='values_noise.csv'
n=4

signal_name=['v1','i1','v2','i2']
measure=Model.read_csv_signal(signals_file,4)
measure2=Model(measure.time,measure.signals[1:])
with open("measure.pickle", "wb") as f:
    pickle.dump(measure2, f)

#%%Pre process class to configure the case

sim_name='trafo_single'
sim_raw='/'+sim_name+'.raw'
netlist_path= r'C:\Users\user\Desktop\python_spice\trafo\trafo_single.net'
parameters=['R1','R2','L1','L2','L3']
signals2=['I(R1)','V(n004)','I(L4)']

simu_data=SimulationInfo(netlist_path,sim_raw,parameters,signals2,norm=True)


#%%----------------------------GA------------------------------
popu_size=100
xover_rate=0.98
mut_rate=0.4
bit_n=10
stop_criteria=20

fitness_fcn= 'fitnessGeneral'
var_n=5

rango=np.array([[1e-3,10],
                [1e-3,2000],
                [1e-6,2],
                [1e-6,2],
                [1e-6,2]])


popu,upper=geneticAlgoritm(fitness_fcn, var_n, rango, popu_size, xover_rate,
                           mut_rate, bit_n, stop_criteria)
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


#%%continue genetic process

popu2,upper2=geneticAlgoritm(fitness_fcn, var_n, rango, popu_size, xover_rate,
                           mut_rate, bit_n, stop_criteria,popu=popu)