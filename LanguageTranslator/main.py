import customtkinter as Ctk
from tkinter import *
from PIL import Image, ImageTk
import googletrans
from googletrans import *
from tkinter.messagebox import askyesno
import pyttsx3
import pyperclip

Ctk.set_appearance_mode("dark")
Ctk.set_default_color_theme("blue")


languages = googletrans.LANGUAGES
Values = list(languages.values())
#Values1 = [Value.capitalize() for Value in Values]

engine = pyttsx3.init()


class LanguageTrans:
    def __init__(self):
        self.root = root
        self.root.title("Language Translator")
        self.root.geometry("700x520")
        self.root.resizable(False,False)
        self.root.protocol("WM_DELETE_WINDOW",self.close)
        self.setup_ui()


    def translate_text(self):
        text = self.langfrom.get()
        textto=self.langto.get()
        translator = Translator()
        for key, Values in languages.items():
            if (Values == text):
                from_language_key = key
        for key, Values in languages.items():
            if (Values == textto):
                to_language_key = key

        translated = translator.translate(text=self.textfrom.get(1.0, END), src=from_language_key, dest=to_language_key)
        
        self.textto.delete(1.0, END)
        self.textto.insert(END,translated.text)
        self.textpronounciation.delete(1.0, END)
        self.textpronounciation.insert(END,translated.pronunciation)


    def speak(self):
        text=self.textto.get('1.0', Ctk.END)
        engine.say(text)
        engine.runAndWait()

    def copy(self):
        text=self.textto.get('1.0', Ctk.END)
        pyperclip.copy(text)
        
    def clear(self):
        self.textfrom.delete("1.0", "end")
        self.textto.delete("1.0", "end")
        self.textpronounciation.delete("1.0", "end")

    def close(self):
        if askyesno("Close Easy Translator?", message='Are you sure you want to close the application?'):
            self.root.destroy()

    def setup_ui(self):

        self.display = Ctk.CTkImage(dark_image=Image.open('translate.png'), size=(100, 100))
        self.displayfig = Ctk.CTkLabel(root, text="",image=self.display)
        self.displayfig.place(x=50, y=20)

        self.displattext = Ctk.CTkLabel(self.root, text="Easy Translate", font=('FangSong ti', 55))
        self.displattext.place(x=180, y=50)

        
        self.langfrom = Ctk.CTkComboBox(self.root, values=Values, width=280, height=30)
        self.langfrom.place(x=40, y=160)

        self.langto = Ctk.CTkComboBox(self.root, values=Values, width=280, height=30)
        self.langto.place(x=370, y=160)

        self.textfrom = Ctk.CTkTextbox(self.root,width=275, height=200)
        self.textfrom.place(x=44, y= 220)

        self.textto = Ctk.CTkTextbox(self.root,width=275, height=100)
        self.textto.place(x=374, y= 220)

        self.textpronounciation = Ctk.CTkTextbox(self.root,width=275, height=100)
        self.textpronounciation.place(x=374, y= 320)

        self.speak_image= ImageTk.PhotoImage(Image.open("speak.png").resize((25,25)))
        self.speak_button = Ctk.CTkButton(self.root, text='',image=self.speak_image,width=30,height=30, fg_color="grey",hover_color="dark grey", command=self.speak)
        self.speak_button.place(x=374,y=428)

        self.copy_image= ImageTk.PhotoImage(Image.open("copy.png").resize((25,25)))
        self.copy_button = Ctk.CTkButton(self.root, text='',image=self.copy_image,width=30,height=30, fg_color="grey", hover_color="dark grey", command=self.copy)
        self.copy_button.place(x=424,y=428)

        self.clear_image= ImageTk.PhotoImage(Image.open("trash.png").resize((25,25)))
        self.clear_button = Ctk.CTkButton(self.root, text='',image=self.clear_image,width=30,height=30, fg_color="grey", hover_color="dark grey", command=self.clear)
        self.clear_button.place(x=50,y=428)


        self.translate = Ctk.CTkButton(self.root, text='Translate', width=100, height=30, command=self.translate_text)
        self.translate.place(x=290, y=480)

        

if __name__ == "__main__":
    root = Ctk.CTk()
    app = LanguageTrans()
    root.mainloop()