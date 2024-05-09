import customtkinter as Ctk
import sounddevice as sd
from scipy.io.wavfile import write
from tkinter import messagebox
from PIL import Image
from tkinter.messagebox import askyesno
from tkinter.filedialog import askdirectory
import time


Ctk.set_appearance_mode("dark")
Ctk.set_default_color_theme("blue")

class VoiceRecorderApp:
    def __init__(self):
        self.root = root
        self.root.title("Voice Recorder")
        self.root.geometry("600x600")
        self.root.resizable(False,False)
        self.root.protocol("WM_DELETE_WINDOW",self.close)
        self.setup_ui()

    def setup_ui(self):
        self.recordlabel = Ctk.CTkLabel(root,text="Choose a Location and Enter Recording Duration in Seconds:", font=('FangSong ti', 16))
        self.recordlabel.place(x=10, y = 430)
        self.duration_entry = Ctk.CTkEntry(root, width=580)
        self.duration_entry.place(x= 10, y= 460)

        self.Record = Ctk.CTkButton(root, text="Record", height=30, width=100, command=self.record)
        self.Record.place(x=20, y= 550)

        self.Path = Ctk.CTkButton(root, text="Location", height=30, width=100, command=self.file_path)
        self.Path.place(x=140, y= 550)

        self.display = Ctk.CTkImage(dark_image=Image.open('microphone.png'), size=(400, 400))
        self.displayfig = Ctk.CTkLabel(root, image=self.display)
        self.displayfig.place(x=100, y=15)

        self.countdown = Ctk.CTkLabel(root,text ="Time Remaining:", font=('FangSong ti', 17))
        self.countdown.place(x=130, y=500)

        self.displaytime = Ctk.CTkLabel(root,text ="", font=('FangSong ti', 17))
        self.displaytime.place(x=300, y=500)

    def close(self):
        if askyesno("Close Voice Recorder", message='Are you sure you want to close the application?'):
            self.root.destroy()


    add=""

    def file_path(self):
        global add 
        add = askdirectory()

    def record(self):
        global add
        try:
            fs=44100 #sample_rate
            seconds=int(self.duration_entry.get())
            addr = add + "/" + "recording.wav"
            record_voice=sd.rec(seconds * fs,samplerate=fs,channels=2)    
            temp =seconds
            while temp>0:
                self.root.update()
                time.sleep(1)
                temp -= 1
                if (temp == 0):
                    messagebox.showinfo("Time Countdown", "Time's up!")
                self.displaytime.configure(text = f"{str(temp)}")
            sd.wait()
            write(addr,fs,record_voice)
        except:
            messagebox.showerror("Error", "Please enter a valid input!")

                
if __name__ == "__main__":
    root = Ctk.CTk()
    app = VoiceRecorderApp()
    root.mainloop()