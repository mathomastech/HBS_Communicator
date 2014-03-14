from gi.repository import Gtk
from config import Configuration

#Initialize communicator XML objects
gui = Gtk.Builder()
gui.add_from_file("communicator.glade")
main_app = gui.get_object("hbsCommunicator")

#Initialize loginWindow XML objects
loginWindow = Gtk.Builder()
loginWindow.add_from_file("loginWindow.glade")
authorize = loginWindow.get_object("loginWindow")

#Command Buttons
central_command_button = gui.get_object("centralCommandButton")
operations_command_button = gui.get_object("operationsCommandButton")
cod_command_button = gui.get_object("codCommandButton")
rust_command_button = gui.get_object("rustCommandButton")
gw_command_button = gui.get_object("gwCommandButton")
wow_command_button = gui.get_object("wowCommandButton")
mc_command_button = gui.get_object("mcCommandButton")
arma_command_button = gui.get_object("armaCommandButton")
logistics_command_button = gui.get_object("logisticsCommandButton")
mp_command_button = gui.get_object("mpCommandButton")
admissions_command_button = gui.get_object("admissionsCommandButton")
#General Buttons
general_button = gui.get_object("generalButton")
cod_general_button = gui.get_object("ccodGeneralButton")
rust_general_button = gui.get_object("rustGeneralButton")
gw_general_button = gui.get_object("gwGeneralButton")
wow_general_button = gui.get_object("wowGeneralButton")
mc_general_button = gui.get_object("mcGeneralButton")
arma_general_button = gui.get_object("armaGeneralButton")
#Channel and Roster Elements
chat_entry = gui.get_object("chatEntry")
submit_button = gui.get_object("submitButton")
info_display = gui.get_object("infoDisplay")
roster_display = gui.get_object("rosterDisplay")
#Login Window Text Entrys
login_button = gui.get_object("loginWindowButton")
username_entry = loginWindow.get_object("usernameEntry")
password_entry = loginWindow.get_object("passwordEntry")
login_status_label = loginWindow.get_object("loginStatusLabel")

LOG_PATH = Configuration.c['Logs']
ROSTER_PATH = Configuration.c['Rosters']
DB_IP = Configuration.c['DB IP']
DB_NAME = Configuration.c['DB Name']
DB_USER = Configuration.c['DB User']
DB_PASSWORD = Configuration.c['DB Password']
