import yt_dlp


__set_fraction


class Logger:
    def info(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def download_status_hook(info):
    global __set_fraction

    if info['status'] == 'downloading':
        fraction = info['downloaded_bytes'] / info['total_bytes_estimate']
        __set_fraction(fraction)
    elif info['status'] == 'finished':
        __set_fraction(1.0)


def extract_formats(url, progress_bar):
    global __set_fraction
    __set_fraction = progress_bar.set_fraction

    url = 'https://youtu.be/K7JeTqXdH7I?si=5QWcs3OAMDKCKtHX'

    yt_dlp_opts = {
        'quiet': True,
        'logger': Logger(),
        'progress_hooks': [download_status_hook]
    }

    with yt_dlp.YoutubleDL(yt_dlp_opts) as ydl:
        ydl.extract_info(url)
