# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 18:20:02 2019

@author: volka
"""

import pandas as pd 
data = pd.read_csv("train.tsv", sep = "\t")

data["Phrase"] = data["Phrase"].apply(lambda x: " ".join(x.lower() for x in x.split()))

data["Phrase"] = data["Phrase"].str.replace("[^\w\s]","")

data["Phrase"] = data["Phrase"].str.replace("\d","")

import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
sw = stopwords.words("english")
data["Phrase"].apply(lambda x: " ".join(x for x in x.split() if x not in sw ))
data["Phrase"] = data["Phrase"].apply(lambda x: " ".join(x for x in x.split() if x not in sw ))

sil = pd.Series(" ".join(data["Phrase"]).split()).value_counts()[-1000:]
data["Phrase"] = data["Phrase"].apply(lambda x: " ".join(x for x in x.split() if x not in sil ))

from textblob import Word
nltk.download("wordnet")

data["Phrase"] = data["Phrase"].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))

tf1 = (data["Phrase"]).apply(lambda x:pd.value_counts(x.split(" "))).sum(axis = 0).reset_index()


tf1 = (data["Phrase"]).apply(lambda x:pd.value_counts(x.split(" "))).sum(axis = 0).reset_index()