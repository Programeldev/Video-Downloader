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

from gi.repository import Gtk
# from downloader import extract_formats
from .downloader import extract_formats


@Gtk.Template(resource_path='/com/github/Programeldev/VideoDownloader/window.ui')
class VideoDownloaderWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'VideoDownloaderWindow'

    image = Gtk.Template.Child()
    url_entry = Gtk.Template.Child()
    extract_info_button = Gtk.Template.Child()
    formats_box = Gtk.Template.Child()

    no_image: Gtk.Picture

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.image.set_resource('/images/no-image.png')

        self.set_size_request(400, 350)
        self.extract_info_button.connect('clicked', self.extract_info)
        # self.formats_box.set_size_request(340, 200)

    def extract_info(self, button):
        url = self.url_entry.get_buffer().get_text()
        if not url:
            return

        progress = Gtk.ProgressBar()
        self.formats_box.append(progress)

        extract_formats('', progress)
