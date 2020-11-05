# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 15:23:06 2020

@author: user
"""

import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from pylab import cm
file='voltage_step_results.xlsx'
data=pd.read_excel(file)
results=data.to_numpy()

colors = cm.get_cmap('tab10', 10)
fig, axis = plt.subplots(2, 2)
axis1=axis[0,0]
axis2=axis[0,1]
axis3=axis[1,0]
axis4=axis[1,1]

tension=results[:,0]
fitness=results[:,1]
r=results[:,2]
rd=results[:,3]
c=results[:,4]

axis1.set_xlabel('Tension[V]')
axis1.set_ylabel('Distancia Euclidea')
axis1.set_title('Fitness')
axis1.plot(tension,fitness,marker='o') 
axis1.set_ylim(0,fitness.max()+1)

axis2.set_xlabel('Tension[V]')
axis2.set_ylabel('$R_d[\Omega]$')
axis2.set_title('$R_d$')
axis2.plot(tension,rd,marker='o') 
axis2.set_ylim(0,rd.max()+5)


axis3.set_xlabel('Tension[V]')
axis3.set_ylabel('$R[\Omega]$')
axis3.set_title('$R$')
axis3.plot(tension,r,marker='o') 
axis3.set_ylim(0,r.max()+100)



axis4.set_xlabel('Tension[V]')
axis4.set_ylabel('$C[\mu F]$')
axis4.set_title('$C$')
axis4.set_ylim(0,c.max()+1)
axis4.plot(tension,c,marker='o') 


#%%
plt.figure()
tensionmin=np.arange(70,50,-5)
#tensionmin=tensionmin.astype(np.float64)
#tensionmin=np.array([125,70])
#tension2=np.concatenate([tension,tensionmin])
y=29.23*tension-1449.4
plt.plot(tension,r,marker='o',label='Estimacion experimento') 
plt.ylim(0,r.max()+100)
plt.plot(tension,y,linestyle='--',label='R(v)=29.23v-1449.4',marker='*')
plt.xlabel('Tension[V]')
plt.ylabel('$R[\Omega]$')
plt.legend()