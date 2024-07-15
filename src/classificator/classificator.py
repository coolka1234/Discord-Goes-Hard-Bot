# classificator.py
from random import sample
from nltk.util import pr
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import re
import nltk
from nltk.corpus import stopwords
import string
import pickle

from sqlalchemy import create_engine

nltk.download('stopwords')
stemmer = nltk.SnowballStemmer("english")
stopword = set(stopwords.words('english'))

engine=create_engine('sqlite:///database/sentences.db')
data=pd.read_sql('select * from sentences', engine)
data=data.drop(['es','fr','de','it','pt','ru','ja','ko','pl'], axis=1)
print(data)

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[0-9]+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    text = ' '.join([word for word in text.split() if word not in stopword])
    text = ' '.join([stemmer.stem(word) for word in text.split()])
    return text

data['sentence'] = data['sentence'].apply(clean_text)
x=np.array(data['sentence'])
y=np.array(data['hard'])

cv = CountVectorizer()
x = cv.fit_transform(x)
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

clf=DecisionTreeClassifier()
clf.fit(X_train, y_train)

# sample_text = "domineering at the expense of your own country."
# sample_text = cv.transform([sample_text]).toarray()
# print(clf.predict(sample_text))

pickle.dump(clf, open('src/classificator/model.pkl', 'wb'))
pickle.dump(cv, open('src/classificator/cv.pkl', 'wb') )
print("Model saved")
