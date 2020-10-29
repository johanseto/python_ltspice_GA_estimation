# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 07:25:26 2020
@author: JohanV
"""
from pylab import cm
import matplotlib as mpl
import matplotlib.font_manager as fm
from fitness_functions import fitnessPv
import numpy as np
import matplotlib.pyplot as plt
#%% plotting
#fit_solution=np.array([upper[-1,:]])
def plotting(upper):
    fit_solution=np.array([upper[-1,1:]])
    dist,measure,simulation_adjust=fitnessPv(fit_solution , models="true")

    
    colors = cm.get_cmap('tab10', 10)
    
    plt.plot(simulation_adjust.v, simulation_adjust.i, color=colors(0), 
             label=' i-simulada',alpha=0.5)
    plt.plot(measure.v, measure.i, color=colors(1), label='i- medida')
    plt.title('Resultados')
   
    plt.xlabel('Tension')
    
    plt.ylabel(r'Corriente(A)', labelpad=10)

    return dist