# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 07:25:26 2020

@author: JohanV
"""
from pylab import cm
import matplotlib as mpl
import matplotlib.font_manager as fm
from fitness_general import fitnessGeneral
import numpy as np
import matplotlib.pyplot as plt
#%% plotting
#fit_solution=np.array([upper[-1,:]])
def plotting(upper):
    fit_solution=np.array([upper[-1,1:]])
    dist,measure,simulation_adjust=fitnessGeneral(fit_solution , models="true")

    
    colors = cm.get_cmap('tab10', 10)
    f, (ax1, ax2) = plt.subplots(2, 1)
    ax1.plot(simulation_adjust.t, simulation_adjust.i1,linewidth=3, color=colors(0), 
             label=' i-simulada')
    ax1.plot(measure.t, measure.i1,linewidth=3, color=colors(1), label='i- medida')
    ax1.set_title('Resultados')
    # ax1.set_xlim(0, measure.t[-1])
    # ax1.set_ylim(min(measure.v1)-0.1, max(measure.i1)+0.1)
    # ax1.set_xlabel('Iteracion(i)')
    
    ax1.set_ylabel(r'Corriente(A)', labelpad=10)
    # ax1.spines['right'].set_visible(False)
    # ax1.spines['top'].set_visible(False)
    # ax1.xaxis.set_tick_params(which='major', size=10, width=2, direction='in')
    # ax1.xaxis.set_tick_params(which='minor', size=7, width=2, direction='in')
    # ax1.yaxis.set_tick_params(which='major', size=10, width=2, direction='in')
    # ax1.yaxis.set_tick_params(which='minor', size=7, width=2, direction='in')
    # ax1.grid(True)
    
    # ax1.xaxis.set_major_locator(mpl.ticker.MultipleLocator(1/120))
    # ax1.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(1/240))
    # ax1.yaxis.set_major_locator(mpl.ticker.MultipleLocator(max(measure.i)/4  ))
    # ax1.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(max(measure.i)/2  ))
    # ax1.legend(bbox_to_anchor=(0.78, 0.8), loc=10, frameon=True, fontsize=14)
    
    ax2.plot(simulation_adjust.t, simulation_adjust.v1, linewidth=3,color=colors(0),
             label='v-simulada')
    ax2.plot(measure.t, measure.v1, linewidth=3,color=colors(1),
             label='v-medida')
    
    # ax2.set_xlim(0, measure.v1[-1])
    # ax2.set_ylim(min(measure.v1)-10, max(measure.v)+10)
    # ax2.set_ylabel(r'Tension(V)', labelpad=10)
    # ax2.xaxis.set_tick_params(which='major', size=10, width=2, direction='in')
    # ax2.xaxis.set_tick_params(which='minor', size=7, width=2, direction='in')
    # ax2.yaxis.set_tick_params(which='major', size=10, width=2, direction='in')
    # ax2.yaxis.set_tick_params(which='minor', size=7, width=2, direction='in')
    # ax2.grid(True)
    
    # ax2.xaxis.set_major_locator(mpl.ticker.MultipleLocator(1/120))
    # ax2.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(1/240))
    # ax2.yaxis.set_major_locator(mpl.ticker.MultipleLocator(50))
    # ax2.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(25))
    # ax2.legend(bbox_to_anchor=(0.78, 0.8), loc=10, frameon=True, fontsize=14)
    
    
    
    
    
    plt.figure()
    plt.subplot(221)
    plt.plot(simulation_adjust.t, simulation_adjust.v1) 
    plt.plot(measure.t, measure.v1)
    
    plt.subplot(222)
    plt.plot(simulation_adjust.t, simulation_adjust.v2) 
    plt.plot(measure.t, measure.v2)
    
    plt.subplot(223)
    plt.plot(simulation_adjust.t, simulation_adjust.i1) 
    plt.plot(measure.t, measure.i1)
    
    plt.subplot(224)
    plt.plot(simulation_adjust.t, simulation_adjust.i2) 
    plt.plot(measure.t, measure.i2)
    
    
    from sklearn.metrics import mean_squared_error
    mse = mean_squared_error(measure.i1, simulation_adjust.i1)
    rmse=np.sqrt(mse)
    
    rms_v = np.sqrt(np.mean(measure.v1**2))
    rms_imeas = np.sqrt(np.mean(measure.i1**2))
    rms_isim = np.sqrt(np.mean(simulation_adjust.i1**2))
    
    square_relative_error_fromIrms=rmse/rms_imeas
    relative_root_mean_square_error=rmse/sum(measure.i1)
    return dist
    #%%Searching times 
# with open("time.pickle", "rb") as f:
#     time_sim = pickle.load(f)
    
# with open("newsim_time.pickle", "rb") as f:
#     time_sim2 = pickle.load(f)
    
# dt=[]
# for i in range(1,len(time_sim)):
#     dt.append(time_sim[i]-time_sim[i-1])
    
# dt2=[]
# for i in range(1,len(time_sim)):
#     dt2.append(time_sim2[i]-time_sim2[i-1])

# dt=np.array(dt)
# dt2=np.array(dt2)

# fig = plt.figure()
# ax1 = fig.add_axes([0.1, 0.1,0.8, 0.8])
# ax1.plot(dt*1e6,linewidth=2, color=colors(0), label='ltspice dt')
# ax1.plot(dt2*1e6,linewidth=2, color=colors(1), label='medida dt')
# ax1.set_title('Pasos de integracion')
# ax1.set_xlim(0, len(dt))
# ax1.set_ylim(0, 2000)
# ax1.set_ylabel('dt(us)')
# # ax1.spines['right'].set_visible(False)
# # ax1.spines['top'].set_visible(False)
# ax1.xaxis.set_tick_params(which='major', size=10, width=2, direction='in')
# ax1.xaxis.set_tick_params(which='minor', size=7, width=2, direction='in')
# ax1.yaxis.set_tick_params(which='major', size=10, width=2, direction='in')
# ax1.yaxis.set_tick_params(which='minor', size=7, width=2, direction='in')
# ax1.grid(True)

# f, (ax1, ax2) = plt.subplots(2, 1)
# ax1.plot(dt*1e6,linewidth=2, color=colors(0), label='ltspice dt')
# ax1.set_title('Pasos de integracion')
# ax1.set_xlim(0, len(dt))
# ax1.set_ylim(0, 2000)
# ax1.set_ylabel('dt(us)')
# # ax1.spines['right'].set_visible(False)
# # ax1.spines['top'].set_visible(False)
# ax1.xaxis.set_tick_params(which='major', size=10, width=2, direction='in')
# ax1.xaxis.set_tick_params(which='minor', size=7, width=2, direction='in')
# ax1.yaxis.set_tick_params(which='major', size=10, width=2, direction='in')
# ax1.yaxis.set_tick_params(which='minor', size=7, width=2, direction='in')
# ax1.grid(True)
# ax1.legend(bbox_to_anchor=(0.78, 0.9), loc=10, frameon=True, fontsize=14)

# ax2.plot(dt2*1e6,linewidth=2, color=colors(1), label='medida dt')


# ax2.set_xlim(0, len(dt))
# ax2.set_ylim(0, 20)
# ax2.set_ylabel('dt(us)')
# # ax1.spines['right'].set_visible(False)
# # ax1.spines['top'].set_visible(False)
# ax2.xaxis.set_tick_params(which='major', size=10, width=2, direction='in')
# ax2.xaxis.set_tick_params(which='minor', size=7, width=2, direction='in')
# ax2.yaxis.set_tick_params(which='major', size=10, width=2, direction='in')
# ax2.yaxis.set_tick_params(which='minor', size=7, width=2, direction='in')
# ax2.grid(True)
# ax2.legend(bbox_to_anchor=(0.78, 0.8), loc=10, frameon=True, fontsize=14)