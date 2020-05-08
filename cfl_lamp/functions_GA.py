  # -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 19:59:12 2020

@author: JohanV
"""
import numpy as np
import math

def evalPopu(popu,bit_n,rango,obj_fcn):
    global count
    pop_n=popu.shape[0]  #Numero de individuos
    fitness = np.zeros([pop_n,1])
    
    for count in range(0,pop_n):
        fitness[count]=evalEach(popu[count,:],bit_n,rango,obj_fcn)
    
    popu_eval=fitness
    return popu_eval


def evalEach(ind,bit_n,rango,obj_fcn):   #ind means individual
    
    var_n=int(len(ind)/bit_n)
    #Cicle to convert each individual from bits to decimal
    ind_fl=np.zeros([1,var_n])

    for i in range(0,var_n):
        ind_fl[0,i]=bit2Num(   ind[i*bit_n : (i+1)*bit_n]   ,rango[i,:])
        
    
    fit_val=eval(obj_fcn)(ind_fl)
    return fit_val
    



def bit2Num(bits,rango):
    integer=np.polyval(bits,2)
    num=integer*(rango[-1]-rango[0])/(2**len(bits) -1)  + rango[0]  
    return num

def upperData(upper,popu_eval,i,var_n,bit_n,rango,popu):
    
    upper=np.resize(upper,[i+1,var_n+1])#i+1 cause creating matrix need int val
    maxf=np.amax(popu_eval)
    maxf_index=np.array(np.where(popu_eval==np.amax(popu_eval))  )
    maxf_index=maxf_index[0,0]
    upper[i,0]=maxf  #Put the fcn_value
    for j in range (0,var_n):
        var=popu[maxf_index,j*bit_n:(j+1)*bit_n ]
        upper[i,j+1]=bit2Num(var,rango[j,:])
         
    return upper 
        
    
def nextPopu(popu,popu_eval,xover_rate,mut_rate):
    new_popu=np.copy(popu) #create copy, no a reference
    [popu_rows,popu_cols]=popu.shape
    #Elitism
    
    popu_eval2=np.copy(popu_eval)
     #Find the first in eval
    index1=np.array(np.where(popu_eval2==np.amax(popu_eval2)) )
    index1=index1[0,0]
    #Find the second
    popu_eval2[index1,0]=np.amin(popu_eval)
    index2=np.array(np.where(popu_eval2==np.amax(popu_eval2))  )
    index2=index2[0,0]
    
    new_popu[0:2,:]=popu[[index1,index2],:]
    
    #Rescale  the set function to be posotive
    fitness=popu_eval-np.amin(popu_eval)
    total=np.sum(fitness)
    
    if total==0:
        print('=====error==== \n Nule Individuals ')
        fitness=np.ones(popu_rows,1)/popu_rows #Sum is always 1
    else:
        fitness=fitness/total#Sum is 1
        
    cum_prob=np.cumsum(fitness)
    
    #Selection and crossing
    for i in range(1,popu_rows//2 ):#integer div,avoid two parents to elite
        p1=np.array(np.where(cum_prob-np.random.rand()>0))
        index_p1=int(np.array(p1[0,0]))
        parent1=popu[index_p1,:]
        
        p2=np.array(np.where(cum_prob-np.random.rand()>0))
        index_p2=int(np.array(p2[0,0]))
        parent2=popu[index_p2,:]
        
        if np.random.rand()<xover_rate:
            xover_point= int ( np.floor(np.random.rand()*(popu_cols)) )
           
            new_popu[i*2,:]=(  np.concatenate((parent1[0:xover_point],
            parent2[xover_point:popu_cols]),axis=0 )  )
           
            new_popu[i*2+1,:]=( np.concatenate( ([parent2[0:xover_point],
            parent1[xover_point:popu_cols]]),axis=0 ) )
             
    #Mutation criteria
    mut_matrix= np.random.rand(popu_rows,popu_cols) 
    mut_matrix=(mut_matrix < mut_rate)*1
    #new_popu=(popu^mut_matrix) #Xor operation,other way
    new_popu=(np.logical_xor(new_popu,mut_matrix))*1 #*1 to pass to log_int 
    #Restore elite members
    new_popu[0:2,:]=popu[[index1,index2],:]
    
    return new_popu
    
    
    
def fitnessSnubber(ind_fl):
    fitness=math.sqrt(ind_fl[0,0]/ind_fl[0,1])    
    return fitness
    