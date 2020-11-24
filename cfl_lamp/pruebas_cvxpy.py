# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 18:10:42 2020

@author: user
"""

import numpy as np


from sklearn.metrics import mean_squared_error
from estimator_classes import Model
from plot_file import plotting
from fitness_functions import fitnessCfl
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import cvxpy as cp
def metrics(fit_solution):
    dist,measure,simulation_adjust=fitnessCfl(fit_solution , models="true")
    mse = mean_squared_error(measure.i, simulation_adjust.i)
    rmse=np.sqrt(mse)
    
    rms_v = np.sqrt(np.mean(measure.v**2))
    rms_imeas = np.sqrt(np.mean(measure.i**2))
    rms_isim = np.sqrt(np.mean(simulation_adjust.i**2))
    norma2_diff = np.linalg.norm(measure.i-simulation_adjust.i)
    square_relative_error_fromIrms=rmse/rms_imeas
    relative_root_mean_square_error=rmse/sum(measure.i)
    metrics={'fitness':dist,'mse':mse,'rmse':rmse,
             'sqre':square_relative_error_fromIrms,
             'rrmse':relative_root_mean_square_error,
             'norma2Diff':norma2_diff}
    
    return metrics 

def function_ltspice_compare(x1,x2,x3):
    individual=np.array([[x1.value,x2.value,x3.value]])
    if individual[0,1] is None:
        sol=1000
    else:
        sol=metrics(individual)
        sol=sol['norma2Diff']
    return sol

#%%
# seed=np.array([[1300,12,20e-6]])
# alpha=0.1
# x_list,x_fitness=steeped_descent(seed, objective,alpha)
x0=[1300,12,20e-6]
n=1
x1=cp.Variable()
x2=cp.Variable()
x3=cp.Variable()

#cost=x1**2+x2**2
prob = cp.Problem(cp.Minimize(function_ltspice_compare(x1,x2,x3)),
                  [x1>=0,
                   x2>=0,
                   x3>=0]
                  
)

prob.solve(solver=cp.ECOS)
