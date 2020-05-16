# -*- coding: utf-8 -*-
"""
Created on Fri May 15 19:15:57 2020

@author: user
"""
import numpy as np
from estimator_classes import Model
from fitness_functions import fitnessCfl
def fitnessSnubber(ind_fl,**options):
    fitness=np.sqrt(ind_fl[0]/ind_fl[1])    
    if options.get("models")=="true":
        a=4
        simulation_adjust=Model([0,2], [0,2],[0,2])
        return fitness,a,simulation_adjust
    else:
        return fitness


a=fitnessSnubber([10,2])
print(a)

b=fitnessSnubber([10,2],models="true")

c=fitnessCfl(np.array([[1e3,600,1e-6]]))
d=fitnessCfl(np.array([[1e3,600,1e-6]]) , models="true")