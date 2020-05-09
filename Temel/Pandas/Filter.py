# -*- coding: utf-8 -*-
import pandas as pd

filmler = pd.read_csv("imdb-1000.csv")

print(filmler)
print(filmler.columns)
print(filmler.head())
print(filmler.tail())
print(filmler.title.head())
print(filmler[["title", "star_rating"]].head())# başlıklar ve ilk 5 i verdi
print(filmler[:9][["title", "star_rating"]].head())
print(filmler[filmler["star_rating"]> 8.5],["title", "star_rating"]) # filtreleme

print(filmler[(filmler["star_rating"]> 8.5)&(filmler["star_rating"] < 9)],
              ["title", "star_rating"])

print(filmler.query("star_rating > 9")
[["title","star_rating"]])