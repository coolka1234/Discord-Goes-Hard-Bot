from googletrans import Translator, LANGUAGES
from wonderwords import RandomSentence
import os
import sys
dir2_path: str = os.path.normpath(os.path.join(os.path.dirname(__file__), '../res'))
sys.path.append(dir2_path)
import constants as res

language_translator = Translator()
sentence_generator = RandomSentence()
print("Languages:")
print(LANGUAGES)
for language in res.languages:
    if language == 'en':
        continue
    sentence = sentence_generator.sentence()
    print(f"Original sentence: {sentence}")
    print(f"Language: {language}")
    translated_sentence = language_translator.translate(sentence,src='en',dest=language).text
    print(f"Translated sentence: {translated_sentence}")
    print("\n")
