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

from sqlalchemy import create_engine

nltk.download('stopwords')
stemmer = nltk.SnowballStemmer("english")
stopword = set(stopwords.words('english'))

engine=create_engine('sqlite:///database/sentences.db')
data=pd.read_sql('select * from sentences', engine)
data=data.drop(['es','fr','de','it','pt','ru','ja','ko','pl'], axis=1)
print(data)