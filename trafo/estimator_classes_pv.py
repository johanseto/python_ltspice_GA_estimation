# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 18:34:47 2020

@author: user
"""

import os
import time
import ltspice
import numpy as np
import pandas

##Principal class
class ModelPv:
    def __init__(self,voltage,current):
        self.v=voltage
        self.i=current
        
        
    def read_csv_signal(voltage_current_file):
        voltage_current_df = pandas.read_csv(voltage_current_file)
        voltage=np.array(voltage_current_df.iloc[0:,0])
        current=np.array(voltage_current_df.iloc[0:,1])
        measure= ModelPv(voltage,current)# -currentdepends on the sense of current coil
        return measure
    
    def unify_sim_model(measure,simulation):
        newsim_voltage=measure.v
        newsim_current=np.interp(np.ravel(measure.v),
                         np.ravel(simulation.v),np.ravel(simulation.i))
        simulation_adjust=ModelPv(newsim_voltage,newsim_current)
        return simulation_adjust
    
    def signals_caracteristics(voltage_current_file):
        measure=ModelPv.read_csv_signal(voltage_current_file)#Measure_model
        dv=measure.v[1]-measure.v[0]
        v_init=measure.v[0]
        v_last=measure.v[-1]
        

        
        simulation_vars=[dv,v_init,v_last]
        return measure,simulation_vars

# Calling ltspice class
class LtspiceCallingPv:
  # Create new netlist
    def __init__(self,netlist,code,seconds):
        f_id=open(netlist,'w')
        f_id.write(code)
        f_id.close()
        #Simulation
        os.system('ltspice_call.bat')
        time.sleep(seconds)
           
    
    def getData(sim_raw,variables):
        l=ltspice.Ltspice(os.path.dirname(__file__)+sim_raw)
# Make sure that the .raw file is located in the correct path
#l = ltspice.Ltspice('C:/Users/user/Desktop/python_spice/root_con/practice_optpy.raw' ) 
        tryParse(l) 
        v_sim = l.getData(variables[0])
        i_sim =l.getData(variables[1])
        simulation=ModelPv(v_sim, i_sim)
        os.system('ltspice_end.bat')
        return simulation
    

            
            
            

    
    
def tryParse(l): #Recursion function to avoid problem of parsing in the working directory
    try:
        l.parse()
    except:
        tryParse(l)
            
            
        




