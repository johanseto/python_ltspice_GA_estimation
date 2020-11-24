# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 10:55:15 2020

@author: user
"""
import numpy as np


from sklearn.metrics import mean_squared_error
from estimator_classes import Model
from plot_file import plotting
from fitness_functions import fitnessCfl
import matplotlib.pyplot as plt
#%%
def steeped_descent(seed,objective,alpha):
    x=seed
    x_list=[]
    x_fitness=[]
    for i in range(1500):
        fitness=metrics(x)[objective]
        x_list.append(x)
        x_fitness.append(fitness)
        gradient_cal=numerical_gradient(x,fitness, objective)
        x=x-alpha*gradient_cal
    return(x_list,x_fitness)

def numerical_gradient(individual,fitness0,metric_objective):
    #moving one percent each variable and caluclte gradient
    gradient=np.zeros(np.shape(individual))
    #cero is about the individual
    for i in range(np.shape(individual)[1] ):
        test_individual=individual.copy()
        param0=individual[0,i]
        param1=param0+param0/10  #+10%
        test_individual[0,i]=param1
        fitness1=metrics(test_individual)[metric_objective]
        dx=param1-param0
        df=fitness1-fitness0
        gradient[0,i]=df/dx
        
    return gradient

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
#%%steepest descent
seed=np.array([[500,5,1e-6]])


epsilon=3.7
objective='norma2Diff'

#%% alpha univalue
seed=np.array([[1300,12,20e-6]])
alpha=0.1
x_list,x_fitness=steeped_descent(seed, objective,alpha)
#%% alpha vector
alpha=np.array([[10,1,0.1e-10]])
x_list2,x_fitness2=steeped_descent(seed, objective,alpha)
#%%continue
x_list3,x_fitness3=steeped_descent(x_list2[-1], objective,alpha)
#%%continue2
alpha=np.array([[20,1,1e-6]])
x_list3,x_fitness3=steeped_descent(x_list3[-1], objective,alpha)