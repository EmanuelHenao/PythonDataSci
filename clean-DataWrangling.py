# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 10:26:27 2020

@author: Emanuel HG
"""

import pandas as pd
import os

MAIN_PATH = "D:/Trabajos/Programacion/Udemy/Python/python-ml-course/datasets/"
fileName = "customer-churn-model/Customer Churn Model.txt"
fullPath = os.path.join(MAIN_PATH, fileName)

data = pd.read_csv(fullPath)
print(data.head())
