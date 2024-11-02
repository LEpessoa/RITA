from ._anvil_designer import RowTemplate5Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class RowTemplate5(RowTemplate5Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def plus_button_click(self, **event_args):
    self.item['quantity'] = 1 # Add 1
    self.item = self.item # Update item      
    self.parent.raise_event('x-add_critical_object', critical_object=self.item)

  def minus_button_click(self, **event_args):
    if self.item['quantity'] == 0:
      return
    self.item['quantity'] -= 1 # Subtract 1
    self.item = self.item # Update item
    self.parent.raise_event('x-remove_critical_object', critical_object=self.item)


