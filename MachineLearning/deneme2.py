# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


data = pd.read_csv("insurance.csv")
print(data.columns)

# x ekseni
age = data.age.values.reshape(-1,1)
# y ekseni
smoker = data.smoker.values.reshape(-1,1)
data.smoker.replace(('yes', 'no'), (1, 0), inplace=True)

regression = LinearRegression()
regression.fit(age,smoker)
print(regression.predict(np.array([[45]])))

tahmin = regression.predict(np.array([[20]]))

regressionPoly = PolynomialFeatures(degree = 4)  # regresiion poly yapmak için
levelPoly = regressionPoly.fit_transform(age)
regression2 = LinearRegression()
regression2.fit(levelPoly,smoker)

tahmin2 = regression2.predict(regressionPoly.fit_transform([[30]]))

plt.scatter(age,smoker, color = "red")
plt.show()
x = np.arange(min(age),max(age),0.01).reshape(-1,1)
plt.plot(age,regression.predict(age),color = "orange")
plt.plot(smoker,regression2.predict(levelPoly))
plt.show()
plt.xlabel("yaş")
plt.ylabel("sigara içen seviyesi")
plt.title("sigara yaş orantısı")
plt.show()
