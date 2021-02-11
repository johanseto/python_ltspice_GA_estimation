# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 18:57:25 2021

@author: user
"""

import numpy as np
import pickle
from estimator_classes_general import Model,LtspiceCalling,SimulationInfo
from sklearn.metrics import mean_squared_error

ind_fl=np.array([[0,1,1000,0.01,1,0.01]])

with open("simu_charac.pickle", "rb") as f:
    simdata= pickle.load(f)
with open("measure.pickle", "rb") as f:
    measure = pickle.load(f)


new_params={}
j=0
for key in simdata.parameters_target:
    new_params[key]=str(ind_fl[0,j])
    j+=1
 # for j in range(0,len(ind_fl[0,:])):
 #     param.append(str(ind_fl[0,j]))
 
 # r1=str(ind_fl[0,0])
 # r2=str(ind_fl[0,1])
 # L1=str(ind_fl[0,2])
 # L2=str(ind_fl[0,3])
 # L3=str(ind_fl[0,4])
 
 
netlist=simdata.netlist_base_path
code_list=list.copy(simdata.netlist_base)
index_param=simdata.index_param
for key in index_param:
    code_list[index_param[key]]=code_list[index_param[key]]+' '+new_params[key]+'\n'
new_code=''.join(code_list)



 #%% Create and run new netlist
 
LtspiceCalling(netlist,new_code,1)#0.5 seconds per simulation
variables=simdata.signals_target
sim_raw=simdata.sim_raw
simulation=LtspiceCalling.getDataClosing(sim_raw, variables)# simulation_Model
 
#%% unify the models 
simulation_adjust=Model.unify_sim_model(measure,simulation)
 #Diference signals
 #%%
 #dist = np.linalg.norm(measure.i-simulation_adjust.i)
 #dist=np.linalg.norm(measure.i*measure.v-simulation_adjust.i*simulation_adjust.v)
 #lelement elemnt milpication for power
# base_v1=max(measure.v1)-min(measure.v1)
rmse_vector=[]

for i in range(0,len(measure.signals)):
    rmse_vector.append(np.sqrt(mean_squared_error(measure.signals[i],
                                          simulation_adjust.signals[i])))
# rmse_v1 = np.sqrt(mean_squared_error(measure.v1,
                             # simulation_adjust.v1))/base_v1

if (simdata.norm):
    
    rmse_array=np.array(rmse_vector)
    for i in range( len(measure.base)):
        rmse_array[i]=rmse_array[i]/measure.base[i]
        
    rmse_vector=rmse_array.tolist()
#rmse calculation
 

rmse_norm=np.linalg.norm(rmse_vector)
dist=-rmse_norm




#%%
# close_file='ltspice_call_base.bat'
# f_id=open(close_file,'r')
# fid_string=f_id.read()
# f_id.close()



# index=simu_data.netlist_base_path.rfind('\\')
# name_netlist=simu_data.netlist_base_path[index+1:]

# new_batch=fid_string[:-1]+name_netlist

# batch_path='ltspice_call_'+name_netlist[:-4]+'.bat'
# f_id=open(batch_path,'w')
# f_id.write(new_batch)
# f_id.close()


# #%%
# import ltspice
# import os
# sim_raw='\\trafo_single_sim.raw'
# l=ltspice.Ltspice(os.path.dirname(__file__)+sim_raw)



#%%
from fitness_general import fitnessGeneral

sim_name='trafo_single'
sim_raw='/'+sim_name+'.raw'
netlist_path= r'C:\Users\user\Desktop\python_spice\trafo\trafo_single.net'


parameters=['R1','R2','L1','L2','L3']

#signals=['V(n001)','I(R1)','V(n004)','I(L4)']

signals2=['I(R1)','V(n004)','I(L4)']
simu_data=SimulationInfo(netlist_path,sim_raw,parameters,signals2,norm=True)

prueba=np.array([[1,1000,0.01,1,0.01]])

dist1= fitnessGeneral(prueba)


simu_data=SimulationInfo(netlist_path,sim_raw,parameters,signals2)
#simu_data.netlistGen(netlist_path,parameters)

dist2= fitnessGeneral(prueba)
a,b,c=fitnessGeneral(prueba,models="true")