import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox
import requests


def convert():
    amount = float(Amount.get())
    From = From_combobox.get()
    To = To_combobox.get()
    converted_amount = requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from={From}&to={To}")
   
    if converted_amount.status_code == 200:
        converted = converted_amount.json()["rates"][To]
        Result['text'] = f'{converted}'
    else:
        Result['text'] = f'Error!'  


root = Tk()
root.title("Currency Converter")
root.geometry("450x500")
root.resizable(False,False)
root.config(bg="white smoke")



Top_frame=Frame(root, bg="RoyalBlue4",width= 450, height= 140)
Top_frame.pack()

Label(Top_frame, text= "CURRENCY CONVERTER",font="arial 20 bold",bg="RoyalBlue4",fg="white").place(x=50, y=50)

Label(root, text="FROM:", font="arial 15 bold", fg="RoyalBlue4").place(x=40,y=160)
Label(root, text="TO:", font="arial 15 bold", fg="RoyalBlue4").place(x=260,y=160)
Label(root, text="AMOUNT:", font="arial 15 bold", fg="RoyalBlue4").place(x=40,y=260)
Label(root, text="RESULT:", font="arial 15 bold", fg="RoyalBlue4").place(x=260,y=260)

Values = ['USD', 'CAD', 'EUR', 'INR','JPY','AUD', 'CNY','KWD','BHD', 'OMR','GBP', 'JOD', 'KYD', 'CHF', 'KRW']

From_combobox=Combobox(root, values=Values,font="arial 14",state='r', width=10)
From_combobox.place(x=40,y=200)
From_combobox.current(0)

To_combobox=Combobox(root,values=Values,font="arial 14",state='r', width=10)
To_combobox.place(x=260,y=200)
To_combobox.current(1)

Amount=Entry(root, font="Robote 15", width= 12)
Amount.place(x=40, y=300)

btn=Button(root,text="Convert",fg="white", bg="RoyalBlue4", width=20, height=2,font="arial 14 bold",borderwidth=5, command=convert)
btn.place(x=100,y=380)

Result = Label(root, text=" ", anchor="w", width=12,font=('Robote 15'),relief="groove", bg="white")
Result.place(x=260, y=300)

root.mainloop()