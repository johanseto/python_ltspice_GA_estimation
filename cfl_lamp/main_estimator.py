# -*- coding: utf-8 -*-
"""
Created on Thu May 14 15:51:30 2020

@author: user
"""

import os
import ltspice
import matplotlib.pyplot as plt
import pandas 
import numpy as np

from spice_functions import newNetCall
##Setup
netlist= r'C:\Users\user\Desktop\python_spice\cfl_lamp\cfl_equiv.net'
sim_name='cfl_equiv'
sim_raw='/'+sim_name+'.raw'

##Principal class
class Modelo:
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
        measure= Modelo(time,voltage,-current)# -currentdepends on the sense of current coil
        return measure

#%% new reading files
voltage_file='voltage.csv'
current_file='current.csv'
measure=Modelo.read_csv_signal(voltage_file, current_file)
dt=measure.t[1]-measure.t[0]

# Find the delay of the singal in order to simulte it.
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

#%% Python netlist modifications

r1=5.978e2
r2=60
c1=3.62e-6
dt_sim=str(dt)
r_1=str(r1)
r_2=str(r2)
c_1=str(c1)
phi=str(phi_deg)
amp=str(signal_peak)
t_sim=str(time_max)




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
'.tran 0 '+t_sim+' 0 '+ dt_sim + ' \n'
'.backanno \n'
'.end \n')

#%% Create new netlist

newNetCall(netlist,code)
#%%Get info

#l = ltspice.Ltspice('C:/Users/user/Desktop/python_spice/root_con/practice_optpy.raw' ) 
l=ltspice.Ltspice(os.path.dirname(__file__)+sim_raw)
# Make sure that the .raw file is located in the correct path
l.parse() 

time = l.getTime()
#v_1 = l.getData('V(V1)')
v_na = l.getData('V(n002)')
v_nb =l.getData('V(n004)')
i_in=l.getData('I(R2)')
simulation=Modelo(time, v_na-v_nb, i_in)


#%% unify the models 


newsim_time=measure.t
newsim_voltage=np.interp(np.ravel(measure.t),
                         np.ravel(simulation.t),np.ravel(simulation.v))
newsim_current=np.interp(np.ravel(measure.t),
                         np.ravel(simulation.t),np.ravel(simulation.i))



simulation_adjust=Modelo(newsim_time, newsim_voltage,newsim_current)
#%% plotting

plt.figure()
plt.subplot(211)
plt.plot(simulation_adjust.t, simulation_adjust.i) 
plt.plot(measure.t, measure.i)

plt.subplot(212)
plt.plot(simulation_adjust.t, simulation_adjust.v) 
plt.plot(measure.t, measure.v)
