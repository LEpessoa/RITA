from ._anvil_designer import modelling_process_pageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class modelling_process_page(modelling_process_pageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def header_headline_1_show(self, **event_args):
    self.header_headline_1.scroll_into_view()

