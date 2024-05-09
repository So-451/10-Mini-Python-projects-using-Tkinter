import customtkinter as Ctk
import re
from nltk.corpus import words
from tkinter.messagebox import askyesno
from textblob import TextBlob
#from nltk.metrics.distance import edit_distance


nltk_words = set(words.words())
Ctk.set_appearance_mode("dark")
Ctk.set_default_color_theme("green")



class SpellChecker:
    def __init__(self):
        self.root = root
        self.root.title("Spell Checker")
        self.root.geometry("800x500")
        self.root.resizable(False,False)
        self.root.protocol("WM_DELETE_WINDOW",self.close)
        self.old_spaces = 0
        self.setup_ui()

    def setup_ui(self):
        self.Label = Ctk.CTkLabel(self.root,text="Real-Time Spelling Checker", font=('FangSong ti', 45))
        self.Label.place(x=30, y = 30)

        self.Text = Ctk.CTkTextbox(self.root, width=720, height=300, font=('Robote', 20))
        self.Text.bind('<KeyRelease>', self.check)
        self.Text.place(x=30, y= 120)

        self.Clear = Ctk.CTkButton(self.root, text="CLEAR", height=30, width=100, command=self.clear)
        self.Clear.place(x=650, y= 420)

        self.FixError = Ctk.CTkButton(self.root, text="FIX ERRORS", height=30, width=100, command=self.fixerrors)
        self.FixError.place(x=550, y= 420)

    def clear(self):
        self.Text.delete("1.0", "end")

    def close(self):
        if askyesno("Close Real-Time Spelling Checker", message='Are you sure you want to close the application?'):
            self.root.destroy()

    def check(self, event):
        content = self.Text.get('1.0', Ctk.END)
        space_count = content.count(' ')


        if space_count != self.old_spaces:
            self.old_spaces = space_count

            for tag in self.Text.tag_names():
                self.Text.tag_delete(tag)


            for word in content.split(' '):
                if re.sub(r"[^\w]", "", word.lower()) not in nltk_words:
                    position = content.find(word)
                    self.Text.tag_add(word, f'1.{position}', f'1.{position + len(word)}')
                    self.Text.tag_config(word, foreground = 'red')

    def fixerrors(self):
        get_text = self.Text.get('1.0', Ctk.END)
        self.Text.delete(1.0, Ctk.END)
        blobby = TextBlob(get_text)
        self.Text.insert(1.0, blobby.correct())

if __name__ == "__main__":
    root = Ctk.CTk()
    app = SpellChecker()
    root.mainloop()
    




