# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 09:02:23 2020

@author: user
"""

import numpy as np


from sklearn.metrics import mean_squared_error
from estimator_classes import Model
from plot_file import plotting
from fitness_functions import fitnessCfl
import matplotlib.pyplot as plt
from scipy.optimize import minimize
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

def function_ltspice_compare(x):
    individual=np.array([x])
    sol=metrics(individual)
    return sol['norma2Diff']

#%%
# seed=np.array([[1300,12,20e-6]])
# alpha=0.1
# x_list,x_fitness=steeped_descent(seed, objective,alpha)
x0=[1300,12,20e-6]
bnds = ((0, None), (0, None),(0,None))
res_nelder_mead = minimize(function_ltspice_compare, x0, method='Nelder-Mead',bounds=bnds )

#%% equential Least SQuares Programming to minimize a function 
res_SLSQP = minimize(function_ltspice_compare, x0, method='SLSQP',bounds=bnds )

#%% powell
res_powell = minimize(function_ltspice_compare, x0, method='Powell',bounds=bnds )  #C negativo wtf  no bounds xd
#%%conjugate gradient
x0=[1300,12,20e-6]

bnds = ((0, None), (0, None),(0,None))
res_CG = minimize(function_ltspice_compare, x0, method='CG',bounds=bnds )

#%%truncated newton algorithm
x0=[1300,12,20e-6]

bnds = ((0, None), (0, None),(0,None))
res_TNC= minimize(function_ltspice_compare, x0, method='TNC',bounds=bnds )

#%%L-BFGS-B algorithm
x0=[1300,12,20e-6]

bnds = ((0+1e-10, None), (0+1e-10, None),(0+1e-12,None))
res_LBGGSB= minimize(function_ltspice_compare, x0, method='L-BFGS-B',bounds=bnds)