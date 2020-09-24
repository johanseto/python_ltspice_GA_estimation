# -*- coding: utf-8 -*-
"""
Created on Fri May 15 18:02:10 2020

@author: user

"""
import numpy as np
import pickle
from estimator_classes import Model,LtspiceCalling
import matplotlib.pyplot as plt


def fitnessSnubber(ind_fl):
    fitness=np.sqrt(ind_fl[0,0]/ind_fl[0,1])    
    a=4
    return fitness,a
#%%---------------------FITNESS FUNCTION CFL
def fitnessCfl(ind_fl,**options):
    

    netlist= r'C:\Users\user\Desktop\python_spice\cfl_lamp\cfl_equiv.net'
    sim_name='cfl_equiv'
    sim_raw='/'+sim_name+'.raw'
    
    #adquire caracterstics from measure signal
    with open("measure.pickle", "rb") as f:
        measure = pickle.load(f)
    with open("simulation_vars.pickle", "rb") as f:
        simulation_vars = pickle.load(f)
        
    dt_sim=simulation_vars[0]
    phi=simulation_vars[1]
    amp=simulation_vars[2]
    t_sim=simulation_vars[3]

    #%% Python netlist modifications
    
    # r1=5.978e2
    # r2=60
    # c1=3.62e-6
    r1=ind_fl[0,0]
    r2=ind_fl[0,1]
    c1=ind_fl[0,2]
    
    
    
    r_1=str(r1)
    r_2=str(r2)
    c_1=str(c1)
    
    
    
    
    
    code=('* C:\\Users\\user\\Desktop\\python_spice\\cfl_lamp\\cfl_equiv.asc \n'
    'R1 N001 0 '+ r_1 +' \n'
    'D1 N003 N001 D \n'
    'D2 N004 N001 D \n'
    'D3 0 N003 D \n'
    'D4 0 N004 D \n'
    'C1 N001 0 '+ c_1 + ' \n'
    'R2 N002 N003 '+ r_2 + ' \n'
    'V1 N002 N004 SINE(0 ' +amp+' 60 0 0 '+phi+ ') \n'
    '.model D D \n'
    '.lib C:\\Users\\user\\Documents\\LTspiceXVII\\lib\\cmp\\standard.dio \n'
    '.options maxstep=1.25-5 \n'
    '.tran 0 '+t_sim+ ' \n'   # \' 0 '+ dt_sim +' \n'
    '.backanno \n'
    '.end \n')
    
    #%% Create and run new netlist
    
    LtspiceCalling(netlist,code,1)#0.5 seconds per simulation
    #%%Get info
    variables=['V(n002)','V(n004)','I(R2)']
    simulation=LtspiceCalling.getData(sim_raw, variables)# simulation_Model
    
    #%% unify the models 
    simulation_adjust=Model.unify_sim_model(measure,simulation)
    
    
    #Diference signals
    dist = np.linalg.norm(measure.i-simulation_adjust.i)
    dist=1/dist
    #     #%% plotting

    # plt.figure()
    # plt.subplot(211)
    # plt.plot(simulation_adjust.t, simulation_adjust.i) 
    # plt.plot(measure.t, measure.i)
    
    # plt.subplot(212)
    # plt.plot(simulation_adjust.t, simulation_adjust.v) 
    # plt.plot(measure.t, measure.v)
    
    #  Control the output of the function
    if options.get("models")=="true":
        return dist,measure,simulation_adjust
    else:
        return dist
    


