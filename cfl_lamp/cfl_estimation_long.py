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
'V1 N002 N004 SINE(0 177 60) \n'
'.model D D \n'
'.lib C:\\Users\\user\\Documents\\LTspiceXVII\\lib\\cmp\\standard.dio \n'
'.tran 200e-3 \n'
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
#%% Plotting signals

#plt.plot(time, v_1)
plt.plot(time, v_na-v_nb) 
plt.plot(time, i_in*1000)
#plt.xlim((0, 1e-3))
#plt.ylim((-10, 10))
plt.grid()
plt.show()

dt=[]
for i in range (1,len(time)):
    dt.append(time[i]-time[i-1] )

plt.figure()
plt.plot(dt)


#%% Data adquire from csv/xls

excel_data_df = pandas.read_excel('CFL.xlsx')
df=np.array(excel_data_df[6:])
time=df[:,0]
current=df[:,1]
measure= Modelo(time,[4,56,13,15],current)

