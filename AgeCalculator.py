from tkinter import messagebox
from datetime import datetime
import customtkinter as Ctk

Ctk.set_appearance_mode("dark")
Ctk.set_default_color_theme("blue")

class AgeCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Age Calculator")
        self.root.geometry("800x450")
        root.resizable(False,False)
        self.setup_ui()

    def setup_ui(self):
        my_font1 = Ctk.CTkFont(family="fangsong ti",size=75, weight = "normal")
        my_font2 = Ctk.CTkFont(family="fangsong ti", size=14, weight="normal")

        self.label_instructions = Ctk.CTkLabel(self.root, text="AGE CALCULATOR", font= my_font1)
        self.label_instructions.pack(padx=60,pady=90)


        self.label_instructions = Ctk.CTkLabel(self.root, text="Enter your birthdate: ", font=my_font2)
        self.label_instructions.pack(pady=10)

        self.calendar_entry = Ctk.CTkEntry(self.root, width=200, placeholder_text="DD-MM-YYYY")
        self.calendar_entry.pack(pady=10)

        self.button_calculate = Ctk.CTkButton(self.root, text="Calculate Age", command=self.calculate_age, fg_color="blue", font=my_font2)
        self.button_calculate.pack(pady=10)

    def calculate_age(self):
        birthdate_str = self.calendar_entry.get()
        try:
            birthdate = datetime.strptime(birthdate_str, "%d-%m-%Y")
            today = datetime.now()
            age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
            messagebox.showinfo("Age", f"Your age is {age} years")
        except ValueError:
            messagebox.showerror("Error", "Please select a valid date")

if __name__ == "__main__":
    root = Ctk.CTk()
    app = AgeCalculatorApp(root)
    root.mainloop()
