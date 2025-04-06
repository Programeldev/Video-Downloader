# window.py
#
# Copyright 2025 Unknown
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: LGPL-3.0-or-later

from multiprocessing import Process

from gi.repository import Gtk
# from .downloader import stop_spinner_wrapper, extract_formats
# import video_downloader.downloader as downloader
from .downloader import Downloader


@Gtk.Template(resource_path='/com/github/Programeldev/VideoDownloader/window.ui')
class VideoDownloaderWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'VideoDownloaderWindow'

    image = Gtk.Template.Child()
    url_entry = Gtk.Template.Child()
    extract_info_button = Gtk.Template.Child()
    formats_box = Gtk.Template.Child()

    spinner = Gtk.Spinner()
    downloading_process = Process()

    downloader = Downloader()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.image.set_resource('/images/no-image.png')

        self.set_size_request(400, 350)
        self.extract_info_button.connect('clicked', self.extract_info)

    def extract_info(self, button):
        url = self.url_entry.get_buffer().get_text()
        if not url:
            return

        self.downloader.extract_formats(url, self.show_extracted_info)

    def show_extracted_info(self, extracted_info):
        print(extracted_info)
    # def extract_info(self, button):
    #     url = self.url_entry.get_buffer().get_text()
    #     if not url:
    #         return
    #
    #     if self.downloading_process.is_alive():
    #         self.downloading_process.terminate()
    #         self.downloading_process.close()
    #
    #     self.spinner.start()
    #     self.formats_box.append(self.spinner)
    #
    #     # Thread(target=downloader.extract_formats, args=[url]).start()
    #     self.downloading_process = Process(
    #         target=downloader.extract_formats,
    #         args=[url, self.spinner.stop]
    #     )
    #     self.downloading_process.start()
    #
    #     print('end extract')
