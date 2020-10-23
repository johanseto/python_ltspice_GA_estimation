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
class ModelTrafo:
    def __init__(self,time,voltage1,current1,voltage2,current2):
        self.t=time
        self.v1=voltage1
        self.i1=current1
        self.v2=voltage2
        self.i2=current2
        
    def read_csv_signal(trafo_signals_file):
        voltage_current_df = pandas.read_csv(trafo_signals_file)
        time=np.array(voltage_current_df.iloc[0:,0])
        voltage1=np.array(voltage_current_df.iloc[0:,1])
        current1=np.array(voltage_current_df.iloc[0:,2])
        voltage2=np.array(voltage_current_df.iloc[0:,3])
        current2=np.array(voltage_current_df.iloc[0:,4])
        measure= ModelTrafo(time,voltage1,current1,voltage2,current2)# -currentdepends on the sense of current coil
        return measure
    
    def unify_sim_model(measure,simulation):
        newsim_time=measure.t
        newsim_voltage1=np.interp(np.ravel(measure.t),
                         np.ravel(simulation.t),np.ravel(simulation.v1))
        newsim_current1=np.interp(np.ravel(measure.t),
                         np.ravel(simulation.t),np.ravel(simulation.i1))
        newsim_voltage2=np.interp(np.ravel(measure.t),
                         np.ravel(simulation.t),np.ravel(simulation.v2))
        newsim_current2=np.interp(np.ravel(measure.t),
                         np.ravel(simulation.t),np.ravel(simulation.i2))
        simulation_adjust=ModelTrafo(newsim_time, newsim_voltage1,newsim_current1,
                                newsim_voltage2,newsim_current2)
        return simulation_adjust
    
    def signals_caracteristics(voltage_current_file):
        measure=ModelTrafo.read_csv_signal(voltage_current_file)#Measure_model
        dv=measure.v[1]-measure.v[0]
        v_init=measure.v[0]
        v_last=measure.v[-1]
        

        
        simulation_vars=[dv,v_init,v_last]
        return measure,simulation_vars

# Calling ltspice class
class LtspiceCallingTrafo:
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
        time=l.getTime()
        v_1 = l.getData(variables[0])
        i_1 =l.getData(variables[1])
        v_2=l.getData(variables[2])
        i_2=l.getData(variables[3])
        simulation=ModelTrafo(time,v_1,i_1,v_2,i_2)
        os.system('ltspice_end.bat')
        return simulation
    

            
            
            

    
    
def tryParse(l): #Recursion function to avoid problem of parsing in the working directory
    try:
        l.parse()
    except:
        tryParse(l)
            
            
        




