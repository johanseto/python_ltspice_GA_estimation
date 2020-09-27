# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 18:42:18 2020

@author: JohanV
"""
from fitness_functions import fitnessPv
import numpy as np
ind_fl=np.array([[52.4768,0.0367251,0.760849,1.43,33,0.29815e-6]])
dist2=fitnessPv(ind_fl)
voltage_current_file=file


measure,simulation_vars=ModelPv.signals_caracteristics(voltage_current_file)

#save classes to functions
with open("measure.pickle", "wb") as f:
    pickle.dump(measure, f)

with open("simulation_vars.pickle", "wb") as f:
    pickle.dump(simulation_vars, f)