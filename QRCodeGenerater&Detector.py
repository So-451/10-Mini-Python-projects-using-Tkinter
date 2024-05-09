import customtkinter as Ctk
import pyqrcode
from tkinter import filedialog
from PIL import Image
from pyzbar.pyzbar import decode
from tkinter import messagebox
from tkinter.messagebox import askyesno
import pyperclip

Ctk.set_appearance_mode("dark")
Ctk.set_default_color_theme("blue")

class QRCodeApp:
    def __init__(self):
        self.root = root
        self.root.title("QR Code Generator-Detector")
        self.root.geometry("600x600")
        self.root.resizable(False,False)
        self.root.protocol("WM_DELETE_WINDOW",self.close)
        self.setup_ui()

    def copy(self):
        text=self.displayQRdata.cget("text")
        pyperclip.copy(text)
    
    def setup_ui(self):

        my_tab = Ctk.CTkTabview(root, width=600, height= 600 )
        my_tab.pack()

        page1 = my_tab.add("Generate QR code" )
        page2 = my_tab.add("Decode QR code")

        self.QRcode_data = Ctk.CTkLabel(page1,text="QRcode Data", font=('FangSong ti', 15))
        self.QRcode_data.place(x=10, y = 420)
        
        self.Filename = Ctk.CTkLabel(page1,text="Filename", font=('FangSong ti', 15))
        self.Filename.place(x=10, y = 460)

        self.QRcode_data_entry = Ctk.CTkEntry(page1, width=450, placeholder_text="https://www.theqrcode.com")
        self.QRcode_data_entry.place(x= 120, y = 420 )

        self.Filename_entry = Ctk.CTkEntry(page1, width=450, placeholder_text="profile")
        self.Filename_entry.place(x= 120, y= 460)

        self.Reset = Ctk.CTkButton(page1, text="Reset", height=30, width=100, command=self.reset)
        self.Reset.place(x=340, y= 510)

        self.Generate_QRcode = Ctk.CTkButton(page1, text="Generate QRCode", height=30, width=119, command=self.generateQRcode)
        self.Generate_QRcode.place(x=450, y= 510)

        self.my_label = Ctk.CTkLabel(page1, text='')
        self.my_label.place(x=140, y = 50)
    

        self.input_path_entry = Ctk.CTkEntry(page2, width=500)
        self.input_path_entry.pack(padx= 180,pady = 25)

        self.displayQRcode_data = Ctk.CTkLabel(page2,text="Data Decoded:", font=('FangSong ti', 15))
        self.displayQRcode_data.place(x=40, y = 60)

        self.displayfilelocation = Ctk.CTkLabel(page2,text="File Location:", font=('FangSong ti', 15))
        self.displayfilelocation.place(x=40, y = 23)

        self.selectimage = Ctk.CTkButton(page2, text="Select Image", height=30, width=100, command=self.select_image)
        self.selectimage.place(x= 30, y = 500)

        self.detectqrcode = Ctk.CTkButton(page2, text="Detect QR Code", height=30, width=100, command=self.detectQRcode)
        self.detectqrcode.place(x=140, y = 500)

        self.displayQR = Ctk.CTkLabel(page2, text='')
        self.displayQR.place(x=170, y = 230)

        self.displayFrame=Ctk.CTkFrame(page2, width=523, height=120, border_width=2, border_color="grey")
        self.displayFrame.place(x = 30, y = 90)

        self.displayQRdata = Ctk.CTkLabel(page2, text='', anchor= "center", wraplength=500)
        self.displayQRdata.pack(pady = 15)

        self.copyy = Ctk.CTkButton(page2, text='Copy Data', height=30, width=100, command=self.copy)
        self.copyy.place(x=250, y=500)

    def close(self):
        if askyesno("Close QR Code Generator and Decoder", message='Are you sure you want to close the application?'):
            self.root.destroy()
        

    def generateQRcode(self):
        try:
            entry = self.Filename_entry.get()
            url = self.QRcode_data_entry.get()
            data = f'Filename: "{ entry}" \n URL: "{ url}" '
            input_path = filedialog.asksaveasfilename(title = "Save Image", 
                initialfile=f'{entry}',
                filetyp= (("PNG File" , ".png"), ("All Files", "*.*")))

            if input_path:
                if input_path.endswith(".png"):
                    get_code = pyqrcode.create(data)
                    get_code.png(input_path, scale = 10)

                else:
                    input_path = f'{input_path}.png'
                    get_code = pyqrcode.create(data)
                    get_code.png(input_path, scale = 10)


                global get_image
                get_image = Ctk.CTkImage(Image.open(input_path), size = (300,300))
                self.my_label.configure(image = get_image)

        except:
            messagebox.showwarning("Error", "Please enter a valid input!")

    

    def reset(self):
        self.Filename_entry.delete(0, Ctk.END)
        self.QRcode_data_entry.delete(0,Ctk.END)
        self.my_label.configure(image ='')

    def select_image(self):
        input_path = filedialog.askopenfilename(title = "Open Image", 
            filetyp= (("PNG File" , ".png"), ("All Files", "*.*")))
        
        if input_path:
            self.input_path_entry.delete(0, Ctk.END)
            self.input_path_entry.insert(0, input_path) 
            global get_image
            get_image = Ctk.CTkImage(Image.open(input_path), size = (250,250))
            self.displayQR.configure(image = get_image)

    def detectQRcode(self):
        input_path = self.input_path_entry.get()
        if input_path:
            global get_image
            get_image = Ctk.CTkImage(Image.open(input_path), size = (250,250))
            self.displayQR.configure(image = get_image)
            decode_QR = decode(Image.open(input_path))
            self.displayQRdata.configure(text=f"{decode_QR[0].data.decode('ascii')}")

if __name__ == "__main__":
    root = Ctk.CTk()
    app = QRCodeApp()
    root.mainloop()