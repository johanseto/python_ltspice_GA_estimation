# -*- coding: utf-8 -*-
"""
Created on Fri May  8 18:03:28 2020

@author: user
"""
import pandas
import matplotlib.pyplot as plt
import numpy as np


class Modelo:
    def __init__(self,time,voltage,current):
        self.v=voltage
        self.i=current
        self.t=time


excel_data_df = pandas.read_excel('CFL.xlsx')

df=np.array(excel_data_df[6:])
time=df[:,0]
current=df[:,1]


dt=[]
for i in range (1,len(time)):
    dt.append( np.round(float(time[i])-float(time[i-1]),decimals=8 ))
    

plt.figure()
plt.plot(dt)

measure= Modelo(time,[4,56,13,15],current)
plt.figure()
plt.plot(measure.t,measure.i)

measure.v=59
# def readMeasuredSignals (filename):
#     excel_data_df = pandas.read_excel('CFL.xlsx')

#     df=np.array(excel_data_df[6:])
#     time=df[:,0]
#     current=df[:,1]
#     plt.plot(time,current)

#     dt=[]
#     for i in range (1,len(time)):                                                                                                                                                                 
#         dt.append( np.round(float(time[i])-float(time[i-1]),decimals=8 ))

                                                                                                    