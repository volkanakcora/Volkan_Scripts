import pandas as pd

filmler = pd.read_csv("imdb-1000.csv")

print(filmler.columns)
print(filmler.head())
print(filmler.star_rating.mean())
print(filmler.groupby("genre").star_rating.mean())
