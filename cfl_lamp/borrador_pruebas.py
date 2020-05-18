# -*- coding: utf-8 -*-
"""
Created on Fri May 15 19:15:57 2020

@author: user
"""
import numpy as np
import pickle



from estimator_classes import Model
from fitness_functions import fitnessCfl
def fitnessSnubber(ind_fl,**options):
    fitness=np.sqrt(ind_fl[0]/ind_fl[1])    
    if options.get("models")=="true":
        a=4
        simulation_adjust=Model([0,2], [0,2],[0,2])
        return fitness,a,simulation_adjust
    else:
        return fitness


a=fitnessSnubber([10,2])
print(a)

b=fitnessSnubber([10,2],models="true")

# c=fitnessCfl(np.array([[1e3,600,1e-6]]))
# d=fitnessCfl(np.array([[1e3,600,1e-6]]) , models="true")



netlist= r'C:\Users\user\Desktop\python_spice\cfl_lamp\cfl_equiv.net'
sim_name='cfl_equiv'
sim_raw='/'+sim_name+'.raw'


# new reading files
voltage_file='voltage.csv'
current_file='current.csv'
measure=Model.read_csv_signal(voltage_file, current_file)#Measure_model
dt=measure.t[1]-measure.t[0]

# Find the delay of the signal in order to simulte it.
j=1
while (  not((measure.v[j]*measure.v[j-1]<0 and measure.v[j]>0)
           or(measure.v[j-1]==0 and measure.v[j]>0))       ) :
    j+=1
    
    
delay=measure.t[j]
phi_rad=delay*2*np.pi*60  #wt
phi_deg=phi_rad*180/np.pi  
phi_deg=-phi_deg  #negative in order to delay the simu signal

signal_peak=max(measure.v)
time_max=measure.t[-1]

#Simulation variables 
dt_sim=str(dt)
phi=str(phi_deg)
amp=str(signal_peak)
t_sim=str(time_max)

obj = measure
with open("obj.pickle", "wb") as f:
    pickle.dump(obj, f)
    

with open("obj.pickle", "rb") as f:
    obj2 = pickle.load(f)
    
obj2 = ['5','jhj','565']
with open("obj2.pickle", "wb") as f:
    pickle.dump(obj2, f)
    

with open("obj2.pickle", "rb") as f:
    obj2 = pickle.load(f)