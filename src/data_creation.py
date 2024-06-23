import tkinter as tk
from tkinter import font
import os
import sys
import pandas as pd
dir2_path: str = os.path.normpath(os.path.join(os.path.dirname(__file__), '../res'))
sys.path.append(dir2_path)
import constants as res
dir2_path: str = os.path.normpath(os.path.join(os.path.dirname(__file__), '../database'))
sys.path.append(dir2_path)
import sentences as db

def create_ui(sentences):
    def on_yes():
        db.update_hard_by_index(1, True)
        get_next_sentence()

    def on_no():
        db.update_hard_by_index(1, False)
        get_next_sentence()

    def get_next_sentence():
        try:
            sentence = next(sentences)
            label.config(text=sentence)
        except StopIteration:
            root.quit()

    root = tk.Tk()
    root.title("Data creations")
    root.geometry("800x400")  

    label_font = font.Font(root, family="Helvetica", size=24, weight="bold")
    button_font = font.Font(root, family="Helvetica", size=18)

    label = tk.Label(root, text='', font=label_font)
    label.pack(pady=50)  

    button_frame = tk.Frame(root)
    button_frame.pack(pady=20)  

    yes_button = tk.Button(button_frame, text="Yes", font=button_font, width=10, command=on_yes)
    yes_button.grid(row=0, column=0, padx=20)  

    no_button = tk.Button(button_frame, text="No", font=button_font, width=10, command=on_no)
    no_button.grid(row=0, column=1, padx=20)  

    get_next_sentence()

    root.mainloop()

def get_sentences():
    sentences = pd.read_csv(res.sentences_path)
    sentences = sentences[sentences['hard'].isnull()]
    for sentence in sentences['sentence']:
        yield sentence

def get_db_sentences():
    sentences = db.get_all_sentences()
    sentences = sentences[sentences['hard'].isnull()]
    for sentence in sentences:
        yield sentence[1]
            

if __name__ == "__main__":
    sentences = get_db_sentences()
    create_ui(sentences)