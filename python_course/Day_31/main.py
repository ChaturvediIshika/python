from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data=pandas.read_csv("data/words_to_learn")
except FileNotFoundError:
    data=pandas.read_csv("data/french_words.csv")
to_learn=data.to_dict(orient="records")
current_card={}

def next_card():
    global current_card,timer
    window.after_cancel(timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(title,text="French",fill="black")
    canvas.itemconfig(word,text=current_card["French"],fill="black")
    canvas.itemconfig(image,image=front_img)
    timer=window.after(3000,func=flip_card)

def flip_card():
    canvas.itemconfig(title,text="English",fill="white")
    canvas.itemconfig(word,text=current_card["English"],fill="white")
    canvas.itemconfig(image,image=back_img)

def is_known():
    to_learn.remove(current_card)
    data=pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn",index=False)
    next_card()

window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

timer=window.after(3000,func=flip_card)

canvas=Canvas(width=800,height=526)
front_img=PhotoImage(file="images/card_front.png")
back_img=PhotoImage(file="images/card_back.png")
image=canvas.create_image(400,263,image=front_img)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
title=canvas.create_text(400,150,text="Title",font=("Ariel",40,"italic"))
word=canvas.create_text(400,263,text="Word",font=("Ariel",60,"bold"))
canvas.grid(column=0,row=0,columnspan=2)

cross_img=PhotoImage(file="images/wrong.png")
wrong=Button(image=cross_img,highlightthickness=0,command=next_card)
wrong.grid(column=0,row=1)

check_img=PhotoImage(file="images/right.png")
right=Button(image=check_img,highlightthickness=0,command=is_known)
right.grid(column=1,row=1)

next_card()

window.mainloop()
