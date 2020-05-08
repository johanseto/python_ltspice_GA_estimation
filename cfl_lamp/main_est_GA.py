# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 21:14:51 2020

@author: JohanV
"""
import numpy as np
from functions_GA import evalPopu,upperData,nextPopu
global a
C_oes=395e-12
popu_size=200
xover_rate=1.0
mut_rate=0.09
bit_n=16
limit=0
epsilon=1e-0

global E_i
global id_max
global C_s1
global L_s1

id_max=0.9
L_max=1000e-6
C_max=1000e-9

fitness_fcn= 'fitnessSnubber'
var_n=2
rango=np.array([[1e-9,L_max],[5*C_oes,C_max]])

popu=np.random.rand(popu_size,bit_n*var_n) >0.5 #popu means population
popu=popu*1

upper=np.array([]) #Matriz para mejores individuos

#popu_eval=evalPopu(popu,bit_n,rango,fitness_fcn) prueba de funcion  
i=0
k=0
while limit<=20:
    
    #popu_fit means popu fit evaluated
    popu_eval=evalPopu(popu,bit_n,rango,fitness_fcn)  
    upper=upperData(upper,popu_eval,i,var_n,bit_n,rango,popu)
    k+=1
    
    if i>=1:
        if upper[i,0]==upper[i-1,0]:
            limit+=1
        else:
            limit=0
          
    i+=1
    popu=nextPopu(popu,popu_eval,xover_rate,mut_rate)
    