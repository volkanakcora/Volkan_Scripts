import pandas as pd
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from nltk.stem import PorterStemmer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
# reading data from csv
df = pd.read_csv('spam.csv',  encoding="ISO-8859-1")

# renaming columns
df = df.rename(columns={'v1': 'label', 'v2': 'text'})
# df['label'] = df.label.map({'ham': 0, 'spam': 1})
df.head()
df.info()

df.fillna(' ', inplace=True)
# putting all text in one sms all together
df['text_msg'] = df['text'] + df['Unnamed: 2'] + df['Unnamed: 3'] + df['Unnamed: 4']

# remove extra whitespace
df['text_msg'] = df['text_msg'].str.strip()

# make lowercase all the text messages
df['text_msg'] = df['text_msg'].str.lower()

# tokenize each message
df['word_tokens'] = df.apply(lambda x: x['text_msg'].split(' '), axis=1)

# removing stopwords
stop_words = set(stopwords.words('english'))
df['cleaned_text_msg'] = df.apply(lambda x: [word for word in x['word_tokens'] if word not in stop_words], axis=1)

# put origin of each word => stemmed words
ps = PorterStemmer()
df['stemmed'] = df.apply(lambda x: [ps.stem(word) for word in x['cleaned_text_msg']], axis=1)

# final message, deleting 1 letter words
df['final_msg'] = df.apply(lambda x: ' '.join([word for word in x['cleaned_text_msg'] if len(word)>1]), axis=1)

# Create an empty list for rows in dataset // I didn't use that, but it's good to have for further functions
msg_list =[]

# Iterate over each row
for index, rows in df.iterrows():
    # Create list for the current row
    my_temp_list =[rows.label, rows.final_msg]
    # append the list to the final list
    msg_list.append(my_temp_list)

# creating one lr instance
lr = LogisticRegression()

# for the curve
x = df["final_msg"].values.reshape(-1,1)
y = df["label"].values.reshape(-1,1)

# You can change your random state as requested (random sampling and test_size, they effect your accuracy)
X, X_test, y_train, y_test = train_test_split(df['final_msg'], df['label'], test_size=0.1, random_state=1)

vectorizer = TfidfVectorizer()

X_train = vectorizer.fit_transform(X)
X_test = vectorizer.transform(X_test)

# fit the data to the lr model
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)

# score method to get accuracy
score = lr.score(X_test, y_test)

#print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
#print(y_pred)
# print out accuracy score of lr model
print('score:'+str(score))




def plot_roc_curve(fpr, tpr):
    plt.plot(fpr, tpr, color='orange', label='ROC')
    plt.plot([0, 1], [0, 1], color='darkblue', linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend()
    plt.show()
    
x,y= make_classification(n_samples=1000, n_classes=2, weights=[1,1], random_state=1)    
   
trainX, testX, trainy, testy = train_test_split(x, y, test_size=0.3, random_state=1)

model = RandomForestClassifier()
model.fit(trainX,trainy)

probs = model.predict_proba(testX)
probs = probs[:, 1]
auc = roc_auc_score(testy, probs)
print('AUC: %.2f' % auc)


fpr, tpr, thresholds = roc_curve(testy, probs)
print(plot_roc_curve(fpr, tpr))