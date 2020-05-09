# -*- coding: utf-8 -*-
import pandas as pd

filmler = pd.read_csv("imdb-1000.csv")
print(filmler.columns)

print(filmler.drop("content_rating",axis=1).head()) # axis = 1 kolon 0 = satır

filmler = filmler.drop("content_rating", axis=1 )
filmler = filmler.drop("actors_list", axis=1 )
filmler = filmler.drop(2, axis=0)  # satır silmek için satır ismi ve axis =0

rowstodrop = [1,0,4,6,8,10]
filmler = filmler.drop(rowstodrop,axis=0)

print(filmler)
