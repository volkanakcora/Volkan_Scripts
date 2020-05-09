# -*- coding: utf-8 -*-

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor

data = pd.read_csv("insurance.csv")

print(data.columns)

age = data.age.values.reshape(-1,1)

smoker = data.smoker.values.reshape(-1,1)
data.smoker.replace(('yes', 'no'), (1, 0), inplace=True)


regression = DecisionTreeRegressor()
regression.fit(age,smoker)
print(regression.predict(np.array([[60]])))

plt.scatter(age,smoker,color ="red")
plt.show()
x = np.arange(min(age),max(age)).reshape(-1,1)  # plotu çizdirmek için.
plt.plot(x,regression.predict(x), color="blue")
plt.xlabel("yaş doğrusu")
plt.ylabel("sigara doğrusu ")
plt.title(" sigara ve yaş oranı")
plt.show()
