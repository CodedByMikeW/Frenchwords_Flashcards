from tkinter import *
import pandas
import random
import time
from pandas.core.interchange.dataframe_protocol import DataFrame



current_card={}
to_learn={}
BACKGROUND_COLOR = "#B1DDC6"
window=Tk()
window.title("My Tkinter App")
window.config(padx=50,pady=50 ,bg=BACKGROUND_COLOR)
try:
    data=pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("french_words.csv")
    print(original_data)
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")


def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    print(current_card["French"])
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_background,image=card_front_img)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(card_title,text="English",fill="white")
    #canvas.config(bg="#808080")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    canvas.itemconfig(card_background,image=card_back_img)
def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data=pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv",index=False)
    next_card()

flip_timer=window.after(3000,flip_card)
canvas = Canvas(width=800,height=526)
card_back_img = PhotoImage(file="card_back.png")
#canvas.create_image(400,263,image=old_image)
card_front_img= PhotoImage(file="card_front.png")
card_background=canvas.create_image(400,263,image=card_front_img)
card_title=canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
card_word=canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

cross_image=PhotoImage(file="wrong.png")
unknown_button = Button(image=cross_image,highlightthickness=0,command=next_card)
unknown_button.grid(row=1,column=0)


check_image = PhotoImage(file="right.png")
known_button=Button(image=check_image,highlightthickness=0,command=is_known)
known_button.grid(row=1,column=1)

next_card()


window.mainloop()






