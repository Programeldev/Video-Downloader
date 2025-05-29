from gi.repository import Gtk


@Gtk.Template(resource_path='/com/github/Programeldev/VideoDownloader/formats_table.ui')
class FormatsTable(Gtk.ColumnView):
    __gtype_name__ = 'FormatsTable'
