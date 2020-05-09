# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

data = pd.read_csv("positions.csv")
level = data.iloc[:,1:2].values.reshape(-1,1)
salary = data.Salary.values

regression = RandomForestRegressor(n_estimators=5)
regression.fit(level,salary)

print(regression.predict(np.array([[8.3]])))
