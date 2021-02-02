
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

LtspiceCallingTrafo(netlist,code,6)#0.5 seconds per simulation
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

def add_noise(signal,mu,sigma):
        noise = np.random.normal(mu, sigma,signal.shape) 
        rms = np.sqrt(np.mean(signal**2))
        signal_noise=rms*noise+signal
        return signal_noise
    
mu, sigma = 0, 0.02

v1_test=2400*np.sqrt(2)*np.sin(377*time_test)
v2_test=v1_test/10



model_ref=ModelTrafo(time_test,v1_test,v1_test,v1_test,v1_test)
model_test=ModelTrafo.unify_sim_model(model_ref,simulation)
model_testn=ModelTrafo(model_test.t,model_test.v1,model_test.i1,
                       model_test.v2,model_test.i2) #ccreate the model with noise
model_testn.v1=add_noise(model_testn.v1, mu, sigma)
model_testn.i1=add_noise(model_testn.i1, mu, sigma)
model_testn.v2=add_noise(model_testn.v2, mu, sigma)
model_testn.i2=add_noise(model_testn.i2, mu, sigma)

#....Plotting
plt.figure('v1')
ax1=plt.subplot(2,2,1)

nlabel_axis=25
nlabel_signal=25

ax1.plot(model_test.t,model_test.v1,'--',label='señal simulada',linewidth=0.6,color='black')
ax1.plot(model_test.t,model_testn.v1,label='señal simulada con ruido',alpha=0.6,linewidth=2,color='GREEN')
#plt.savefig('comparacion perfecta-simulada-v1.svg')
ax1.set_title('V1')
ax1.set_ylabel('Tensión[V]',fontsize=nlabel_axis)
ax1.set_xlabel('tiempo(s)',fontsize=nlabel_axis)

ax3=plt.subplot(2,2,3)
ax3.plot(model_test.t,model_test.i1,'--',label='señal simulada',linewidth=0.6,color='black')
ax3.plot(model_test.t,model_testn.i1,label='señal simulada con ruido',alpha=0.6,linewidth=2,color='GREEN')
#plt.savefig('comparacion perfecta-simulada-i1.svg')
ax3.set_title('i1')
ax3.set_ylabel('Corriente[A]',fontsize=nlabel_axis)
ax3.set_xlabel('tiempo(s)',fontsize=nlabel_axis)

ax2=plt.subplot(2,2,2)
ax2.plot(model_test.t,model_test.v2,'--',label='Señal simulada',linewidth=0.6,color='black')
ax2.plot(model_test.t,model_testn.v2,label='Señal simulada con ruido',alpha=0.6,linewidth=2,color='GREEN')
ax2.set_xlabel('tiempo(s)',fontsize=nlabel_axis)
ax2.set_title('V2')
ax2.set_ylabel('Tensión[V]',fontsize=nlabel_axis)
ax2.legend(bbox_to_anchor=(0, 1.22), loc=10, frameon=True, fontsize=nlabel_signal)


ax4=plt.subplot(2,2,4)
ax4.plot(model_test.t,model_test.i2,'--',label='señal simulada',linewidth=0.6,color='black')
ax4.plot(model_test.t,model_testn.i2,label='señal simulada con ruido',alpha=0.6,linewidth=2,color='GREEN')
ax4.set_xlabel('tiempo(s)',fontsize=nlabel_axis)
ax4.set_ylabel('Corriente[A]',fontsize=nlabel_axis)
plt.savefig('comparacion seniales.svg')
ax4.set_title('i2')
#plt.savefig('comparacion perfecta-simulada-i2.svg')
from sklearn.metrics import mean_squared_error
mse=mean_squared_error(v1_test,model_testn.v1)
print(mse)

# creating  


#%% Guardar  datos modelo modelo en csv
array2csv=np.array([model_test.t,model_test.v1,model_test.i1,
                   model_test.v2,model_test.i2])
array2csv=array2csv.T

import pandas as pd 
pd.DataFrame(array2csv).to_csv("values.csv")
array2csv.tofile('valuestrol.csv',sep=',',format='%10.5f')
np.savetxt('values_full.csv', array2csv, delimiter=",")

array2csvnoise=np.array([model_testn.t,model_testn.v1,model_testn.i1,
                   model_testn.v2,model_testn.i2])
array2csv=array2csvnoise.T

import pandas as pd 
pd.DataFrame(array2csv).to_csv("values.csv")
array2csv.tofile('valuestrol.csv',sep=',',format='%10.5f')
np.savetxt('values_noise.csv', array2csv, delimiter=",")