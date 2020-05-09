# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 00:17:14 2019

@author: volka
"""
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import confusion_matrix

import numpy as np
import itertools
import matplotlib.pyplot as plt

def get_all_data():
    root = "C:\python\MachineLearning/"
    
    with open (root + "SMSSpamCollection.txt" , "r") as text_file:
        data = text_file.read().split("\n")
        return data
    
get_all_data()

def preprocessing_data(data):
    processing_data = []
    for single_data in data:
        if len(single_data.split("\t")) == 2 and single_data.split("\t")[1] != "":
            processing_data.append(single_data.split("\t"))

    return processing_data

all_data = get_all_data()

preprocessing_data(all_data)

def split_data(data):
    total = len(data)
    training_ratio = 0.75
    training_data = []
    evaluation_data = []

    for indice in range(0, total):
        if indice < total * training_ratio:
            training_data.append(data[indice])
        else:
            evaluation_data.append(data[indice])

    return training_data, evaluation_data

def preprocessing_step():
    data = get_all_data()
    processing_data = preprocessing_data(data)

    return split_data(processing_data)

def training_step(data, vectorizer):
    training_text = [data[0] for data in data]
    training_result = [data[1] for data in data]

    training_text = vectorizer.fit_transform(training_text)

    return BernoulliNB().fit(training_text, training_result)

training_data, evaluation_data = preprocessing_step()
vectorizer = CountVectorizer(binary = 'true')
classifier = training_step(training_data, vectorizer)
result = classifier.predict(vectorizer.transform(["I love this movie!"]))

result[0]


def analyse_text(classifier, vectorizer, text):
    return text, classifier.predict(vectorizer.transform([text]))
  
def print_result(result):
    text, analysis_result = result
    print_text = "Positive" if analysis_result[0] == '1' else "Negative"
    print(text, ":", print_text)
    
    
    def simple_evaluation(evaluation_data):
    evaluation_text     = [evaluation_data[0] for evaluation_data in evaluation_data]
    evaluation_result   = [evaluation_data[1] for evaluation_data in evaluation_data]

    total = len(evaluation_text)
    corrects = 0
    for index in range(0, total):
        analysis_result = analyse_text(classifier, vectorizer, evaluation_text[index])
        text, result = analysis_result
        corrects += 1 if result[0] == evaluation_result[index] else 0

    return corrects * 100 / total