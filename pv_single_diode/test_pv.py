# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 10:19:09 2020

@author: JohanV
"""
import os
import time
import ltspice
import numpy as np
import pandas
import matplotlib.pyplot as plt
from estimator_classes_pv import ModelPv,LtspiceCallingPv
from fitness_functions import *

file='french_solar_cell.csv'
sim_name='pv'
sim_raw='/'+sim_name+'.raw'
measure=ModelPv.read_csv_signal(file)
#plt.plot(measure.v,measure.i)

simulation_vars=[0.5e-3,0,0.6]
dv_sim=str(simulation_vars[0])
v_init=str(simulation_vars[1])
v_last=str(simulation_vars[2])

ind_fl=np.array([[52.4768,0.0367251,0.760849,1.43,33,0.29815e-6]])
r1=ind_fl[0,0]#Rshunt
r2=ind_fl[0,1]#Rserie
ilambda=ind_fl[0,2] #ilambda
n=ind_fl[0,3]#emission coeef
temp=ind_fl[0,4]#temperature
isat=ind_fl[0,5]#saturation current



r_1=str(r1)
r_2=str(r2)
i_lambda=str(ilambda)
n_s=str(n)
temp_work=str(temp)
i_sat=str(isat)    


netlist= r'C:\Users\user\Desktop\python_spice\pv_single_diode\pv.net'


code=('* C:\\Users\\user\\Desktop\\python_spice\\pv_single_diode\\pv.asc \n'
'R1 N001 0 '+r_1 +' \n'
'R2 N001 N002 '+r_2 +' \n'
'D1 N001 0 DPV \n'
'V1 N002 0 0 \n'
'I1 0 N001 '+i_lambda +' \n'
'.model DPV D(Is='+i_sat+' N='+n_s+' Tnom='+temp_work+') \n'
'.lib C:\\Users\\user\\Documents\\LTspiceXVII\\lib\\cmp\\standard.dio \n'
'.dc V1 '+v_init+' '+v_last+' '+dv_sim+ '\n'
'.backanno \n'
'.end \n ')
    
    #%% Create and run new netlist
    

LtspiceCallingPv(netlist,code,1)



variables=['V(n002)','I(V1)']
simulation=LtspiceCallingPv.getData(sim_raw, variables)# simulation_Model


simulation_adjust=ModelPv.unify_sim_model(measure,simulation)


#Diference signals
dist = np.linalg.norm(measure.i-simulation_adjust.i)
dist=1/dist

from sklearn.metrics import mean_squared_error
mse = mean_squared_error(measure.i, simulation_adjust.i)
rmse=np.sqrt(mse)

rms_v = np.sqrt(np.mean(measure.v**2))
rms_imeas = np.sqrt(np.mean(measure.i**2))
rms_isim = np.sqrt(np.mean(simulation_adjust.i**2))

square_relative_error_fromIrms=rmse/rms_imeas
relative_root_mean_square_error=rmse/sum(measure.i)






#%% new reading files

voltage_current_file=file


measure,simulation_vars=ModelPv.signals_caracteristics(voltage_current_file)

#save classes to functions
with open("measure.pickle", "wb") as f:
    pickle.dump(measure, f)

with open("simulation_vars.pickle", "wb") as f:
    pickle.dump(simulation_vars, f)
    
ind_fl=np.array([[52.4768,0.0367251,0.760849,1.43,33,0.29815e-6]])

dist2,measure,simulation_adjust=fitnessPv(ind_fl , models="true")

mse2 = mean_squared_error(measure.i, simulation_adjust.i)
rmse2=np.sqrt(mse)

rms_v = np.sqrt(np.mean(measure.v**2))
rms_imeas2 = np.sqrt(np.mean(measure.i**2))
rms_isim2 = np.sqrt(np.mean(simulation_adjust.i**2))

square_relative_error_fromIrms2=rmse2/rms_imeas2
relative_root_mean_square_error2=rmse2/sum(measure.i)