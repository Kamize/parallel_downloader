import tkinter as tk
from tkinter import ttk
import multiprocessing
import requests

FILE_URL = 'http://127.0.0.1:5000/static/test.zip'
SPLIT_NUM = 10

def main():
    content = parallel_download(FILE_URL)

    with open('test.zip', 'wb') as f:
        f.write(content)

def parallel_download(url):
    file_length = int(requests.head(url).headers['Content-Length'])
    chunk_size = file_length//SPLIT_NUM

    content = b''

    for start in range(0, file_length, chunk_size):
        # Change this part to implement parallelization
        partial_content = partial_download(url, start, chunk_size)
        content += partial_content
    
    return content

def partial_download(url, start_byte, chunk_size):
    headers = {'Range': f'bytes={start_byte}-{start_byte+chunk_size-1}'}

    stream = requests.get(FILE_URL, headers=headers)

    return stream.content

# Create the main window
root = tk.Tk()
root.title('Download Manager')

# Create the progress bar
progress_bar = ttk.Progressbar(root, orient='horizontal', length=200, mode='determinate')
progress_bar.pack()

# Create the download button
download_button = tk.Button(root, text='Download', command=main)
download_button.pack()

root.mainloop()
