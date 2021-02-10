# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 18:34:47 2020

@author: user
"""

import os
import time
import ltspice
import numpy as np
import pandas
import pickle
##Principal class
class Model:
    def __init__(self,time,signals):
        self.time=time
        self.signals=signals
        base=[]
        for signal in self.signals:
            base.append(max(signal)-min(signal))
        self.base=base
        
    def read_csv_signal(signals_file,n_signals):
        voltage_current_df = pandas.read_csv(signals_file,header=None)
        time=np.array(voltage_current_df.iloc[0:,0])
        signals=[]
        for i in range(n_signals):
            signals.append(np.array(voltage_current_df.iloc[0:,i+1])) #cero is time
            measure= Model(time,signals)# l
        return measure
    
    def unify_sim_model(measure,simulation):
        newsim_time=measure.time
        newsim_signals=[]
        for old_signal in simulation.signals:
            newsim_signals.append(np.interp(np.ravel(measure.time),
                             np.ravel(simulation.time),np.ravel(old_signal)))
       
        simulation_adjust=Model(newsim_time, newsim_signals)
        return simulation_adjust
    
    def signals_caracteristics(voltage_current_file):
        measure=Model.read_csv_signal(voltage_current_file)#Measure_model
        rms = np.sqrt(np.mean(measure.v1**2))
        vmax=rms*np.sqrt(2)
        dt=measure.t[2]-measure.t[1]
        t_init=measure.t[0]
        t_last=measure.t[-1]
    
        simulation_vars=[t_init,t_last,dt,vmax]
        return measure,simulation_vars

# Calling ltspice class
class LtspiceCalling:
  # Create new netlist
    def __init__(self,batch_file,netlist,code,seconds):
        f_id=open(netlist,'w')
        f_id.write(code)
        f_id.close()
        #Simulation
        os.system(batch_file)
        time.sleep(seconds)
           
    
    def getDataClosing(sim_raw,variables):
        l=ltspice.Ltspice(os.path.dirname(__file__)+sim_raw)
# Make sure that the .raw file is located in the correct path
#l = ltspice.Ltspice('C:/Users/user/Desktop/python_spice/root_con/practice_optpy.raw' ) 
        tryParse(l) 
        time=l.getTime()
        signals_sim=[]
        
        for signal in variables:
            signals_sim.append(l.getData(signal))
        simulation=Model(time,signals_sim)
        os.system('ltspice_end.bat')
        return simulation
    

            
            
            
class SimulationInfo:
    
        def __init__(self,netlist_path,sim_raw,parameters_target,signals_target,norm=False):
            self.netlist_path=netlist_path
            self.sim_raw=sim_raw
            self.parameters_target=parameters_target
            self.signals_target=signals_target
            self.index_param={}
            self.netlist_base=[]
            self.norm=norm

            netlist=netlist_path
            parameters=parameters_target
            # f_id=open(netlist,'r')
            # fid_string=f_id.read()
            # f_id.close()
            
            f_id=open(netlist,'r')
            fid_list=f_id.readlines()
            f_id.close()
            
            index_param={}
            index_row=-1#the first line is a path, began 0
            #raise and search the params in netlist
            for param in parameters:
                
                index_row=-1
                for row in fid_list:
                    index_row+=1#get the index of the row
                    ind=row.find(param)
                    if ind != -1 and ind==0:
                        index_param[param]=index_row
                        k=-3
                        while(not(row[k].isspace())):
                            k+=-1
                            
                        fid_list[index_row]=fid_list[index_row][:k]
            
            #fniish the recognition of parameter
            self.netlist_base=list.copy(fid_list)# list to create simulation cases
            for key in index_param:
                fid_list[index_param[key]]=fid_list[index_param[key]]+' '+'\n'
            
            # base_netlist=''.join(fid_list)
            netlist_base_path=netlist
            # f_id=open(netlist_base_path,'w')
            # f_id.write(base_netlist)
            # f_id.close()

            self.index_param=index_param
            self.netlist_base_path=netlist_base_path
            

                
            #configure batch open file
            close_file='ltspice_call_base.bat'
            f_id=open(close_file,'r')
            fid_string=f_id.read()
            f_id.close()
            
            
            
            index=netlist_base_path.rfind('\\')
            name_netlist=netlist_base_path[index+1:]
            
            new_batch=fid_string[:-1]+name_netlist
            
            batch_file='ltspice_call_'+name_netlist[:-4]+'.bat'
            f_id=open(batch_file,'w')
            f_id.write(new_batch)
            f_id.close()
            self.batch_file=batch_file
            with open("simu_charac.pickle", "wb") as f:
                pickle.dump(self, f)
# fid_string.find('R1')
# spaces=[]
# #buscador de espacios
# for row in fid_list:
#     for i in row:
#         if i=='':
#             spaces.append(row+i)
            
#%%

#%%

    #change and correct the \n jump was modified.
    

    
    
def tryParse(l): #Recursion function to avoid problem of parsing in the working directory
    try:
        l.parse()
    except:
        time.sleep(0.1)
        tryParse(l)
            
            
        




