# -*- coding: utf-8 -*-
"""
Created on Fri May 15 18:02:10 2020

@author: user

"""
import numpy as np
import pickle
from estimator_classes_general import Model,LtspiceCalling,SimulationInfo
from sklearn.metrics import mean_squared_error



    
#%%---------------------FITNESS FUNCTION TRAF
def fitnessGeneral(ind_fl,**options):
    with open("simu_charac.pickle", "rb") as f:
        simdata= pickle.load(f)
    with open("measure.pickle", "rb") as f:
        measure = pickle.load(f)
    
    
    new_params={}
    j=0
    for key in simdata.parameters_target:
        new_params[key]=str(ind_fl[0,j])
        j+=1

     
    netlist=simdata.netlist_base_path
    code_list=list.copy(simdata.netlist_base)
    index_param=simdata.index_param
    for key in index_param:
        code_list[index_param[key]]=code_list[index_param[key]]+' '+new_params[key]+'\n'
    new_code=''.join(code_list)
    
    
    
     #%% Create and run new netlist
    batch_file=simdata.batch_file
    LtspiceCalling(batch_file,netlist,new_code,1)#0.5 seconds per simulation
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
        for i in range(0, len(measure.base)):
            rmse_array[i]=rmse_array[i]/measure.base[i]
            
        rmse_vector=rmse_array.tolist()
    #rmse norm vector
    
    rmse_norm=np.linalg.norm(rmse_vector)
    dist=-rmse_norm

    if options.get("models")=="true":
        return dist,measure,simulation_adjust
    else:
        return dist