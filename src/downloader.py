import yt_dlp
from multiprocessing import Process, Pipe
from threading import Thread, Lock
from time import sleep


# terminate = False


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

    def extract_formats(self, url: str, formats_extracted_callable):
        if self.thread.is_alive():
            print('killing thread and process')
            self.thread.terminate()

        print('running thread')

        self.thread = WatchingProcessThread(url, formats_extracted_callable)
        # self.thread.start()
        # self.thread = Thread(
        #     target=watching_process, args=[url,
        #                                    # self.terminate,
        #                                    # self.process,
        #                                    formats_extracted_hook]
        # )
        # self.thread.start()


class WatchingProcessThread(Thread):

    __terminate = False
    url: str
    formats_extracted_callable = None

    def __init__(self, url: str, formats_extracted_callable):
        super().__init__()
        self.url = url
        self.formats_extracted_callable = formats_extracted_callable
        self.start()

    def run(self):
        print('thread started')
        pipe, p_pipe = Pipe()
        process = Process(
            target=extract_formats_process,
            args=[self.url, p_pipe]
        )
        process.start()
        print('process started')

        while True:
            if self.__terminate is True:
                print('terminating process')
                pipe.close()
                process.terminate()
                process.join()
                break
            elif pipe.poll():
                print('process success')
                extracted_formats = str(pipe.recv())
                pipe.close()
                process.kill()
                self.formats_extracted_callable(extracted_formats)
                break
        print('end thread')

    def terminate(self):
        self.__terminate = True
        self.join()


def extract_formats_process(url: str, pipe: Pipe):
    # url = 'https://youtu.be/K7JeTqXdH7I?si=5QWcs3OAMDKCKtHX'
    url = 'https://www.youtube.com/watch?v=lN2JuSx3vtY'

    # yt_dlp_opts = {
    #     'quiet': True,
        # 'logger': Logger(),
    #     # 'progress_hooks': [when_finished_hook]
    # }
    #
    # with yt_dlp.YoutubeDL(yt_dlp_opts) as ydl:
    #     ydl.extract_info(url, download=False)

    sleep(5)
    pipe.send('piped extracted')
    pipe.close()
    print('process end')
