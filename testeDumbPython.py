import tkinter as tk
import random

def show_popup():
    popup = tk.Toplevel(root)
    popup.title("Popup")
    label = tk.Label(popup, text="EU SABIA!!!")
    label.pack(padx=20, pady=20)

def move_button(event):
    x = random.randint(0, 350)
    y = random.randint(0, 350)
    no_button.place(x=x, y=y)

root = tk.Tk()
root.geometry("400x400")

question_label = tk.Label(root, text="Are you Dumb?")
question_label.pack(pady=20)

yes_button = tk.Button(root, text="Sim", command=show_popup)
yes_button.pack()

no_button = tk.Button(root, text="Não")
no_button.pack()

no_button.bind("<Enter>", move_button)

root.mainloop()