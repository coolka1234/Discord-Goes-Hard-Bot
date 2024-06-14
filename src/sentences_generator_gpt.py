# sentence generator using DialoGPT
from ast import mod
import pandas as pd
from transformers import AutoModelForCausalLM, AutoTokenizer
import wonderwords
from googletrans import Translator, LANGUAGES
from sqlalchemy import create_engine
import csv
import os
import sys
dir2_path: str = os.path.normpath(os.path.join(os.path.dirname(__file__), '../res'))
sys.path.append(dir2_path)
import constants as res

model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
model.generation_config.pad_token_id = tokenizer.pad_token_id

def generate_discord_message(prompt, max_length=150, num_return_sequences=30):
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    
    outputs = model.generate(
        inputs,
        max_length=max_length,
        num_return_sequences=num_return_sequences,
        no_repeat_ngram_size=3,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.7,
    )
    
    generated_messages = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
    return generated_messages


def generate_file_of_sentences(number : int):
    messages = []
    for i in range(number):
        prompt = wonderwords.RandomWord().word()
        messages.append(generate_discord_message(prompt, num_return_sequences=1))
    sentences = pd.DataFrame(columns=['sentence']+res.languages+['Hard'])
    language_translator = Translator()
    for i, sentence in enumerate(messages):
        sentences.loc[i, 'sentence'] = sentence[0]
        for lang in res.languages:
            if lang == 'en':
                continue
            translation = language_translator.translate(sentence[0], dest=lang).text
            sentences.loc[i, lang] = translation
    con= create_engine('sqlite:///'+res.sentences_path)
    sentences.to_sql(res.sentences_path, if_exists='append', index=True, con=con, chunksize=1000)

if __name__ == "__main__":
    generate_file_of_sentences(10)
