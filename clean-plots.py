# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 14:18:27 2020

@author: Emanuel HG
"""
# Plots  DIAGRAMAS

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

MAIN_PATH = "D:/Trabajos/Programacion/Udemy/Python/python-ml-course/datasets/"
fileName = "customer-churn-model/Customer Churn Model.txt"
fullPath = os.path.join(MAIN_PATH, fileName)

data = pd.read_csv(fullPath)
print(data.head())



    

#///////// HISTOGRAMA DE FRECUENCIAS/////////////////////
plt.hist(data["Day Calls"],bins = int(np.ceil(1 + np.log2(3333))))# bean permite introducir las diviciones deseadas [0,30,60,..,,,100]
plt.title("histograma de nuemero de llamadas al dia")
plt.xlabel("n- llamadas ak dia")
plt.ylabel("frecuencia")
plt.close()

print(int(np.ceil(1 + np.log2(3333))))


#BOXPLOT, DIAGRAMA DE CAJA Y BIGOTES
#permiete ver donde estan condensados los valores centrales, los vordes corresponden al cuartil 25 y al 75
plt.boxplot(data["Day Calls"])#mediana = al valor central
plt.ylabel("numero de llamadas diarias")
plt.title("Boxplot de las llamadas diarias")

#///////Scatter Plot (nube de puntos o nube de dispersion)

data.plot(kind="scatter", x ="Day Mins", y = "Day Charge")
data.plot(kind="scatter", x ="Night Mins", y = "Night Charge")

#compartit un mismo grafico
figure, axs = plt.subplots(2,2, sharey=True, sharex=True)
data.plot(kind="scatter", x="Day Mins", y ="Day Charge", ax=axs[0][0])
data.plot(kind="scatter", x="Night Mins", y="Night Charge", ax=axs[0][1])
data.plot(kind="scatter", x="Day Calls", y ="Day Charge", ax=axs[1][0])
data.plot(kind="scatter", x="Night Calls", y="Night Charge", ax=axs[1][1])
plt.close()
