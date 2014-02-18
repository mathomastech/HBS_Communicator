from configuration import *
from communicator import *
from handler import *

def main():
    print("success")



gui.connect_signals(Handler())
loginWindow.connect_signals(Handler())
main_app.show_all()
Gtk.main()
