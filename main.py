from gui import *
from communicator import *
from handler import *

def main():
    GUI.APP.connect_signals(Handler())
    GUI.LOGIN_WINDOW.connect_signals(Handler())
    GUI.MAIN_APP.show_all()
    GUI.AUTHORIZE_WINDOW.show_all()
    Gtk.main()


main()
