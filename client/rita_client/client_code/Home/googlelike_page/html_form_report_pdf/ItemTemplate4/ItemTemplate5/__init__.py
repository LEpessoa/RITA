from ._anvil_designer import ItemTemplate5Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ItemTemplate5(ItemTemplate5Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.countermeasure_repeating_panel.items = self.item['rcms']

    # Any code you write here will run before the form opens.
    
    
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    print(self.item)

