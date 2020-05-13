# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 15:10:25 2020

@author: JohanV
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

#%% Python netlist modifications

r1=5.978e3
r2=49.6
c1=3.62e-6

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
'V1 N002 N004 SINE(0 177 60 0 0 90) \n'
'.model D D \n'
'.lib C:\\Users\\user\\Documents\\LTspiceXVII\\lib\\cmp\\standard.dio \n'
'.options maxstep=1.25-5 \n'
'.tran 0 512e-4 0 0.417e-6 \n'
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
#%% Plotting signals

#plt.plot(time, v_1)
plt.plot(simulation.t, simulation.v) 
plt.plot(time, simulation.i*1000)
#plt.xlim((0, 1e-3))
#plt.ylim((-10, 10))
plt.grid()
plt.show()

dt=[]
for i in range (1,len(time)):
    dt.append(np.round(time[i]-time[i-1],decimals=8) )

plt.figure()
plt.plot(dt)
plt.axis([0 ,495,1.24e-7,100e-5])

#%% Data adquire from csv/xls

excel_data_df = pandas.read_excel('CFL.xlsx')
df=np.array(excel_data_df[6:])
time=df[4095:,0]
time=time.astype(float)
current=df[4095:,1]
current=current.astype(float)
measure= Modelo(time,[4,56,13,15],current)


#%% unify the models 

if len(simulation.t)>len(measure.t):
    newsim_time=measure.t
    newsim_voltage=np.interp(np.ravel(measure.t),
                             np.ravel(simulation.t),np.ravel(simulation.v))
    newsim_current=np.interp(np.ravel(measure.t),
                             np.ravel(simulation.t),np.ravel(simulation.i))



simulation_adjust=Modelo(newsim_time, newsim_voltage,newsim_current)
#%% plotting

plt.figure()
plt.subplot(211)
plt.plot(simulation.t, simulation.i) 
plt.subplot(212)
plt.plot(measure.t, measure.i)
plt.figure()
plt.plot(measure.t, measure.i)
plt.plot(measure.t, simulation_adjust.i)

#%% new readgin files
voltage_data_df = pandas.read_csv('voltage.csv',skiprows=4)
current_data_df = pandas.read_csv('current.csv',skiprows=4)
time=time=np.array(voltage_data_df.iloc[4095:,0])
voltage=np.array(voltage_data_df.iloc[4095:,1])
current=np.array(current_data_df.iloc[4095:,1])


measure120= Modelo(time,voltage,current)

plt.figure()
plt.subplot(211)
plt.plot(simulation.t, simulation.v) 
plt.plot(simulation.t, simulation.i*1000)
plt.subplot(212)
plt.plot(measure120.t, measure120.v)
plt.plot(measure120.t, -100*measure120.i)
