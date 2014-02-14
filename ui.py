from gi.repository import Gtk
# instantiate XML object
gui = Gtk.Builder()
gui.add_from_file("communicator.glade")
app = gui.get_object("hbsCommunicator")

hbs_communicator = gui.get_object("hbsCommunicator")
com_window = gui.get_object("comWindow")
nav_box = gui.get_object("navBox")
channel_label = gui.get_object("channelLabel")
channel_notebook = gui.get_object("channelNotebook")
command_nav_box = gui.get_object("commandNavBox")
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
command_tab = gui.get_object("commandTab")
general_nav_box = gui.get_object("generalNavBox")
general_button = gui.get_object("generalButton")
cod_general_button = gui.get_object("ccodGeneralButton")
rust_general_button = gui.get_object("rustGeneralButton")
gw_general_button = gui.get_object("gwGeneralButton")
wow_general_button = gui.get_object("wowGeneralButton")
mc_general_button = gui.get_object("mcGeneralButton")
arma_general_button = gui.get_object("armaGeneralButton")
general_tab = gui.get_object("generalTab")
content_grid = gui.get_object("contentGrid")
submit_grid = gui.get_object("submitGrid")
chat_entry = gui.get_object("chatEntry")
submit_button = gui.get_object("submitButton")
content_notebook = gui.get_object("contentNotebook")
info_display = gui.get_object("infoDisplay")
channel_tab = gui.get_object("channelTab")
roster_text_view = gui.get_object("rosterTextView")
roster_tab = gui.get_object("rosterTab")


class communicator:
   def __init__(self):    
    hbs_communicator = gui.get_object("hbsCommunicator")

class Handler:
    def on_hbsCommunicator_delete_event(self,*args):
        Gtk.main_quit(*args)

    def on_submitButton_clicked(self, *args):
        info_buffer = info_display.get_buffer()
        chat_input = chat_entry.get_text()        
        chat_input += '\n' 
        info_buffer.insert(info_buffer.get_end_iter(),chat_input)
        chat_entry.set_text("")

    def on_chatEntry_activate(self, *args):
        Handler.on_submitButton_clicked(self, *args)
        #info_buffer = info_display.get_buffer()
        #chat_input = chat_entry.get_text()        
        #chat_input += '\n' 
        #info_buffer.insert(info_buffer.get_end_iter(),chat_input)
        #chat_entry.set_text("")

gui.connect_signals(Handler())
app.show_all()
Gtk.main()
