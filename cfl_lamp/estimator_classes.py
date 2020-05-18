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
class Model:
    def __init__(self,time,voltage,current):
        self.v=voltage
        self.i=current
        self.t=time
        
    def read_csv_signal(voltage_file,current_file):
        voltage_data_df = pandas.read_csv(voltage_file,skiprows=4)
        current_data_df = pandas.read_csv(current_file,skiprows=4)
        mid=np.where(voltage_data_df.iloc[:,0]==0)
        mid=mid[0][0]
        time=time=np.array(voltage_data_df.iloc[mid:,0])
        voltage=np.array(voltage_data_df.iloc[mid:,1])
        current=np.array(current_data_df.iloc[mid:,1])
        measure= Model(time,voltage,-current)# -currentdepends on the sense of current coil
        return measure
    
    def unify_sim_model(measure,simulation):
        newsim_time=measure.t
        newsim_voltage=np.interp(np.ravel(measure.t),
                         np.ravel(simulation.t),np.ravel(simulation.v))
        newsim_current=np.interp(np.ravel(measure.t),
                         np.ravel(simulation.t),np.ravel(simulation.i))
        simulation_adjust=Model(newsim_time, newsim_voltage,newsim_current)
        return simulation_adjust
    
    def signals_caracteristics(voltage_file,current_file):
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
        
        simulation_vars=[dt_sim,phi,amp,t_sim]
        return measure,simulation_vars

# Calling ltspice class
class LtspiceCalling:
  # Create new netlist
    def __init__(self,netlist,code,seconds):
        f_id=open(netlist,'w')
        f_id.write(code)
        f_id.close()
        #Simulation
        os.system('ltspice_call.bat')
        time.sleep(seconds)
        os.system('ltspice_end.bat')   
    
    def getData(sim_raw,variables):
        l=ltspice.Ltspice(os.path.dirname(__file__)+sim_raw)
# Make sure that the .raw file is located in the correct path
#l = ltspice.Ltspice('C:/Users/user/Desktop/python_spice/root_con/practice_optpy.raw' ) 
        l.parse() 
        time = l.getTime()
        v_na = l.getData(variables[0])
        v_nb =l.getData(variables[1])
        i_in=l.getData(variables[2])
        simulation=Model(time, v_na-v_nb, i_in)
        return simulation





