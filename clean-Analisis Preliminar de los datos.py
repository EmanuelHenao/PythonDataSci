# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 08:10:58 2020

@author: Emanuel HG
"""

#////////////////RESUMEN DE DATOS : DIMENSIONES Y ESTRUCTURAS///////////////////////////
    
import pandas as pd
import os


MAIN_PATH = "D:/Trabajos/Programacion/Udemy/Python/python-ml-course/datasets/"
fileName = "titanic/titanic3.csv"
fullPath = os.path.join(MAIN_PATH, fileName)

data = pd.read_csv(fullPath)

print(data.head(20))#mustra los primeros valores
print(data.tail(10))#muestra los ultimos valores
print(data.shape)# retorna la forma del dataframe (Filas,columnas)
print(data.columns.values)# muestra los nombres de las columnas 

        #///////es posible hacer un resumen de los datos numericos, con estadisticas basicas //////

print(data.describe()) 
print(data['pclass'].describe(),"\n") 

        #///////// es necesario conocer los tipos de datos//////////
print(data.dtypes)

    #es posible conocer cuales datos estan VACIOS
print(pd.isnull(data["body"])) 
print(pd.notnull(data["body"]).values.ravel().sum() )

#QUE HACER CUANDO FALTAN VALORES///////////////////////////////////////////////
    #1. ELIMINAR DATOS, SEGUN FILAS O CULUMNAS VACIAS

data.dropna(axis=0,how="all")#elimina todas las filas, en las cuales todos sus valores sean nulos
# data.dropna(axis=0,how="any")#elimina todas las filas , en las cuales exista almenos un valor nulo !!:(
# data.dropna(axis=1,how="all")#elimina todas las columnas , en las cuales todos sus valores sean nulos
# data.dropna(axis=1,how="any")#elimina todas las columnas , en las cuales exista almenos un valor nulo !!:(

    #2. COMPUTO  DE VALORES FALTANTES
        #2.1 RELLENAR CON 0
#data = data.fillna(0)
        #2.2 RELLENAR SEGUN TIPO DE DATO
#data["body"] = data["body"].fillna(0)
#data["home.dest"] = data["home.dest"].fillna("desconocido")

        #2.3 RELLAR CON MEDIA/PROMEDIO 
data["age"] = data["age"].fillna(data["age"].mean())
print(data["age"].head(20))
        #2.4 RELLENAR CON EL PROXIMO O ANTERIOR VALOR MAS CERCANO
data["age"].fillna(method="ffill")
data["age"].fillna(method="backfill")

#VARIABLES DOOMYES
#funcion para crear variables doomies a apartir de un campo

def crearDummies(df,var_name):
    dummy = pd.get_dummies(df[var_name], prefix= var_name)#se crea una variable dommie con base en un campo, 
    df = df.drop(var_name, axis = 1)# se elimina la columna 
    df = pd.concat([df,dummy], axis = 1)#se concatena los 2 arreglos en 1, segun columnnas
    return df





