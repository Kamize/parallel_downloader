import tkinter as tk
import tkinter.ttk as ttk
from tkinter.ttk import Progressbar

#import class downloader
# import downloader
from downloader import DownloadManager
#import path
from pathlib import Path
from urllib.parse import urlparse

FILE_URL = urlparse('http://127.0.0.1:5000/static/test.zip')
FILE_PATH = Path(FILE_URL.path)

OUTPUT_PATH = Path(__file__).parent

SPLIT_NUM = 10

class DownloadManagerGUI:
    def __init__(self, master):
        self.master = master
        self.create_widgets()
    
    def create_widgets(self):
        self.url_label = tk.Label(self.master, text="URL:")
        self.url_entry = tk.Entry(self.master)
        self.download_button = tk.Button(self.master, text="Download", command=self.download)
        self.progress_label = tk.Label(self.master, text="Progress:")
        self.progress_bar = ttk.Progressbar(self.master, orient="horizontal", length=500, mode="determinate")
        
        self.url_label.pack()
        self.url_entry.pack()
        self.download_button.pack()
        self.progress_label.pack()
        self.progress_bar.pack()
    
    def download(self):
        # get the URL from the entry widget
        #url = self.url_entry.get()
        #HARD CODED
        downloader = DownloadManager(FILE_URL)

        
        # download the file here and update the progress bar as the download progresses
        #self.progress_bar['value'] = current_progress

root = tk.Tk()
root.geometry("600x200")
app = DownloadManagerGUI(root)
root.mainloop()
