# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 18:34:47 2020

@author: user
"""

import os
import time
import ltspice
import numpy




  #%% Create new netlist
def newNetCall(netlist,code):


    f_id=open(netlist,'w')
    f_id.write(code)
    f_id.close()
    #Simulation
    os.system('ltspice_call.bat')
    time.sleep(7)
    os.system('ltspice_end.bat')   
    


  #%%Get info    
#def getData(dir,variables):
#
#    class modelo:
#        def _init_(self,time,voltages,currents):
#            self.v=voltages
#            self.i=currents
#            self.t=time
#
#    
#    
#    
#    
#    l = ltspice.Ltspice(dir) 
#    # Make sure that the .raw file is located in the correct path
#    l.parse() 
#    
#    time = l.getTime()
#   # V_source = l.getData('V(V1)')
  
    
    #  variables=l.v_list
#   # valores=numpy.zeros([3,len(time)])
#    
#    
  
    #for  i in range(3):
        #valores[i,:]=l.getData(variables[i])
#        
#        
#        
#    
#    
#    
#    señal=modelo(time,V,I) 
#    
#  
#    return señal
 
    
    