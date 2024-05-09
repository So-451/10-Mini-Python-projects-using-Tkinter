import customtkinter as Ctk
import threading 
from pytube import YouTube
from tkinter.messagebox import showinfo, showerror, askokcancel
from PIL import Image, ImageTk
import os



Ctk.set_appearance_mode("dark")
Ctk.set_default_color_theme("blue")

Values = ['360p','480p', '720p', '1080p']

class YT_Audio_Video_Downloader_APP:
    def __init__(self):
        self.root = root
        self.root.title("Audio-Video Downloader")
        self.root.geometry("600x500")
        self.root.resizable(False,False)
        #self.root.protocol("WM_DELETE_WINDOW",self.close)
        self.setup_ui()

    def mp3download(self):
        
        def download():
            link3 = self.MP3link.get()

            self.progressbarMP3.start()
            if link3 == '':
                showerror(title='Error', message='Please enter the MP3 URL')
            else:
                try:
                    def on_progress(stream, chunk, bytes_remaining):
                        total_size = stream.filesize
                        
                        def get_formatted_size(total_size, factor = 1024, suffix = 'B'):
                            for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
                                if total_size < factor:
                                    return f"{total_size:.2f}{unit}{suffix}"
                                total_size /=factor
                            return f"{total_size:.2f}Y{suffix}"
                        global formatted_size, percentage_completed 
                        formatted_size = get_formatted_size(total_size)

                        bytes_downloaded = total_size - bytes_remaining
                        percentage_completed = round(bytes_downloaded / total_size * 100)
                        
                        self.progressMP3_label.configure(text=str(percentage_completed) + '%, File size:'+ formatted_size)
                        root.update()
                    
                    audio = YouTube(link3, on_progress_callback=on_progress)
                    output = audio.streams.get_audio_only().download()
                    base, ext = os.path.splitext(output)
                    new_file = base + '.mp3'
                    self.progressbarMP3.stop()
                    self.progressbarMP3.set(0)
                    os.rename(output, new_file)
                    showinfo(title='Download Complete', message='MP3 has been succesfully downloaded.')
                
                except:  
                    self.progressMP3_label.configure(text="")
                    self.progressbarMP3.stop()
                    self.progressbarMP3.set(0) 
                    showerror(title='Download Error', message='An error occurred while trying to ' \
                    'download the MP3\nThe following could ' \
                    'be the causes:\n->Invalid link\n->No internet connection\n'\
                    'Make sure you have stable internet connection and the MP3 link is valid')
                    # ressetting the progress bar and the progress label
                    
                
                

        def downloadthread():
            t1 = threading.Thread(target=download)
            t1.start()
            self.progressMP3_label.configure(text="         Downloading....")

        downloadthread()

    def mp4download(self):  
        
        def download():
            link4 = str(self.MP4link.get())
            resolution = self.resolution.get()
            self.progressbarMP4.start()
            if link4 == '':
                showerror(title='Error', message='Please enter the MP4 URL')
            else:
                
                    def on_progress(stream, chunk, bytes_remaining):
                        total_size = stream.filesize
                            
                        def get_formatted_size(total_size, factor = 1024, suffix = 'B'):
                            for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
                                if total_size < factor:
                                    return f"{total_size:.2f}{unit}{suffix}"
                                total_size /=factor
                            return f"{total_size:.2f}Y{suffix}"
                        global formatted_size, percentage_completed 
                        formatted_size = get_formatted_size(total_size)

                        bytes_downloaded = total_size - bytes_remaining
                        percentage_completed = round(bytes_downloaded / total_size * 100)
                            
                        self.progressMP4_label.configure(text=str(percentage_completed) + '%, File size:'+ formatted_size)
                        root.update()
                        
                    url = YouTube(link4, on_progress_callback=on_progress)
                    
                    output = url.streams.filter(res=resolution).first()
                    output.download()
                    self.progressbarMP4.stop()
                    self.progressbarMP4.set(0)  
                    showinfo(title='Download Complete', message='MP4 has been succesfully downloaded.')
                    
        def downloadthread():
            t1 = threading.Thread(target=download)
            t1.start()
            self.progressMP4_label.configure(text="         Downloading....")

        downloadthread()    
        


    def clear(self):
        self.MP3link.delete(0,'end')
        self.progressMP3_label.configure(text="")
        self.MP4link.delete(0,'end')
        self.progressMP4_label.configure(text="")
        
    

    def setup_ui(self):

        my_tab = Ctk.CTkTabview(root, width=600, height= 500 )
        my_tab.pack()

        page1 = my_tab.add("Audio Downloader")
        page2 = my_tab.add("Video Downloader")

        self.display = Ctk.CTkImage(dark_image=Image.open('mp3.png'), size=(140, 140))
        self.displayfig = Ctk.CTkLabel(page1, text="",image=self.display)
        self.displayfig.place(x=50, y=20)

        self.audio = Ctk.CTkLabel(page1,text="Audio \n Downloader", font=('FangSong ti', 55))
        self.audio.place(x=195, y = 30)

        self.MP3 = Ctk.CTkLabel(page1,text="Enter MP3 URL: ", font=('FangSong ti', 20))
        self.MP3.place(x=15, y = 180)

        self.MP3link = Ctk.CTkEntry(page1, width=530, placeholder_text="https://youtu.be/ly2hioc")
        self.MP3link.place(x= 16, y= 210)

        self.clear_image= ImageTk.PhotoImage(Image.open("trash.png").resize((25,25)))
        self.clear_button = Ctk.CTkButton(self.root, text='',image=self.clear_image,width=30,height=30, fg_color="grey", hover_color="dark grey", command=self.clear)
        self.clear_button.place(x=555,y=250)

        self.progressMP3_label =Ctk.CTkLabel(page1, text='')
        self.progressMP3_label.place(x=230, y=260)

        self.progressbarMP3 = Ctk.CTkProgressBar(page1, orientation="horizontal", width=550, mode='determinate', height=12)
        self.progressbarMP3.set(0)
        self.progressbarMP3.place(x=16, y=305)

        self.dowloadAudio = Ctk.CTkButton(page1, text="Download MP3", height=30, width=100, command=self.mp3download)
        self.dowloadAudio.place(x=250, y= 360)

        self.display1 = Ctk.CTkImage(dark_image=Image.open('mp4.png'), size=(150, 150))
        self.displayfig1 = Ctk.CTkLabel(page2, text="",image=self.display1)
        self.displayfig1.place(x=30, y=20)

        self.video = Ctk.CTkLabel(page2,text="Video \n Downloader", font=('FangSong ti', 55))
        self.video.place(x=195, y = 30)


        self.MP4 = Ctk.CTkLabel(page2,text="Enter MP4 URL: ", font=('FangSong ti', 20))
        self.MP4.place(x=15, y = 180)
        
        self.MP4link = Ctk.CTkEntry(page2, width=530, placeholder_text="https://youtu.be/ly2hioc")
        self.MP4link.place(x= 16, y= 210)

        self.MP4 = Ctk.CTkLabel(page2,text="Resolution: ", font=('FangSong ti', 15))
        self.MP4.place(x=16, y = 240)

        self.resolution = Ctk.CTkComboBox(page2, values=Values, width=100, height=24)
        self.resolution.place(x=16, y=270)

        self.progressMP4_label =Ctk.CTkLabel(page2, text='')
        self.progressMP4_label.place(x=230, y=290)

        self.progressbarMP4 = Ctk.CTkProgressBar(page2, orientation="horizontal", width=550, mode='determinate', height=12)
        self.progressbarMP4.set(0)
        self.progressbarMP4.place(x=16, y=335)

        self.dowloadVideo = Ctk.CTkButton(page2, text="Download MP4", height=30, width=100, command=self.mp4download)
        self.dowloadVideo.place(x=250, y= 380)



if __name__ == "__main__":
    root = Ctk.CTk()
    app = YT_Audio_Video_Downloader_APP()
    root.mainloop()