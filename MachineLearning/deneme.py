# -*- coding: utf-8 -*-

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv("insurance.csv")
print(data.columns)

# x ekseni
sex = data.sex.values.reshape(-1,1)
data.sex.replace(('female', 'male'), (1, 0), inplace=True)

# y ekseni
smoker = data.smoker.values.reshape(-1,1)
data.smoker.replace(('yes', 'no'), (1, 0), inplace=True)

regression = LinearRegression()
regression.fit(sex,smoker)
print(regression.predict(np.array([[45]])))
tahmin = regression.predict(np.array([[25]]))
print(tahmin)


plt.scatter(sex,smoker, color = "red")
plt.show()
x = np.arange(min(sex),max(sex),0.01).reshape(-1,1)
plt.plot(sex,regression.predict(sex),color = "orange")
plt.xlabel("cinsiyet")
plt.ylabel("sigara içen seviyesi")
plt.title("sigara cinsiyet orantısı")
plt.show()