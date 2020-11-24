# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 10:15:22 2020

@author: user
"""
import numpy as np


from sklearn.metrics import mean_squared_error
from estimator_classes import Model
from plot_file import plotting
from fitness_functions import fitnessCfl

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
#solution=[rd,r,c]=[R1,R2,C1]
fit_solution=np.array([[1.946521368734263888e+03,1.888197756923780801e+01,1.201735957885099540e-05]])
cost1=metrics(fit_solution)
cost1['norma2Diff']
#%%
fit_prueba=np.array([[1.946521368734263888e+03,1.888197756923780801e+01,12.00e-6]])
costprueba=metrics(fit_prueba)
norma2=costprueba['norma2Diff']

seed=np.array([[500,5,1e-6]])



#%%
seed=np.array([[5,5,5e-6]])
objective='norma2Diff'

def numerical_gradient(individual,fitness0,metric_objective):
    #moving one percent each variable and caluclte gradient
    gradient=np.zeros(np.shape(individual))
    #cero is about the individual
    for i in range(np.shape(individual)[1] ):
        test_individual=individual.copy()
        param0=individual[0,i]
        param1=param0+param0/10  #+1%
        test_individual[0,i]=param1
        fitness1=metrics(test_individual)[metric_objective]
        dx=param1-param0
        df=fitness1-fitness0
        gradient[0,i]=df/dx
        
    return gradient
fitness0=metrics(seed)[objective]
gradient_cal=numerical_gradient(seed,fitness0,objective)



#%%steepest descent

def steeped_descent(seed,objective,alpha):
    x=seed
    fitness=metrics(x)[objective]
    x_list=[]
    x_fitness=[]
    for i in range(30):
        x_list.append(x)
        x_fitness.append(fitness)
        fitness=metrics(x)[objective]
        gradient_cal=numerical_gradient(seed,fitness, objective)
        x=x-alpha*gradient_cal
    return(x_list,x_fitness)

