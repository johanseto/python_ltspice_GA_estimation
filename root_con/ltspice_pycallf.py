# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 21:57:25 2019

import librares

@author: user
"""

import os
#import time
import ltspice
import matplotlib.pyplot as plt
#import numpy as np
from spice_functions import newNetCall,getData
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
netlist= r'C:\Users\user\Desktop\python_spice\root_con\practice_optpy.net'



#%% Python netlist modifications
#we dont need the path but its functional to have it
#dont forget that the paths needs the backslash character
v_amp='1'
v_freq='20e3'


code=('* C:\\Users\\user\\Desktop\\python_spice\\root_con\\practice_optpy.asc \n'
'V1 source 0 SINE(0 '+ v_amp+' '+v_freq+') \n'
'R1 cap source 100 \n'
'C1 cap 0 1µ \n'
'.tran 2m \n'
'.backanno \n'
'.end \n')



#%% Create new netlist

newNetCall(netlist,code)
#%%Get info

dir=os.path.dirname(__file__)+'/practice_optpy.raw'
time,V,I=getData(dir)


#%% Plotting signals

#plt.plot(time, V_source)
plt.plot(time, V)
plt.plot(time, I)
#plt.xlim((0, 1e-3))
#plt.ylim((-10, 10))
plt.grid()
plt.show()




