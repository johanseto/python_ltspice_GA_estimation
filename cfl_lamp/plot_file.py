# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 11:41:43 2020

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Thu May 14 15:51:30 2020

@author: user
"""
import matplotlib.pyplot as plt
import numpy as np
from estimator_classes import Model

from fitness_functions import fitnessCfl

from pylab import cm
import matplotlib as mpl







#%%
def plotting(fit_solution):
    dist,measure,simulation_adjust=fitnessCfl(fit_solution , models="true")

    
    
    colors = cm.get_cmap('tab10', 10)
    f, (ax2, ax1) = plt.subplots(2, 1)
    ax1.plot(simulation_adjust.t*1e3, simulation_adjust.i,linewidth=3, color=colors(0), 
             label=' i-simulada')
    ax1.plot(measure.t*1e3, measure.i,linewidth=3, color=colors(1), label='i- medida')
    ax2.set_title('Resultados')
    ax1.set_xlim(0, measure.t[-1]*1e3)
    ax1.set_ylim(min(measure.i)-0.1, max(measure.i)+0.1)
    # ax1.set_xlabel('Iteracion(i)')
    ax1.set_xlabel(r'Tiempo(ms)', labelpad=10)
    ax1.set_ylabel(r'Corriente(A)', labelpad=10)
    # ax1.spines['right'].set_visible(False)
    # ax1.spines['top'].set_visible(False)
    

    ax1.legend(bbox_to_anchor=(0.78, 0.8), loc=10, frameon=True, fontsize=14)
    
    ax2.plot(simulation_adjust.t*1e3, simulation_adjust.v, linewidth=3,color=colors(0),
             label='v-simulada')
    ax2.plot(measure.t*1e3, measure.v, linewidth=3,color=colors(1),
             label='v-medida')
    
    ax2.set_xlim(0, measure.t[-1]*1e3)
    ax2.set_ylim(min(measure.v)-10, max(measure.v)+10)
    ax2.set_ylabel(r'Tension(V)', labelpad=10)
    ax2.set_xlabel(r'Tiempo(ms)', labelpad=10)
    ax2.legend(bbox_to_anchor=(0.78, 0.8), loc=10, frameon=True, fontsize=14)
    
    
    
    
    
    # plt.figure()
    # plt.subplot(211)
    # plt.plot(simulation_adjust.t, simulation_adjust.i) 
    # plt.plot(measure.t, measure.i)
    
    # plt.subplot(212)
    # plt.plot(simulation_adjust.t, simulation_adjust.v) 
    # plt.plot(measure.t, measure.v)
    
    from sklearn.metrics import mean_squared_error
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

