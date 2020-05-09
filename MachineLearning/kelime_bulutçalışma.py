# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 23:01:36 2020

@author: volka
"""
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud , STOPWORDS , ImageColorGenerator
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("train.tsv" , sep = "\t")

print(data)

text = data["Phrase"][0 ]
wordcloud = WordCloud().generate(text)
plt.imshow(wordcloud , interpolation = "bilinear")
plt.axis("off")
plt.show()


wordcloud = WordCloud(max_font_size= 40,
                      max_words= 50,
                     background_color= "white").generate(text)
plt.figure()
plt.imshow(wordcloud , interpolation = "bilinear")
plt.axis("off")
plt.show()
text = " ".join(i for i in data.Phrase)
ordcloud = WordCloud(max_font_size= 50,
                      max_words= 100,
                     background_color= "white").generate(text)
plt.figure()
plt.imshow(wordcloud , interpolation = "bilinear")
plt.axis("off")
plt.show()