import yt_dlp
from multiprocessing import Process, Pipe
from threading import Thread, Lock


class Logger:
    def debug(self, msg):
        pass

    def info(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


class Downloader:

    thread = Thread()
    # process = Process()
    terminate = False
    # mutex = Lock()

    def extract_formats(self, url: str, formats_extracted_hook):
        if self.thread.is_alive():
            print('killing thread and process')
            self.terminate = True
            self.thread.join()

        print('running thread')
        self.thread = Thread(
            target=watching_process, args=[url,
                                           self.terminate,
                                           # self.process,
                                           formats_extracted_hook]
        )
        self.thread.start()


def watching_process(url: str,
                     terminate: bool,
                     # process: Process,
                     formats_extracted_hook):
    # if process.is_alive():
        # process.kill()


    print('thread started')
    pipe, child_pipe = Pipe()
    process = Process(target=extract_formats_process, args=[url, child_pipe])
    process.start()
    print('process started')

    while True:
        if terminate is True:
            print('terminating process')
            pipe.close()
            process.kill()
            terminate = False
            return
        elif pipe.poll():
            print('process success')
            extracted_formats = pipe.recv()
            pipe.close()
            process.kill()
            formats_extracted_hook(extracted_formats)
            return
    print('end thread')


def extract_formats_process(url: str, pipe: Pipe):
    # url = 'https://youtu.be/K7JeTqXdH7I?si=5QWcs3OAMDKCKtHX'
    url = 'https://www.youtube.com/watch?v=lN2JuSx3vtY'

    # yt_dlp_opts = {
    #     'quiet': True,
    #     'logger': Logger(),
    #     # 'progress_hooks': [when_finished_hook]
    # }
    #
    # with yt_dlp.YoutubeDL(yt_dlp_opts) as ydl:
    #     ydl.extract_info(url, download=False)

    pipe.send('data extracted')
    pipe.close()
    print('process end')

# def when_finished_hook(info):
#     global stop_spinner_wrapper
#
#     if info['status'] == 'downloading':
#         print('downloading')
#
#     if info['status'] == 'finished':
#         print('finish')
#         stop_spinner_wrapper()
