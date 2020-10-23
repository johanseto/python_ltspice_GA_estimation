# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 18:34:47 2020

@author: user
"""

import os
import time
import ltspice

  #%% Create new netlist
def newNetCall(netlist,code):


    f_id=open(netlist,'w')
    f_id.write(code)
    f_id.close()
    #Simulation
    os.system('ltspice_call.bat')
    time.sleep(5)
    os.system('ltspice_end.bat')   
    


  #%%Get info    
def getData(dir):
    

    
    l = ltspice.Ltspice(dir) 
    # Make sure that the .raw file is located in the correct path
    l.parse() 
    
    time = l.getTime()
    V_source = l.getData('V(source)')
    V = l.getData('V(cap)')
    I=l.getData('I(R1)')
  
    return time,V,I
 
    
    