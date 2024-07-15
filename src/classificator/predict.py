# predict.py
import pickle
import googletrans
def predict_if_hard(sentence):
    translator = googletrans.Translator()
    sentence = translator.translate(sentence, dest='en').text
    clf = pickle.load(open('src/classificator/model.pkl', 'rb'))
    cv = pickle.load(open('src/classificator/cv.pkl', 'rb'))
    sentence = cv.transform([sentence]).toarray()
    return clf.predict(sentence)[0] == 1