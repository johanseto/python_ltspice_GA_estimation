# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 06:39:48 2020

@author: JohanV
"""
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

def steeped_descent(seed,objective,alpha,epsilon):
    x=seed
    x_list=[]
    x_fitness=[]
    k=0
    for i in range(200):
        fitness=metrics(x)[objective]
        x_list.append(x)
        x_fitness.append(fitness)
        gradient_cal=numerical_gradient(x,fitness, objective)
        x=x-alpha*gradient_cal
        if(len(x_fitness)>5):
            tol=np.average(x_fitness[-3:-1])-x_fitness[-1]
            if(np.abs(tol)<=epsilon):
                alpha=alpha*0.1
                k=k+1
                if(k==10):
                    break
    return(x_list,x_fitness)

def numerical_gradient(individual,fitness0,metric_objective):
    #moving one percent each variable and caluclte gradient
    gradient=np.zeros(np.shape(individual))
    #cero is about the individual
    for i in range(np.shape(individual)[1] ):
        test_individual=individual.copy()
        param0=individual[0,i]
        param1=param0+param0/100  #+1%
        test_individual[0,i]=param1
        fitness1=metrics(test_individual)[metric_objective]
        dx=param1-param0
        df=fitness1-fitness0
        gradient[0,i]=df/dx
    return gradient

def metrics(fit_solution):
    #r1*1000,r2*1,c1*1e^-6
    fit_solution_norm=np.array([fit_solution[0,:]*[1000,1,1e-6]])
    dist,measure,simulation_adjust=fitnessCfl(fit_solution_norm , models="true")
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


epsilon=0.02
objective='norma2Diff'

#%% alpha univalue
#r1*1000,r2*1,c1*1e^-6
seed=np.array([[1.3,12,20]])
alpha=0.1
x_list,x_fitness=steeped_descent(seed, objective,alpha,epsilon)
#%% alpha vector
seed=np.array([[1.3,12,20]])
epsilon=0.01
objective='norma2Diff'
alpha=np.array([[0.01,10,10]])
x_list2,x_fitness2=steeped_descent(seed, objective,alpha,epsilon)
 #%%continue
#x_list3,x_fitness3=steeped_descent(x_list2[-1], objective,alpha)
# #%%continue2
# alpha=np.array([[20,1,1e-6]])
# x_list3,x_fitness3=steeped_descent(x_list3[-1], objective,alpha)
#%%

import datetime
today=datetime.datetime.today()
today_str='{:%Y-%b-%d-%H_%M}'.format(today)
np.save('alpha_variable_params'+today_str+'.npy',x_list2)
np.save('alpha_variable_ftness'+today_str+'.npy',x_fitness2)


#%%plot'
import matplotlib.pyplot as plt
plt.plot(x_fitness2)
x_param0=[]
x_param1=[]
x_param2=[]
for ind in x_list2:
    x_param0.append(ind[0][0])
    x_param1.append(ind[0][1])
    x_param2.append(ind[0][2])

fig, axis = plt.subplots(2, 2)
axis1=axis[0,0]
axis2=axis[0,1]
axis3=axis[1,0]
axis4=axis[1,1]



axis1.plot(x_fitness2)
axis1.set_ylabel('Fitness')
axis1.set_xlabel('$iteración$ [i]')

axis2.plot(np.array(x_param0)*1000)
#axis5.title('Funcion fitness')
axis2.set_ylabel('$R1,R_d[\Omega]$')
axis2.set_xlabel('$iteración$ [i]')



axis3.plot(x_param1)
#axis3.title('Funcion fitness')
axis3.set_ylabel('$R2,R$ [$\Omega$]')
axis3.set_xlabel('$iteración$ [i]')

axis4.plot(x_param2)
#axis4.title('Funcion fitness')
axis4.set_ylabel('$C,C1$ [$uF$]')
axis4.set_xlabel('$iteración$ [i]')

    
#%% 
from plot_file import plotting 

plotting(x_list2[-1]*[1000,1,1e-6])