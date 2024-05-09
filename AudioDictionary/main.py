import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import pyttsx3
from PyDictionary import PyDictionary

root = Tk()
root.title("Audio Dictionary")
root.geometry("720x550")
root.resizable(False,False)
root.config(bg="brown")

engine = pyttsx3.init()
dictionary = PyDictionary()


def speaknow(text):
    engine.say(text)
    engine.runAndWait()

def clear():
    word.delete(0, END)

def search():
    text = word.get()
    try:
        # Look up the word in the dictionary
        meaning = dictionary.meaning(text)
        if meaning:
            display_definition['text'] = f'{meaning}' 

            speaknow(meaning)
        else:
            return "Word not found in the dictionary."
    except Exception as e:
        return str(e)

Top_frame = Frame(root, bg = "white", width= 750, height= 140)
Top_frame.pack()

Label(Top_frame, text= "Audio Dictionary",font="Cambria 40 ", bg="white").place(x=178, y=50)

word=Entry(root, font="Cambria 17", relief="groove",width= 49)
word.place(x=30, y=150)

search_meaning = PhotoImage(file="search.png")
search_meaning_photo = search_meaning.subsample(20,20)
searchbtn = Button(root, image=search_meaning_photo, bg="white", width=30, command=search)
searchbtn.place(x=635, y=150)

display_definition = Label(root,text=" ", justify="left", anchor="nw",wraplength=650, width=98, height=16,font='Cambria 10',relief="groove", bg="white")
display_definition.place(x=12, y=260)

clearbtn = Button(root, text="Clear",width=15, bg="white", font='Cambria 13',command=clear)
clearbtn.place(x=30, y=200)

root.mainloop()