# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 17:50:49 2019

@author: volka
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



data = pd.read_csv("titanic3.csv")


print("Female : ", data[data['sex'].str.match("female")].count())
print("male :",data[data['sex'].str.match("male")].count())

#how many people survived divided by class.

print(sns.countplot(x='survived', hue='pclass', data=data))

# how many people survived by sex
print(sns.countplot(x='survived', hue='sex', data=data))

## We can infer that, as Molly,
# if you were a female and you were in class 1,
# probably you would survive.
#On the other hand, if you were a man and
# you were in class 3, you didn’t have good chances to live

plt.figure(figsize=(10,7))
sns.boxplot(x='pclass',y='age',data=data)

def add_age(cols):
    age = cols[0]
    pclass = cols[1]
    if pd.isnull(age):
        return int(data[data["pclass"] == pclass]["age"].mean())
    else:
        return age
    
    
    
data["age"] = data[["age", "pclass"]].apply(add_age,axis=1)   

data.drop("cabin",inplace=True,axis=1) 

data.dropna(inplace=True)


