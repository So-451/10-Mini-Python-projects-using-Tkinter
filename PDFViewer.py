from tkinter import*
import fitz
from tkinter.ttk import Progressbar
from threading import Thread
import math
from tkinter import filedialog



class PDFViewer:
    def __init__(self):
        self.root = root
        self.root.title("PDF Viewer")
        self.root.geometry("640x720")
        self.root.resizable(False,False)
        self.bar = True
        self.load="after"
        self.zoom_dpi=72
        self.img_object_li = []
        self.setup_ui()


    def pdf_view(self,pdf_location, bar, load):
       

        
        def add_img():
            precentage_dicide = 0
            open_pdf = fitz.open(pdf_location)

            for page in open_pdf:
                pix = page.get_pixmap()
                pix1 = fitz.Pixmap(pix,0) if pix.alpha else pix
                img = pix1.tobytes("ppm")
                timg = PhotoImage(data = img)
                self.img_object_li.append(timg)
                if bar==True and load=="after":
                    precentage_dicide = precentage_dicide + 1
                    percentage_view = (float(precentage_dicide)/float(len(open_pdf))*float(100))
                    self.loading['value'] = percentage_view
                    self.percentage_load.set(f"Please wait!, your pdf is loading {int(math.floor(percentage_view))}%")
            if bar==True and load=="after":
                self.loading.pack_forget()
                self.display_msg.pack_forget()

            for i in self.img_object_li:
                self.text.image_create(END,image=i)
                self.text.insert(END,"\n\n")
            self.text.configure(state="disabled")


        def start_pack():
            t1 = Thread(target=add_img)
            t1.start()

        if load=="after":
            root.after(580,start_pack)
        else:
            start_pack()

        return self.frame

    def reset(self):
        self.img_object_li=[]
        self.percentage_view = 0
        self.percentage_load = StringVar()
        self.text.delete(1.0, END)
     
    def zoom_in(self):
        global zoomdpi
        zoomdpi = 200
        self.text.configure(width=720+zoomdpi, height=720+zoomdpi)

    def zoom_out(self):
        self.zoom_dpi -= 10
        if self.zoom_dpi < 10:
            self.zoom_dpi = 10
        self.text.config(font=("Helvetica", self.zoom_dpi))

        



    def open_pdf(self):
        self.pdf_path = filedialog.askopenfilename(initialdir="E:/PDF/",
                                                   title="Open PDF File",
                                                   filetypes=[("PDF files", "*.pdf"),
                                                              ("All Files", "*.*")])
        if self.pdf_path:
            global d1
            d1 = PDFViewer().pdf_view(pdf_location=self.pdf_path, bar=True, load="after")
            d1.pack()

        

    def setup_ui(self ):
        

        
        self.my_menu = Menu(self.root)
        self.root.config(menu=self.my_menu)
        self.file_menu = Menu(self.my_menu, tearoff=False)
        self.my_menu.add_cascade(label="File", menu=self.file_menu)
        #self.my_menu.add_cascade(label="Zoom In", command=self.zoom_in)
        #self.my_menu.add_cascade(label="Zoom Out", command=self.zoom_out)
        self.file_menu.add_command(label="Open", command=self.open_pdf)
        #self.file_menu.add_command(label="Close current file", command=self.reset)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Quit", command=root.quit)


        self.frame = Frame(self.root,width= 720,height= 720,bg="white")

        self.scroll_y = Scrollbar(self.frame,orient="vertical")
        self.scroll_x = Scrollbar(self.frame,orient="horizontal")

        self.scroll_x.pack(fill="x",side="bottom")
        self.scroll_y.pack(fill="y",side="right")

        self.percentage_view = 0
        self.percentage_load = StringVar()

        if self.bar==True and self.load=="after":
            self.display_msg = Label(textvariable=self.percentage_load)
            self.display_msg.pack(pady=0)

            self.loading = Progressbar(self.frame,orient= HORIZONTAL,length=300,mode='determinate')
            self.loading.pack(side = TOP,fill=X)

        self.text = Text(self.frame,yscrollcommand=self.scroll_y.set,xscrollcommand= self.scroll_x.set,width= 760,height= 760)
        self.text.pack(side="left")

        self.scroll_x.config(command=self.text.xview)
        self.scroll_y.config(command=self.text.yview)


if __name__ == "__main__":
    root = Tk()
    app = PDFViewer()
    root.mainloop()