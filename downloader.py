import multiprocessing
import requests

class DownloadManager:
    def __init__(self, file_url, file_path, output_path, split_num):
        self.file_url = file_url
        self.file_path = file_path
        self.output_path = output_path
        self.split_num = split_num

    def main(self):
        content = self.parallel_download(self.file_url)

        with open(self.output_path/self.file_path.name, 'wb') as f:
            f.write(content)

    def parallel_download(self, url):
        file_length = int(requests.head(url).headers['Content-Length'])
        print(file_length)
        chunk_size = file_length//self.split_num
        print(chunk_size)

        content = b''

        for start in range(0, file_length, chunk_size):
            # Change this part to implement parallelization
            partial_content = self.partial_download(url, start, chunk_size)
            content += partial_content
        
        return content

    def partial_download(self, url, start_byte, chunk_size):
        headers = {'Range': f'bytes={start_byte}-{start_byte+chunk_size-1}'}

        print(headers['Range'])
        stream = requests.get(self.file_url, headers=headers)

        return stream.content

#How to run 
#download_manager = DownloadManager(FILE_URL, FILE_PATH, OUTPUT_PATH, SPLIT_NUM)
#download_manager.main()