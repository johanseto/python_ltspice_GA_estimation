# python-ltspice-GA-estimation
![diagrama funcionamiento ](herramienta_manual_resumen.png)
Working repository of estimation tool for electrical devices based on GA.

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
