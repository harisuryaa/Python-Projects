from tkinter import *
import pandas
import random

try:
    word= pandas.read_csv("data/french_words.csv")
except FileNotFoundError:
    word_2 = pandas.read_csv("data/words_to_learn.csv")
    dict_words = word.to_dict(orient="records")
else:
    dict_words = word.to_dict(orient="records")
current_card={}

def next_card_n():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(dict_words)
    canvas.itemconfig(lang_f,text="Hindi",fill = "black")
    canvas.itemconfig(word_f,text=current_card["Hindi"],fill= "black")
    canvas.itemconfig(canvas_image, image=front)
    window.after(5000, func=change)

def next_card_s():

    dict_words.remove(current_card)
    data= pandas.DataFrame(dict_words)
    data.to_csv("data/words_to_learn.csv")

    next_card_n()


def change():
    canvas.itemconfig(canvas_image, image=back)
    canvas.itemconfig(lang_f, text= "English", fill = "white")
    canvas.itemconfig(word_f,text=current_card["Wordss"] ,fill = "white")

BACKGROUND_COLOR = "#B1DDC6"


window =Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer= window.after(3000, func=change)


#flash card
canvas = Canvas(width=800,height=526, highlightthickness=0,bg=BACKGROUND_COLOR )
front = PhotoImage(file="images/card_front.png")
back= PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400,263, image=front)
canvas.grid(row=0,column=1,columnspan=2)


#buttons
my_image = PhotoImage(file="images/right.png")
button_s = Button(image=my_image, highlightthickness=0, command=next_card_s)
button_s.grid(row=1,column=1)
my_image_n = PhotoImage(file="images/wrong.png")
button_n = Button(image=my_image_n, highlightthickness=0, command=next_card_n)
button_n.grid(row=1,column=2)
#text
lang_f = canvas.create_text(400,150, text="Language", font=("Ariel",40,"italic"))
word_f = canvas.create_text(400,263, text= "Words", font=("Ariel",60,"bold"))

next_card_n()
window.mainloop()