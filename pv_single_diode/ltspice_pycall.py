# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 21:57:25 2019

import librares

@author: user
"""

import os
import time
import ltspice
import matplotlib.pyplot as plt
import numpy as np
#  Useful paths :
#C:\Users\user\Desktop\matlab_spice
#C:\Program Files\LTC\LTspiceXVII\ltspicej.exe

#* C:\Users\user\Desktop\python_spice\practice.asc
# V1 source 0 SINE(0 10 10e3)
# R1 cap source 100
# C1 cap 0 1µ
# .tran 1m
# .backanno
# .end

## Setupp
netlist= r'C:\Users\user\Desktop\python_spice\practice_optpy.net'



#%% Python netlist modifications
#we dont need the path but its functional to have it
#dont forget that the paths needs the backslash character
v_amp='10'
v_freq='20e3'


code=('* C:\\Users\\user\\Desktop\\python_spice\\practice_optpy.asc \n'
'V1 source 0 SINE(0 '+ v_amp+' '+v_freq+') \n'
'R1 cap source 100 \n'
'C1 cap 0 1µ \n'
'.tran 2m \n'
'.backanno \n'
'.end \n')

#%% Create new netlist

f_id=open(netlist,'w')
f_id.write(code)
f_id.close()

#%%Simulation

os.system('ltspice_call.bat')
time.sleep(5)
os.system('ltspice_end.bat') 
#%%Get info

#l = ltspice.Ltspice('C:/Users/user/Desktop/python_spice/practice_optpy.raw' ) 
l=ltspice.Ltspice(os.path.dirname(__file__)+'/practice_optpy.raw')
# Make sure that the .raw file is located in the correct path
l.parse() 

time = l.getTime()
V_source = l.getData('V(source)')
V_cap = l.getData('V(cap)')
I_ser=l.getData('I(R1)')

#%% Plotting signals

plt.plot(time, V_source)
plt.plot(time, V_cap)
plt.plot(time, I_ser)
#plt.xlim((0, 1e-3))
#plt.ylim((-10, 10))
plt.grid()
plt.show()




