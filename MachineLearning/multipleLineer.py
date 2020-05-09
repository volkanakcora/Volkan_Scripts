# -*- coding: utf-8 -*-

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv("insurance.csv")
print(data.columns)

# y ekseni
expenses = data.expenses.values.reshape(-1,1)

# x ekseni

ageBmis = data.iloc[:,[0,2]].values

regression = LinearRegression()
regression.fit(ageBmis,expenses)

regression.predict

print(regression.predict(np.array([[22,20],[23,21],[24,22],[28,23],[29,26]])))