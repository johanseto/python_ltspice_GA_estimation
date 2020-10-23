# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 15:10:25 2020

@author: JohanV
"""
import os
import ltspice
import matplotlib.pyplot as plt

from spice_functions import newNetCall, getData

##Setup
netlist= r'C:\Users\user\Desktop\python_spice\cfl_lamp\cfl_equiv.net'


#%% Python netlist modifications

r1=5.978e3
r2=49.6
c1=3.62e-6

r_1=str(r1)
r_2=str(r2)
c_1=str(c1)



code= ('* C:\\Users\\user\\Desktop\\python_spice\\cfl_lamp\\cfl_equiv.asc \n'
'R1 N001 N004 '+ r_1 +' \n'
'D1 N003 N001 D \n'
'D2 0 N001 D \n'
'D3 N004 N003 D \n'
'D4 N004 0 D \n'
'C1 N001 N004 '+ c_1 + '\n'
'R2 N002 N003 '+ r_2 + ' \n'
'V1 N002 0 SINE(0 177 60)\n'
'.model D D \n'
'.lib C:\\Users\\user\\Documents\\LTspiceXVII\\lib\\cmp\\standard.dio \n'
'.tran 200e-3 \n'
'.backanno \n'
'.end \n')


#%% Create new netlist

newNetCall(netlist,code)
#%%Get info

dir=os.path.dirname(__file__)+'/cfl_equiv.raw'
variables=['V(n001)','V(n002)','I(R2)']
time,V,I=getData(dir)


#%% Plotting signals

#plt.plot(time, V_source)
plt.plot(time, V)
plt.plot(time, I)
#plt.xlim((0, 1e-3))
#plt.ylim((-10, 10))
plt.grid()
plt.show()