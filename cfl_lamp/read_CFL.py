# -*- coding: utf-8 -*-
"""
Created on Fri May  8 18:03:28 2020

@author: user
"""
import pandas
import matplotlib.pyplot as plt
import numpy as np
excel_data_df = pandas.read_excel('CFL.xlsx')

df=np.array(excel_data_df[6:])
time=df[:,0]
current=df[:,1]
plt.plot(time,current)

dt=[]
for i in range (1,len(time)):
    dt.append( float(time[i])-float(time[i-1] ))
    

plt.figure()
plt.plot(dt)
