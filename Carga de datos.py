# -*- coding: utf-8 -*-
"""
leer datos de cvs

Created on Wed Jul 29 13:14:34 2020

@author: Emanuel HG
"""
# //////////////////////////////bloque de importacion de datos 1 CSV///////////////////////////////
import pandas as pd
import os

MAIN_PATH = "D:/Trabajos/Programacion/Udemy/Python/python-ml-course/datasets/"
fileName = "titanic/titanic3.csv"
fullPath = os.path.join(MAIN_PATH, fileName)

data = pd.read_csv(fullPath)
print(data.head())
print(data.columns)

# //////////////////////////////bloque de importacion de datos 2  TXT ///////////////////////////////

data2 = pd.read_csv(MAIN_PATH+"customer-churn-model/Customer Churn Model.txt")
print("Leido con TXT")
print(data2.head())

# /////Para renombrar la abecera de un dataset con base en otro archivo externo///////
data_columnas = pd.read_csv(
    MAIN_PATH + "customer-churn-model/Customer Churn Columns.csv")
dataColumnasList = data_columnas["Column_Names"].tolist()
data2 = pd.read_csv(MAIN_PATH+"customer-churn-model/Customer Churn Model.txt",
                    header=None, names=dataColumnasList)

print(data2.head())
'''
#/////////////////leer datos Manualmente Funcion OPEN py//////////////////////

data3= open (MAIN_PATH+"customer-churn-model/Customer Churn Model.txt","r")
nombreColumnas = data3.readline().strip().split(",")
ncols = len(nombreColumnas)

    #Se crea un diccionario (nombrecolumna:arreglo de valores), en el cual se va a asignar lo datos primero se crea y luego
        #se le asigna un arreglo vacio

cont=0
diccionarioPrincipal = {}

for columna in nombreColumnas:
    diccionarioPrincipal[columna] = []


    #a continuacion se procede a rellenar cada uno de los arreglos con sus respectivos datos

for linea in data3:
    valores = linea.readline().strip().split(",")
    for i in range(len(nombreColumnas)):
        diccionarioPrincipal[nombreColumnas[i]].append(valores[i])
    cont+=1
    

print("el data set tiene %d filas y %d columnas"%(cont,ncols))
df3= pd.DataFrame(diccionarioPrincipal)
print(df3.head())
   '''










