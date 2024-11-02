from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...threat_types_page import threat_types_page

class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def related_threats_button_click(self, **event_args):    
    page = threat_types_page(threat_type_filter=(self.item['acronym'], None,None,None,None))
    self.set_open_form(page)
  
  def set_open_form(self, form):
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(form)

