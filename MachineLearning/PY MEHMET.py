# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 14:02:02 2019

@author: volka
"""

from textblob import TextBlob
from sklearn import model_selection, preprocessing , linear_model,naive_bayes,metrics
from sklearn.feature_extraction.text import TfidfVectorizer , CountVectorizer
from sklearn import decomposition , ensemble

import pandas , xgboost , numpy , textblob , string
from keras.preprocessing import text , sequence
from keras import layers, models, optimizers 

import pandas as pd
data8 = pd.read_csv("train.tsv", sep = "\t")

data8["Sentiment"].replace(0, value = "negative" , inplace = True)
data8["Sentiment"].replace(1, value = "negative" , inplace = True)


data8["Sentiment"].replace(3, value = "pozitive" , inplace = True)
data8["Sentiment"].replace(4, value = "pozitive" , inplace = True)

data8 = data8[(data8.Sentiment == "negative") | (data8.Sentiment == "pozitive")]

df = pd.DataFrame()
df["text"] =  data8["Phrase"]
df["label"] = data8["Sentiment"]

## LOWER WORDS

df["text"].apply(lambda x: " ".join(x.lower() for x in x.split()))
## NOKTALAMA İŞARETLERİNİN SİLİNMESİ

df["text"] = df["text"].str.replace("[^\w\s]","")

###Sayıların silinmesi
df["text"] = df["text"].str.replace("\d","")

## STOPWORDS
import nltk

##nltk.download("stopwords")
from nltk.corpus import stopwords
sw = stopwords.words("english")
df["text"]= df["text"].apply(lambda x: " ".join(x for x in x.split() if x not in sw ))

## Deleting less words

import pandas as pd

sil = pd.Series(" ".join(df["text"]).split()).value_counts()[-1000:]
df["text"] = df["text"].apply(lambda x: " ".join(x for x in x.split() if x not in sil ))


## Lemmatization

from textblob import Word
nltk.download("wordnet")

df["text"] = df["text"].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split() ] ))


## TEST -TRAIN OLUŞTURMA

train_x,test_x , train_y , test_y = model_selection.train_test_split(df["text"],df["label"], random_state = 1)

encoder = preprocessing.LabelEncoder()

train_y = encoder.fit_transform(train_y)
train_y = encoder.fit_transform(test_y)

##print(train_y[0:5])

##print(test_y[0:5])


##Count Vectors ## 

vectorizer = CountVectorizer()
vectorizer.fit(train_x)

x_train_count = vectorizer.transform(train_x)
x_test_count = vectorizer.transform(test_x)

x_train_count.toarray()

## TF-IDF

# word level

tf_idf_word_vectorizer = TfidfVectorizer()
tf_idf_word_vectorizer.fit(train_x)


x_train_tf_idf_word = tf_idf_word_vectorizer.transform(train_x)
x_test_tf_idf_word = tf_idf_word_vectorizer.transform(test_x)

x_train_tf_idf_word.toarray()
## ngram level tf ıdf
tf_idf_ngram_vectorizer = TfidfVectorizer(ngram_range = (2,3))
tf_idf_ngram_vectorizer.fit(train_x)

x_train_tf_idf_ngram = tf_idf_ngram_vectorizer.transform(train_x)
x_test_tf_idf_ngram = tf_idf_ngram_vectorizer.transform(test_x)


##characters level tf-idf

tf_idf_chars_vectorizer = TfidfVectorizer(analyzer = "char" , ngram_range = (2,3))
tf_idf_chars_vectorizer.fit(train_x)

x_train_tf_idf_chars = tf_idf_chars_vectorizer.transform(train_x)
x_test_tf_idf_chars =  tf_idf_chars_vectorizer.transform(test_x)

## Logistic Regression

loj = linear_model.LogisticRegression()
loj_model = loj.fit(x_train_count , train_y)
accuracy = model_selection.cross_val_score(loj_model,
                                           x_test_count,
                                           test_y,
                                           cv = 10).mean()

print("Count vectors accuracy rate : " , accuracy)





loj = linear_model.LogisticRegression()
loj_model = loj.fit(x_train_tf_idf_word , train_y)
accuracy = model_selection.cross_val_score(loj_model,
                                           x_test_tf_idf_word,
                                           test_y,
                                           cv = 10).mean()

print("Word-Level TF-IDF accuracy rate : " , accuracy)



loj = linear_model.LogisticRegression()
loj_model = loj.fit(x_train_tf_idf_ngram , train_y)
accuracy = model_selection.cross_val_score(loj_model,
                                           x_test_tf_idf_ngram,
                                           test_y,
                                           cv = 10).mean()

print("N-GRAM TF-IDF  accuracy rate : " , accuracy)




loj = linear_model.LogisticRegression()
loj_model = loj.fit(x_train_tf_idf_chars , train_y)
accuracy = model_selection.cross_val_score(loj_model,
                                           x_test_tf_idf_chars,
                                           test_y,
                                           cv = 10).mean()

print("Char Level accuracy rate : " , accuracy)


### NAİVE BAYES

nb = naive_bayes.MultinomialNB()
nb_model = nb.fit(x_train_count , train_y)
accuracy = model_selection.cross_val_score(loj_model,
                                           x_test_count,
                                           test_y,
                                           cv = 10).mean()

print("Count vectors accuracy rate : " , accuracy)

nb = naive_bayes.MultinomialNB()
nb_model = nb.fit(x_train_tf_idf_word , train_y)
accuracy = model_selection.cross_val_score(loj_model,
                                           x_test_tf_idf_word,
                                           test_y,
                                           cv = 10).mean()

print("Word - Level TF-IDF accuracy rate : " , accuracy)

nb = naive_bayes.MultinomialNB()
nb_model = nb.fit(x_train_tf_idf_ngram , train_y)
accuracy = model_selection.cross_val_score(loj_model,
                                           x_test_tf_idf_ngram,
                                           test_y,
                                           cv = 10).mean()

print("N-GRAM TF-IDF accuracy rate : " , accuracy)

nb = naive_bayes.MultinomialNB()
nb_model = nb.fit(x_train_tf_idf_chars , train_y)
accuracy = model_selection.cross_val_score(loj_model,
                                           x_test_tf_idf_chars,
                                           test_y,
                                           cv = 10).mean()

print("Char level accuracy rate : " , accuracy)



## RANDOM FOREST


rf = ensemble.RandomForestClassifier()
rf_model = rf.fit(x_train_count , train_y)
accuracy = model_selection.cross_val_score(loj_model,
                                           x_test_count,
                                           test_y,
                                           cv = 10).mean()

print("Count vectors accuracy rate : " , accuracy)

rf = ensemble.RandomForestClassifier()
rf_model = rf.fit(x_train_tf_idf_word , train_y)
accuracy = model_selection.cross_val_score(loj_model,
                                           x_test_tf_idf_word,
                                           test_y,
                                           cv = 10).mean()

print("Word - Level TF-IDF accuracy rate : " , accuracy)

rf = ensemble.RandomForestClassifier()
rf_model = rf.fit(x_train_tf_idf_ngram , train_y)
accuracy = model_selection.cross_val_score(loj_model,
                                           x_test_tf_idf_ngram,
                                           test_y,
                                           cv = 10).mean()

#print("N-GRAM TF-IDF accuracy rate : " , accuracy)

rf = ensemble.RandomForestClassifier()
rf_model = rf.fit(x_train_tf_idf_chars , train_y)
accuracy = model_selection.cross_val_score(loj_model,
                                           x_test_tf_idf_chars,
                                           test_y,
                                           cv = 10).mean()

print("Char level accuracy rate : " , accuracy)



loj_model

loj_model.predict("yes i like this film")

yeni_yorum = pd.Series("this film is very nice and good i like it")

yeni_yorum = pd.Series("no not good look at that shit very bad")

v = CountVectorizer()
v.fit(train_x)
yeni_yorum = v.transform(yeni_yorum)

loj_model.predict(yeni_yorum)
