from googletrans import Translator, LANGUAGES
from wonderwords import RandomSentence
import os
import sys
import numpy as np
dir2_path: str = os.path.normpath(os.path.join(os.path.dirname(__file__), '../res'))
sys.path.append(dir2_path)
import constants as res

language_translator = Translator()
sentence_generator = RandomSentence()
print("Languages:")
print(LANGUAGES)

