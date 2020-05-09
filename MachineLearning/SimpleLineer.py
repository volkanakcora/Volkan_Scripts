# -*- coding: utf-8 -*-
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

data = pd.read_csv("hw_25000.csv")
print(data.columns)

boy = data.Height.values.reshape(-1,1)     # boy ve kiloyu uygun değerler haline getirdik
kilo = data.Weight.values.reshape(-1,1)

regression = LinearRegression()
regression.fit(boy,kilo)

print(regression.predict(np.array([[60]])))
print(regression.predict(np.array([[62]])))
print(regression.predict(np.array([[64]])))
print(regression.predict(np.array([[66]])))
print(regression.predict(np.array([[68]])))
print(regression.predict(np.array([[70]])))




plt.scatter(data.Height,data.Weight)
x = np.arange(min(data.Height),max(data.Height)).reshape(-1,1) # tAHMİN DEĞERlerini grafikleştirir
plt.plot(x,regression.predict(x),color = "red") # tahmin degeri grafikleştirme
plt.xlabel("boy")
plt.ylabel("Kilo")    # line ları adlandırmada kullanılırız
plt.title("Regression Model")
plt.show()

print(r2_score(kilo ,regression.predict(boy,)))  # datadan verdiğim sonuc yüzde 25 dooğru der.
