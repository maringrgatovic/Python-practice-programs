import tkinter as tk
import random

def roll_random_dice():
    number_label["text"] = str(random.randint(1,6))

window = tk.Tk()
window.title("Dice Roll")

window.columnconfigure(0, weight=1, minsize=300)
window.rowconfigure([0,1], weight=1, minsize=100)

roll_button = tk.Button(text="Roll", command=roll_random_dice)
roll_button.grid(row=0, column=0, sticky="nesw")

number_label = tk.Label(text=' ')
number_label.grid(row=1, column=0, sticky="nesw")

dice_value = roll_random_dice

window.mainloop()

