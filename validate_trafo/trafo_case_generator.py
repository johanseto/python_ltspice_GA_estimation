
import numpy as np
import pandas
from estimator_classes_trafo import LtspiceCallingTrafo,ModelTrafo
sim_name='trafo_single'
sim_raw='/'+sim_name+'.raw'

#adquire caracterstics from measure signal
n=256#muestras por ciclo
dt=1/(60*n)
time_test=np.arange(0,50e-3,dt)
    


#%Python netlist modifications

dt=dt*1000

dt=str(dt)



netlist= r'C:\Users\user\Desktop\python_spice\validate_trafo\trafo_single.net'


code=('* C:\\Users\\user\\Desktop\\python_spice\\validate_trafo\\trafo_single.asc \n'
'R1 N001 N002 1 \n'
'L1 N002 N003 0.01 \n'
'V1 N001 0 SINE(0 3394.11 60) \n'
'R2 N003 0 1000 \n'
'R3 N005 0 100 \n'
'L2 N003 0 1 \n'
'L3 N004 0 0.01 \n'
'L4 N004 N005 0.2m \n'
'.tran 50ms \n'
'K L2 L3 1 \n'
'.options  maxstep=0.1e-6 \n'
'.backanno \n'
'.end \n'
)



#%% Create and run new netlist

LtspiceCallingTrafo(netlist,code,5)#0.5 seconds per simulation
variables=['V(n001)','I(R1)','V(n004)','I(L4)']
simulation=LtspiceCallingTrafo.getData(sim_raw, variables)# simulation_Model  
    
#%%
import matplotlib.pyplot as plt
time=simulation.t
plt.plot(time)

dt2=[]
for i in range(len(time)-1):
    dt2.append(time[i+1]-time[i])
plt.figure()   
plt.plot(dt2)
plt.plot([dt]*len(dt2))
plt.figure()
plt.plot(time,simulation.v1)

#%%Make some noise

v1_test=2400*np.sqrt(2)*np.sin(377*time_test)
v2_test=v1_test/10
plt.figure()
plt.plot(time_test,v1_test)
model_ref=ModelTrafo(time_test,v1_test,v1_test,v1_test,v1_test)

model_test=ModelTrafo.unify_sim_model(model_ref,simulation)
plt.plot(model_test.t,model_test.v1)

plt.figure()
plt.plot(time_test,v2_test)
plt.plot(model_test.t,model_test.v2)
dist = np.linalg.norm(v1_test-model_test.v1)
print(dist)

from sklearn.metrics import mean_squared_error
mse=mean_squared_error(v1_test,model_test.v1)
print(mse)


mu, sigma = 0, 0.01 
# creating a noise with the same dimension as the dataset (2,2) 
noise = np.random.normal(mu, sigma,model_test.v1.shape) 
print(noise)
y=2400*noise+model_test.v1
plt.figure()
plt.plot(model_test.t,y)
model_test.v1=y
rms = np.sqrt(np.mean(model_test.v1**2))
#%% Guardar  datos modelo modelo en csv
array2csv=np.array([model_test.t,model_test.v1,model_test.i1,
                   model_test.v2,model_test.i2])
array2csv=array2csv.T

import pandas as pd 
pd.DataFrame(array2csv).to_csv("values.csv")
array2csv.tofile('values0.csv',sep=',',format='%10.5f')
np.savetxt('values2.csv', array2csv, delimiter=",")