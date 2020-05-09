# -*- coding: utf-8 -*-
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

data = pd.read_csv("positions.csv")
print(data.columns)

# y ekseni
level = data.iloc[:,1].values.reshape(-1,1)
salary = data.Salary.values.reshape(-1,1)
x = level
salary1 = data.iloc[:,2].values.reshape(-1,1) # kendim denemek için yaptım ve aynısı yukarıkiyle


regression = LinearRegression()  # klasik uygulanan lineer formulü
regression.fit(level,salary)

tahmin = regression.predict(np.array([[8.3]]))



regressionPoly = PolynomialFeatures(degree = 4)  # regresiion poly yapmak için
levelPoly = regressionPoly.fit_transform(level)
regression2 = LinearRegression()
regression2.fit(levelPoly,salary)


tahmin2 = regression2.predict(regressionPoly.fit_transform([[8.3]]))

plt.scatter(level,salary, color = "red") # plot çizdirmek için
x = np.arange(min(level),max(level)).reshape(-1,1)  # plotu çizdirmek için.
plt.plot(x,regression.predict(x),color = "blue")
plt.plot(level,regression2.predict(levelPoly))
plt.show()
