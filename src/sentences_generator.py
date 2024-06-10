from googletrans import Translator, LANGUAGES
from wonderwords import RandomSentence
import os
import sys
import numpy as np
import pandas as pd
dir2_path: str = os.path.normpath(os.path.join(os.path.dirname(__file__), '../res'))
sys.path.append(dir2_path)
import constants as res

language_translator = Translator()
sentence_generator = RandomSentence()

def generate_file_of_sentences(number : int):
    sentences = pd.DataFrame(columns=['sentence']+res.languages+['Hard'])
    for i in range(number):
        sentence = sentence_generator.sentence()
        sentences.loc[i, 'sentence'] = sentence
        for lang in res.languages:
            if lang == 'en':
                continue
            translation = language_translator.translate(sentence, dest=lang).text
            sentences.loc[i, lang] = translation
    sentences.to_csv(res.sentences_path, index=False)

if __name__ == "__main__":
    generate_file_of_sentences(10)