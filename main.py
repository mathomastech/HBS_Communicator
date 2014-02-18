from gi.repository import Gtk
from ui import *
import os.path


#Global Variables
f = open("config.txt", 'r')
configs = f.readline()
f.close()
config = configs.split(",")

LOG_PATH = config[0]
ACTIVE_LOG_PATH = config[1]
ROSTER_PATH = config[2]
ACTIVE_ROSTER_PATH = config[3]
USER_PATH = config[4]
USER = config[5]



def main():
    print("success")



gui.connect_signals(Handler())
loginWindow.connect_signals(Handler())
main_app.show_all()
Gtk.main()
