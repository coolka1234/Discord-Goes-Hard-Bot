import tkinter as tk
from tkinter import font

def create_ui():
    root = tk.Tk()
    root.title("Simple UI")
    root.geometry("800x400")  

    label_font = font.Font(root, family="Helvetica", size=24, weight="bold")
    button_font = font.Font(root, family="Helvetica", size=18)

    label = tk.Label(root, text="Please make a choice:", font=label_font)
    label.pack(pady=50)  

    button_frame = tk.Frame(root)
    button_frame.pack(pady=20)  

    yes_button = tk.Button(button_frame, text="Yes", font=button_font, width=10)
    yes_button.grid(row=0, column=0, padx=20)  

    no_button = tk.Button(button_frame, text="No", font=button_font, width=10)
    no_button.grid(row=0, column=1, padx=20)  

    root.mainloop()

if __name__ == "__main__":
    create_ui()
