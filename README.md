# python-ltspice-GA-estimation
Repositorio de trabajo de herramienta de estimación de dispositivos eléctricos basada en GA.

 La metodología interconecta técnicas de estimación en un lenguaje de programación(Python) con un programa de simulación (LTspice).La  estimación se basa en simulaciones iterativas que se comparan con una entrada o medidas hasta hallar los parámetros de salida, como se muestra en ek gisguiente diagrama.
![diagrama funcionamiento ](herramienta_manual_resumen.png)

## Funcionamiento

El flujo del trabajo inicia con la selección del dispositivo de su modelo eléctrico o de topología. En ese sentido su topología se dispone por medio de un modelado basado en Netlist en LTspice. De esa manera se carga el Netlist por medio de “strings” para manipular los parámetros a estimar y configurar el centro de control y procesamiento de Python con los respectivos parámetros objetivos.

Luego desde Python se inicia una rutina de estimación basado de G.A se crea una población de individuos basados en los parámetros objetivo. Así se da inicio al proceso iterativo basado en la técnica para estimar.

 En el proceso cada individuo se somete a una evaluación en el software de simulación. Desde Python se da la instrucción de script de consola donde por medio de comandos de consola se envía cada individuo a LTspice, se simula y se devuelve al centro de control la información de las señales eléctricas simuladas a Python. De ese modo se extraen las señales de simulación para manipularlas y compararlas con las señales medidas con una métrica de semejanza.
Cada individuo de parámetros tiene una evaluación en la que se mide si su simulación tiene semejanza a los datos medidos y así se emplea la técnica evolucionaria de inteligencia artificial sucesivamente hasta extraer el individuo que prevea el mejor parentesco con las señales medidas.
 Por último, luego de que el algoritmo de control haya encontrado la mejor solución en el proceso del algoritmo genético, se consolida el proceso y se puede dar como salida, los parámetros estimados con mejor ajuste de las medidas físicas del dispositivo eléctrico.

## Conocimientos previos recomendados

Para la utilización del repositorio se recomienda tener formación o conocimiento en las siguientes temáticas:
- Modelado y simulación en electrónica de potencia.
- Herramienta de simulación LTspice.
- Lenguaje de programación Python.

## Instalación


1. Instalar [Ltspice XVII](https://www.analog.com/en/design-center/design-tools-and-calculators/ltspice-simulator.html) en Windows 10.

2. Instalar [Python 3.7](https://www.python.org/downloads/) o superior.

3. Se recomienda instalar el paquete e manejo o núcleo [AnaConda](https://docs.anaconda.com/anaconda/install/windows/) que incluye Spyder para mayor facilidad de manejo de datos en optimización y estimación. 

4. Use el administrador de paquetes  [pip](https://pip.pypa.io/en/stable/) para instalar la librería [ltspice](https://pypi.org/project/ltspice/).

```bash

pip install ltspice
```

5. Descargar respositorio de trabajo [python-ltspice-GA-estimacion](https://github.com/johanv26/python_ltspice_GA_estimation) con código fuente de la herramienta en Github.


## Uso

Para la utilización de este repositorio se debe tener instalados los pasos previos del ítem anterior.

El proceso se basa en la ejecución del archivo principal *main_general_estimator.py*. Este script principal se compone de 3 secciones principales: Sección de adquirir señales en modelo de trabajo. Sección de crear ambiente de simulación con la clase de procesamiento. Y por último la sección de estimación por medio del algoritmo genético.
![diagrama utlizacion codigo principal](esquema_manual_herramienta.png)
###1) Modelo de señales adquiridas.
```python
#%%Measure data recolection-model class

signals_file='values_noise.csv'
n=4

signal_name=['v1','i1','v2','i2']
measure=Model.read_csv_signal(signals_file,4)
measure2=Model(measure.time,measure.signals[1:])
with open("measure.pickle", "wb") as f:
    pickle.dump(measure2, f)
```
La herramienta se basa en estimar los parámetros de un disipativos eléctricos a partir de un modelo eléctrico de simulación.
Por tal motivo el codigo principal utiliza como base la formulación de un circuito de simulación en netlist para estimar. 

```python


import numpy as np
import pickle
from estimator_classes_general import Model,SimulationInfo
from functions_GA import evalPopu,upperData,nextPopu
from plot_file import plotting
import datetime

signals2=['I(R1)','V(n004)','I(L4)']
simu_data=SimulationInfo(netlist_path,sim_raw,parameters,signals2,norm=True)

signals_file='values_noise.csv'
n=4

signal_name=['v1','i1','v2','i2']
measure=Model.read_csv_signal(signals_file,4)
sim_name='trafo_single'
sim_raw='/'+sim_name+'.raw'
netlist_path= r'C:\Users\user\Desktop\python_spice\trafo\trafo_single.net'
parameters=['R1','R2','L1','L2','L3']
signals2=['I(R1)','V(n004)','I(L4)']
```


## Contribución
Todas los requests o peticiones de colaboración son bienvenidas. Para mayor cambios, por favor abrir una discusión para tratar el tema o item posible a modificar.

## Autores y reconocimiento
Este repositorio fue desarrollado por Johan Castiblanco, ingeniero electrónico. Se reconoce al grupo de investigación GICEP de la Universidad Nacional de Colombia sede Manizales, por su formación y acompañamiento en temáticas relacionadas con electrónica de potencia y modelado y simulación. 
Se agradece también por la  colaboración a los doctores Andres Felipe Guerrero y Armando Ustariz en el proceso.

## License
[MIT](https://choosealicense.com/licenses/mit/)
